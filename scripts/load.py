import os

def load(clean_data, clean_file_path, agg_data, agg_file_path):
    """Save cleaned and aggregated datasets to CSV."""
    clean_data.to_csv(clean_file_path, index=False)
    agg_data.to_csv(agg_file_path, index=False)

    print(f"✅ Cleaned data saved to {clean_file_path}")
    print(f"✅ Aggregated data saved to {agg_file_path}")

def validate(file_path):
    """Validate file existence and print preview."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Validation failed: {file_path} does not exist.")
    print(f"✅ Validation successful: {file_path}")
