import os
from extract import extract
from transform import transform
from aggregate import avg_weekly_sales_per_month
from load import load, validate

def main():
    # Define input paths
    store_data_path = os.path.join("data", "grocery_sales.csv")
    extra_data_path = os.path.join("data", "extra_data.parquet")

    # Extract
    print("📥 Extracting data...")
    merged_df = extract(store_data_path, extra_data_path)

    # Transform
    print("🔄 Transforming data...")
    clean_data = transform(merged_df)

    # Aggregate
    print("📊 Aggregating data...")
    agg_data = avg_weekly_sales_per_month(clean_data)

    # Define outputs
    output_dir = "outputs"
    os.makedirs(output_dir, exist_ok=True)

    clean_file_path = os.path.join(output_dir, "clean_data.csv")
    agg_file_path = os.path.join(output_dir, "agg_data.csv")

    # Load
    print("💾 Saving outputs...")
    load(clean_data, clean_file_path, agg_data, agg_file_path)

    # Validate
    print("✅ Validating saved files...")
    validate(clean_file_path)
    validate(agg_file_path)

    print("🎉 Pipeline completed successfully!")

if __name__ == "__main__":
    main()
