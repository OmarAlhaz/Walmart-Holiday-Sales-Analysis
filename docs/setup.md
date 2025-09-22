# ⚙️ Setup & Installation Guide

This guide explains how to set up and run the **Walmart Holiday Sales Analysis** project.

---

## 📦 1. Clone the Repository

```bash
git clone https://github.com/OmarAlhaz/Walmart-Holiday-Sales-Analysis.git
cd Walmart-Holiday-Sales-Analysis
````

---

## 🐍 2. Set Up Python Environment

It is recommended to use **Python 3.10+** and a virtual environment.

```bash
# Create a virtual environment
python -m venv venv

# Activate it
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate
```

---

## 📚 3. Install Dependencies

Install required Python libraries:

```bash
pip install -r requirements.txt
```

Dependencies include:

* **pandas** → data wrangling
* **pyarrow / fastparquet** → parquet file support
* **numpy** → numerical processing

---

## 🗂️ 4. Project Structure

```plaintext
Walmart-Holiday-Sales-Analysis/
│── data/            # Raw datasets (CSV, Parquet)
│── scripts/         # ETL pipeline scripts
│── outputs/         # Saved results
│── docs/            # Documentation
│── tests/           # Unit tests
│── requirements.txt # Dependencies
│── README.md        # Project overview
```

---

## 🚀 5. Run the Pipeline

To run the **full ETL pipeline** (Extract → Transform → Aggregate → Load):

```bash
python scripts/pipeline.py
```

This will:

* Merge and clean datasets
* Save cleaned data → `outputs/clean_data.csv`
* Save aggregated results → `outputs/agg_data.csv`
* Validate that the files were saved successfully

---

## 📊 6. Outputs

After running the pipeline, you should see:

* `outputs/clean_data.csv` → Clean dataset for analysis
* `outputs/agg_data.csv` → Monthly average sales

Optional: Place charts/figures in `outputs/figures/`.

---

## 🧪 7. Run Tests (Optional)

To validate pipeline functions, run:

```bash
pytest tests/
```

---

## 🔑 Notes

* Ensure the input files are available in the `data/` folder:

  * `grocery_sales.csv`
  * `extra_data.parquet`
* If you replace datasets, rerun `pipeline.py` to regenerate outputs.
* Outputs are overwritten each time the pipeline is executed.

---

✅ You’re now ready to explore **holiday sales trends** at Walmart!
