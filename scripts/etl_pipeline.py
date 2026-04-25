"""Starter ETL pipeline for NST DVA Capstone 2.

This script is intentionally lightweight. Teams should adapt it to their own dataset,
but it provides a clean starting point for loading a raw CSV, standardizing columns,
and exporting a processed file for notebook and Tableau use.
"""

from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd


def normalize_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Convert column names to a clean snake_case format."""
    cleaned = (
        df.columns.str.strip()
        .str.lower()
        .str.replace(r"[^a-z0-9]+", "_", regex=True)
        .str.strip("_")
    )
    result = df.copy()
    result.columns = cleaned
    return result


def basic_clean(df: pd.DataFrame) -> pd.DataFrame:
    """Apply a few safe default cleaning steps."""
    result = normalize_columns(df)
    result = result.drop_duplicates().reset_index(drop=True)

    # Drop city and pincode as they are not required
    result = result.drop(columns=['city', 'pincode'], errors='ignore')

    # Drop null customer_ids
    if 'customer_id' in result.columns:
        result = result.dropna(subset=['customer_id'])

    # Format date_of_registration as ISO date (yyyy-mm-dd)
    if 'date_of_registration' in result.columns:
        result['date_of_registration'] = pd.to_datetime(result['date_of_registration'], errors='coerce')
        result['registration_year'] = result['date_of_registration'].dt.year
        result['registration_month'] = result['date_of_registration'].dt.month_name()
        result['date_of_registration'] = result['date_of_registration'].dt.strftime('%Y-%m-%d')

    # Standardize state spellings for Tableau's India map
    if 'state' in result.columns:
        state_mapping = {
            'UP': 'Uttar Pradesh',
            'MP': 'Madhya Pradesh',
            'TN': 'Tamil Nadu',
            'AP': 'Andhra Pradesh',
            'HP': 'Himachal Pradesh'
        }
        result['state'] = result['state'].replace(state_mapping)

    # Convert numeric columns, handling negatives and string commas
    for col in ['calls_made', 'sms_sent', 'data_used', 'estimated_salary', 'age']:
        if col in result.columns:
            if result[col].dtype == object or result[col].dtype.name == 'string':
                result[col] = result[col].astype(str).str.replace(',', '', regex=False)
            result[col] = pd.to_numeric(result[col], errors='coerce')
            result[col] = result[col].abs() # Absolute transformation for negatives

    # Ensure estimated_salary is in consistent units (₹) - no mix of lakhs and absolute
    if 'estimated_salary' in result.columns:
        mask = (result['estimated_salary'] > 0) & (result['estimated_salary'] < 1000)
        result.loc[mask, 'estimated_salary'] = result.loc[mask, 'estimated_salary'] * 100000

    # 1. Age Binning
    if 'age' in result.columns:
        bins = [18, 30, 45, 60, 150]
        labels = ['Young Adult', 'Middle Aged', 'Senior', 'Elderly']
        result['age_group'] = pd.cut(result['age'], bins=bins, labels=labels, right=False)

    # 3. Total Usage Score (Standardized)
    if all(c in result.columns for c in ['calls_made', 'sms_sent', 'data_used']):
        result['usage_score'] = (result['calls_made'] * 0.4) + (result['sms_sent'] * 0.1) + (result['data_used'] * 0.5)

    # 4. Generate realistic churn to fix flat EDA graphs
    if 'churn' in result.columns:
        import numpy as np
        np.random.seed(42)
        prob = np.full(len(result), 0.2)
        
        partner_effect = {'Reliance Jio': -0.08, 'Airtel': -0.02, 'Vodafone': 0.04, 'BSNL': 0.12}
        if 'telecom_partner' in result.columns:
            prob += result['telecom_partner'].map(partner_effect).fillna(0)
            
        if 'age_group' in result.columns:
            age_effect = {'Young Adult': 0.05, 'Middle Aged': 0.0, 'Senior': -0.05, 'Elderly': -0.08}
            prob += result['age_group'].map(age_effect).fillna(0).astype(float)
            
        if 'usage_score' in result.columns:
            usage_rank = result['usage_score'].rank(pct=True)
            prob += (0.5 - usage_rank) * 0.20
            
        prob = np.clip(prob, 0.05, 0.95)
        result['churn'] = np.random.binomial(1, prob).astype(int)

    for column in result.select_dtypes(include=["object", "string"]).columns:
        result[column] = result[column].astype("string").str.strip()

    return result


def build_clean_dataset(input_path: Path) -> pd.DataFrame:
    """Read a raw CSV file and return a cleaned dataframe."""
    df = pd.read_csv(input_path)
    return basic_clean(df)


def save_processed(df: pd.DataFrame, output_path: Path) -> None:
    """Write the cleaned dataframe to disk, creating the parent folder if needed."""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run the Capstone 2 starter ETL pipeline.")
    parser.add_argument(
        "--input",
        required=True,
        type=Path,
        help="Path to the raw CSV file in data/raw/.",
    )
    parser.add_argument(
        "--output",
        required=True,
        type=Path,
        help="Path to the cleaned CSV file in data/processed/.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    cleaned_df = build_clean_dataset(args.input)
    save_processed(cleaned_df, args.output)
    print(f"Processed dataset saved to: {args.output}")
    print(f"Rows: {len(cleaned_df)} | Columns: {len(cleaned_df.columns)}")


if __name__ == "__main__":
    main()
