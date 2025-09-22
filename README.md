# 🛒 Walmart Holiday Sales Analysis

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![pandas](https://img.shields.io/badge/pandas-2.0+-yellow.svg)](https://pandas.pydata.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Project Status](https://img.shields.io/badge/Status-Completed-brightgreen.svg)]()

---

## 📌 Overview
Walmart is the largest retailer in the United States, with e-commerce sales reaching **$80B in 2022** (13% of total sales).  
One key driver of demand is **public holidays** such as the Super Bowl, Labor Day, Thanksgiving, and Christmas.  

This project builds a **data pipeline** in Python to analyze **supply and demand trends around holidays**.  
It covers **data extraction, transformation, aggregation**, and produces insights about sales patterns.

---

## 🎯 Objectives
- Build an **ETL pipeline** using **Python & Pandas**.  
- Merge multiple datasets (PostgreSQL export + Parquet complementary data).  
- Clean and transform data into a structured format.  
- Analyze **monthly sales trends** and the **impact of holidays**.  
- Export cleaned and aggregated data as CSVs.  

---

## 📂 Project Structure
```plaintext
Walmart-Holiday-Sales-Analysis/
│
├── data/                               # Raw datasets
│   ├── grocery_sales.csv
│   └── extra_data.parquet
│
├── docs/                               # Project documentation
│   ├── architecture.md                 # ETL pipeline diagram (Mermaid)
│   ├── data_catalog.md                 # Dataset dictionary
│   ├── findings.md                     # Key insights and analysis
│   └── setup.md                        # How to run the project
│
├── figure_scripts/                      # Scripts to generate visualizations
│   ├── plot_holiday_vs_nonholiday.py
│   └── plot_monthly_sales_trend.py
│
├── outputs/                             # Generated outputs
│   ├── clean_data.csv                   # Cleaned dataset
│   ├── agg_data.csv                     # Aggregated monthly sales
│   └── figures/                         # Figures generated from analysis
│       ├── holiday_vs_nonholiday.png
│       └── monthly_sales_trend.png
│
├── scripts/                             # ETL pipeline scripts
│   ├── extract.py                       # Extract data
│   ├── transform.py                     # Clean & transform data
│   ├── aggregate.py                     # Compute aggregations
│   ├── load.py                          # Save outputs
│   └── pipeline.py                      # Master ETL pipeline
│
├── tests/                               # Unit tests
│   └── test_pipeline.py
│
├── LICENSE                              # MIT License
├── README.md                             # Project overview and instructions
└── requirements.txt                      # Python dependencies
```
---

## 🔧 Pipeline Steps

1. **Extract**

   * Load sales (`grocery_sales.csv`) and complementary data (`extra_data.parquet`).
   * Merge on the `index` column.

2. **Transform**

   * Handle missing values (fill with column mean).
   * Convert `Date` → `Month`.
   * Filter out low-sales records (`Weekly_Sales` > 10,000).
   * Keep relevant features.

3. **Aggregate**

   * Group by month.
   * Compute average weekly sales.

4. **Load**

   * Save processed datasets:

     * `clean_data.csv` (filtered, clean dataset)
     * `agg_data.csv` (monthly average sales)

---

## 📊 Example Outputs

### Cleaned Data (sample)

| Store\_ID | Month | Dept | IsHoliday | Weekly\_Sales | CPI   | Unemployment |
| --------- | ----- | ---- | --------- | ------------- | ----- | ------------ |
| 1         | 2     | 5    | 0         | 15234.56      | 214.3 | 7.8          |
| 2         | 11    | 8    | 1         | 18342.11      | 216.5 | 7.5          |

### Aggregated Data

| Month | Avg\_Sales |
| ----- | ---------- |
| 1     | 33,174.18  |
| 2     | 34,333.32  |
| 11    | 45,892.55  |
| 12    | 48,421.10  |

---

## 📑 Documentation

* [docs/architecture.md](docs/architecture.md) → ETL flow diagram
* [docs/data\_catalog.md](docs/data_catalog.md) → Dataset dictionary
* [docs/findings.md](docs/findings.md) → Key insights (holiday vs non-holiday trends)
* [docs/setup.md](docs/setup.md) → How to run the pipeline

---

## 📌 Tech Stack

* **Python (pandas, numpy)** → Data manipulation
* **CSV + Parquet** → Data formats
* **PostgreSQL (source table)** → Original grocery sales
* **Modular ETL pipeline** → `extract`, `transform`, `aggregate`, `load`

---

## 🔍 Insights

* Sales spike significantly during **Thanksgiving & Christmas** (up to **40% higher** than early months).
* **Markdown promotions** amplify holiday demand.
* **Store type & size** strongly influence holiday sales performance.
* Economic factors (CPI, unemployment) have **weaker short-term effects** compared to seasonality.

---

## 🛡️ License

This project is licensed under the [MIT License](LICENSE). You are free to use, modify, and share this project with proper attribution.

---

## ✨ Contributors

Developed by [@OmarAlhaz](https://github.com/OmarAlhaz) and open for community contributions. Feel free to submit issues and PRs 🚀
