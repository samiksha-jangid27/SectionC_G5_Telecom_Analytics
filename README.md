# 📡 Telecom Customer Analytics — SectionC_G5

> **DVA Capstone 2 | Newton School of Technology**
> Sector: Telecommunications | Team: Section C, Group 5

---

## 🔍 Project Overview

This project analyses **243,553 telecom customer records** across 4 Indian operators (Airtel, BSNL, Reliance Jio, Vodafone) spanning 28 states. We built an end-to-end analytics pipeline — from raw data ingestion to Tableau dashboards — to uncover the drivers of a **20.05% churn rate** and deliver actionable retention strategies.

**Business Question:**  
*Which customer segments are most at risk of churning, and what operational interventions can reduce churn by at least 10% within 6 months?*

---

## 👥 Team Members

| Name | Role | Email |
|------|------|-------|
| Samiksha Jangid | Project Lead / Visualization Lead | samiksha.jangid2024@nst.rishihood.edu.in |
| Gauri Jindal | Analysis Lead | gauri.jindal2024@nst.rishihood.edu.in |
| Abhishek Rana | ETL Lead | abhishek.rana2024@nst.rishihood.edu.in |
| Rudraksh | Data Lead | rudraksh.2024@nst.rishihood.edu.in |
| Ritik Raj | Strategy Lead | ritik.raj2024@nst.rishihood.edu.in |
| Aryan | PPT & Quality Lead | aryan.a2024@nst.rishihood.edu.in |

**Institute:** Newton School of Technology, Rishihood University

---

## 📊 Tableau Dashboard

