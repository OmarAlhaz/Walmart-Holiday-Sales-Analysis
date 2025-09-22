# 📊 Pipeline Architecture

The Walmart Holiday Sales Analysis project follows a simple ETL (Extract → Transform → Load) workflow.

```mermaid
flowchart TD
    A[📥 Extract Data] --> B[🔄 Transform Data]
    B --> C[📊 Aggregate Sales by Month]
    C --> D[💾 Load to CSV Outputs]

    subgraph Inputs
        A1[grocery_sales.csv]
        A2[extra_data.parquet]
    end

    subgraph Outputs
        D1[clean_data.csv]
        D2[agg_data.csv]
    end

    A1 --> A
    A2 --> A
    D --> D1
    D --> D2
````

---

## 🔧 Steps Explained

1. **Extract**

   * Load sales data (`grocery_sales.csv`)
   * Load complementary data (`extra_data.parquet`)
   * Merge datasets on the `index` field

2. **Transform**

   * Handle missing values
   * Convert `Date` → `Month`
   * Filter `Weekly_Sales > 10,000`
   * Select relevant features

3. **Aggregate**

   * Group by `Month`
   * Compute average `Weekly_Sales` → `Avg_Sales`

4. **Load**

   * Save `clean_data.csv` (clean dataset)
   * Save `agg_data.csv` (aggregated dataset)
