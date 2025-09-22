# 📚 Data Catalog

This document provides an overview of the datasets used in the **Walmart Holiday Sales Analysis** project.  
It describes **source data**, **transformed outputs**, and the **final aggregated dataset**.

---

## 🗂 Source Datasets

### 1. `grocery_sales.csv`
Exported from Walmart's sales database (PostgreSQL).  
Represents **weekly sales data** for each store.

| Column        | Type    | Description                                      |
|---------------|---------|--------------------------------------------------|
| index         | int     | Unique row identifier                            |
| Store_ID      | int     | Store number                                     |
| Date          | date    | Week of sales (YYYY-MM-DD)                       |
| Weekly_Sales  | float   | Total sales for that store and week              |

---

### 2. `extra_data.parquet`
Contains **complementary features** affecting sales, such as holiday flags, promotions, and economic indicators.

| Column        | Type    | Description                                      |
|---------------|---------|--------------------------------------------------|
| index         | int     | Join key (matches `grocery_sales.index`)         |
| IsHoliday     | int     | 1 if week contains a public holiday, else 0      |
| Temperature   | float   | Average temperature (°F) during the week         |
| Fuel_Price    | float   | Average fuel price in the region                 |
| CPI           | float   | Consumer Price Index                             |
| Unemployment  | float   | Regional unemployment rate (%)                   |
| MarkDown1–4   | float   | Promotional markdown values                      |
| Dept          | int     | Department number in each store                  |
| Size          | int     | Store size (square feet)                         |
| Type          | str     | Store type (A/B/C, correlated with size)         |

---

## 🧹 Transformed Dataset

### 3. `clean_data.csv`
Produced after **merging, cleaning, and filtering**.  
Includes only relevant columns for analysis.

| Column        | Type    | Description                                      |
|---------------|---------|--------------------------------------------------|
| Store_ID      | int     | Store number                                     |
| Month         | int     | Extracted month from `Date` (1–12)               |
| Dept          | int     | Department number                                |
| IsHoliday     | int     | 1 if week contains a holiday, else 0             |
| Weekly_Sales  | float   | Sales > 10,000 (filtered for meaningful records) |
| CPI           | float   | Consumer Price Index                             |
| Unemployment  | float   | Regional unemployment rate (%)                   |

---

## 📊 Aggregated Dataset

### 4. `agg_data.csv`
Monthly sales averages aggregated across all stores.

| Column        | Type    | Description                                      |
|---------------|---------|--------------------------------------------------|
| Month         | int     | Month number (1–12)                              |
| Avg_Sales     | float   | Average weekly sales for that month              |

---

## 🔑 Notes
- Missing values in `Weekly_Sales`, `CPI`, and `Unemployment` were **imputed with the mean**.  
- Only rows with `Weekly_Sales > 10,000` were included in the clean dataset to filter out low/no-sales records.  
- Final analysis focuses on **monthly sales trends** and the **impact of holidays**.
