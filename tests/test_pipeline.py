"""
-------------------------------------------------
How to Run the Tests
-------------------------------------------------

1.Make sure you have pytest installed:
pip install pytest

2.Run tests from your repo root:
pytest tests/test_pipeline.py
"""

import os
import pandas as pd
import pytest

from scripts.extract import extract
from scripts.transform import transform
from scripts.aggregate import avg_weekly_sales_per_month
from scripts.load import load, validate

# Paths to test data
STORE_DATA = os.path.join("data", "grocery_sales.csv")
EXTRA_DATA = os.path.join("data", "extra_data.parquet")
OUTPUT_DIR = "outputs"

# Ensure output dir exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

CLEAN_FILE = os.path.join(OUTPUT_DIR, "clean_data_test.csv")
AGG_FILE = os.path.join(OUTPUT_DIR, "agg_data_test.csv")


def test_extract():
    """Test that extraction merges data correctly"""
    merged_df = extract(STORE_DATA, EXTRA_DATA)
    # Should not be empty
    assert not merged_df.empty
    # Must contain required columns
    required_columns = ['index', 'Store_ID', 'Date', 'Weekly_Sales', 'IsHoliday', 'Dept']
    for col in required_columns:
        assert col in merged_df.columns


def test_transform():
    """Test that transformation produces clean_data with correct columns"""
    merged_df = extract(STORE_DATA, EXTRA_DATA)
    clean_data = transform(merged_df)
    # Should not be empty
    assert not clean_data.empty
    # Should contain only relevant columns
    expected_cols = ['Store_ID', 'Month', 'Dept', 'IsHoliday', 'Weekly_Sales', 'CPI', 'Unemployment']
    assert list(clean_data.columns) == expected_cols
    # Weekly_Sales should all be > 10000
    assert all(clean_data['Weekly_Sales'] > 10000)


def test_aggregate():
    """Test that aggregation computes Avg_Sales per month"""
    merged_df = extract(STORE_DATA, EXTRA_DATA)
    clean_data = transform(merged_df)
    agg_data = avg_weekly_sales_per_month(clean_data)
    # Should have 'Month' and 'Avg_Sales'
    assert list(agg_data.columns) == ['Month', 'Avg_Sales']
    # Avg_Sales should be numeric
    assert pd.api.types.is_numeric_dtype(agg_data['Avg_Sales'])


def test_load_and_validate():
    """Test saving and validation of CSV outputs"""
    merged_df = extract(STORE_DATA, EXTRA_DATA)
    clean_data = transform(merged_df)
    agg_data = avg_weekly_sales_per_month(clean_data)

    load(clean_data, CLEAN_FILE, agg_data, AGG_FILE)

    # Validate files exist
    assert os.path.exists(CLEAN_FILE)
    assert os.path.exists(AGG_FILE)

    # Validate file contents
    df_clean = pd.read_csv(CLEAN_FILE)
    df_agg = pd.read_csv(AGG_FILE)

    assert not df_clean.empty
    assert not df_agg.empty
    assert list(df_clean.columns) == ['Store_ID', 'Month', 'Dept', 'IsHoliday', 'Weekly_Sales', 'CPI', 'Unemployment']
    assert list(df_agg.columns) == ['Month', 'Avg_Sales']
