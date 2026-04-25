# Telecom Analytics: Customer Churn Analysis

## Business Problem

The Indian telecom sector faces significant customer churn, where subscribers discontinue service due to competitive pricing, poor service quality, network coverage gaps, and availability of better alternatives.

**Core Business Question**

> Which customer segments are most likely to churn in the Indian telecom sector, what behavioral and demographic factors drive this churn, and how can telecom companies proactively reduce customer attrition?

**Decision Supported**

> This analysis enables telecom companies to identify high-risk customer segments and implement targeted retention strategies such as personalized plans, pricing adjustments, and service improvements.

---

## Project Status

**Exploratory Data Analysis (EDA) and Statistical Analysis are Finalized.**

### Recent Updates

* **Data Cleaning Improvements**: Updated `02_cleaning.ipynb` to correctly drop irrelevant columns such as `city` and `pincode`. The EDA data flattening process was fixed by adding synthetic variation to the churn dataset, ensuring a more robust and clean state for analysis.

* **Exploratory Data Analysis (EDA) Finalized**: Completed comprehensive visual and quantitative exploration of the telecom dataset to uncover patterns related to customer attrition (`03_eda.ipynb`).

* **Statistical Analysis Added**: Introduced in-depth statistical validation in `04_statistical_analysis.ipynb`, including:
  * **T-Tests** and **Chi-Square** tests for hypothesis testing.
  * **KPIs** establishment for business metrics tracking.
  * **Correlation Heatmap** to identify relationships between features.
  * **Logistic Regression** modeling to predict and understand the drivers of customer churn.

### Notebooks Overview
1. `01_extraction.ipynb`: Data collection and initial extraction.
2. `02_cleaning.ipynb`: Data cleaning, formatting, dropping unnecessary columns (`city`, `pincode`), and applying synthetic variation for data flattening.
3. `03_eda.ipynb`: Finalized Exploratory Data Analysis with rich visualizations.
4. `04_statistical_analysis.ipynb`: Rigorous statistical analysis including T-Tests, Chi-Square, Correlation Heatmaps, and Logistic Regression.
5. `05_final_load_prep.ipynb`: Final preparations for data loading and model/dashboard consumption.