🔗 **Live Dashboard:** [View on Tableau Public](https://public.tableau.com/views/Telecom_analysis_17774577765420/Dashboard3?:language=en-US&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)

| Dashboard | Focus |
|-----------|-------|
| Dashboard 1 | Telecom Market Overview |
| Dashboard 2 | Customer Churn Analysis |
| Dashboard 3 | Engagement Distribution |
| Dashboard 4 | Customer Segmentation |

Screenshots are in [`tableau/screenshots/`](./tableau/screenshots/)

---

## 📁 Repository Structure

```
SectionC_G5_Telecom_Analytics/
│
├── README.md                          ← You are here
│
├── data/
│   ├── raw/
│   │   └── telecom_raw.csv            ← Original dataset (never edited)
│   └── processed/
│       └── telecom_cleaned.csv        ← Cleaned output from pipeline
│
├── notebooks/
│   ├── 01_extraction.ipynb            ← Data loading & initial inspection
│   ├── 02_cleaning.ipynb              ← ETL pipeline & transformation log
│   ├── 03_eda.ipynb                   ← Exploratory data analysis
│   ├── 04_statistical_analysis.ipynb  ← Correlation, regression, hypothesis tests
│   └── 05_final_load_prep.ipynb       ← KPI computation & Tableau-ready export
│
├── scripts/
│   └── etl_pipeline.py                ← Standalone ETL script
│
├── tableau/
│   ├── screenshots/                   ← Dashboard screenshots (PNG)
│   └── dashboard_links.md             ← Tableau Public URL
│
├── reports/
│   ├── project_report.pdf             ← Final written report (10–15 pages)
│   └── presentation.pdf              ← Final presentation deck
│
├── docs/
│   └── data_dictionary.md             ← Column definitions & data quality notes
│
└── DVA-oriented-Resume/               ← Individual resumes (per member)
```

---

## 📦 Dataset

| Attribute | Detail |
|-----------|--------|
| **Source** | Synthetic Indian Telecom Dataset (Kaggle) |
| **Records** | 243,553 customer rows |
| **Columns** | 19 columns (raw) |
| **Time Range** | January 2020 – December 2023 |
| **Operators Covered** | Airtel, BSNL, Reliance Jio, Vodafone |
| **States Covered** | 28 Indian states |
| **Cities Covered** | 96 cities |

---

## 🔑 Key Metrics (All-Time)

| KPI | Value |
|-----|-------|
| Total Customers | 243,553 |
| **Churn Rate** | **20.05%** |
| Total Churned | 48,827 |
| Total Retained | 194,726 |
| Avg Annual Income | ₹85,021 |
| Avg Customer Age | 46.08 years |
| Avg Data Usage | 5,010 GB/month |
| Avg Monthly Calls | 49.23 |
| Highest Churning Operator | Airtel (20.37%) |

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.x | ETL, EDA, Statistical Analysis |
| Pandas, NumPy | Data manipulation |
| Matplotlib, Seaborn | Python visualisations |
| SciPy, Statsmodels | Statistical testing |
| Tableau Public | Interactive dashboards |
| GitHub | Version control & collaboration |
| Google Colab | Notebook environment |

---

## 🚀 How to Run

### 1. Clone the repository
```bash
git clone https://github.com/samiksha-jangid27/SectionC_G5_Telecom_Analytics.git
cd SectionC_G5_Telecom_Analytics
```

### 2. Install dependencies
```bash
pip install pandas numpy matplotlib seaborn scipy statsmodels jupyter
```

### 3. Run notebooks in order
```bash
jupyter notebook notebooks/01_extraction.ipynb
# Then 02 → 03 → 04 → 05
```

### 4. View dashboards
Open the Tableau Public link in [`tableau/dashboard_links.md`](./tableau/dashboard_links.md)

---

## 💡 Key Insights

1. **Uniform churn across operators** — All four operators maintain churn between 19.86%–20.37%, suggesting a systemic market issue rather than operator-specific failures.
2. **Elderly customers churn most** — The 65+ age band shows the highest absolute churn count (12,999 customers).
3. **Male customers churn more** — 29,022 male vs. 19,805 female churned customers; however, female churn rate (20.30%) is marginally higher.
4. **Churn is age-agnostic** — Average age of churned customers is 46.1, nearly identical to the overall average (46.08).
5. **Jharkhand leads state-level churn** at 21.12%, followed by Karnataka (20.71%) and Mizoram (20.65%).
6. **Engagement score does NOT predict churn** — Churned (2,529) and retained (2,526) customers have nearly identical engagement scores, suggesting engagement metrics alone are insufficient retention indicators.
7. **Income is not a churn driver** — Churned customers earn ₹84,772 vs. retained ₹85,084 — essentially the same.
8. **2023 churn dropped sharply** — Only 4,917 churn events recorded in 2023 vs. 14,644 in 2022, likely due to partial year data.
9. **Top cities by volume** — Agartala (8,660) and Imphal (8,651) lead city-level customer counts.
10. **Northeast India dominates** — Top 10 cities by customer count are all from northeastern states.

---

## 📋 Business Recommendations

1. **Deploy personalised retention campaigns for Elderly and Male segments** — these groups contribute disproportionately to churn counts.
2. **Investigate Jharkhand, Karnataka, and Mizoram** for state-level service quality or pricing issues driving above-average churn.
3. **Redefine engagement KPIs** — current engagement score shows no predictive power for churn; incorporate recency, frequency, and monetary metrics.
4. **Implement proactive win-back triggers at the 2-year mark** — churn is consistent year-over-year, suggesting a tenure cliff.
5. **Conduct competitive pricing review** — cross-operator churn uniformity implies customers are switching for price/plan reasons rather than service quality.

---

## 📝 Contribution Matrix

| Member | Key Contributions |
|--------|------------------|
| Samiksha Jangid | Project leadership, Tableau dashboard (all 4 views), GitHub repo management |
| Gauri Jindal | Statistical analysis (notebook 04), churn analysis, visualisation design |
| Abhishek Rana | ETL pipeline (notebooks 01 & 02), data cleaning, GitHub commits |
| Rudraksh | Dataset sourcing, data dictionary, initial EDA (notebook 03) |
| Ritik Raj | Problem statement, KPI framework, business recommendations |
| Aryan | Final report (PDF), presentation deck, contribution matrix |


---

*Submitted for DVA Capstone 2 | Newton School of Technology | April 2026*
