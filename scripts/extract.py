import pandas as pd

def extract(store_data_path, extra_data_path):
    """Extract and merge sales & extra datasets."""
    store_df = pd.read_csv(store_data_path)
    extra_df = pd.read_parquet(extra_data_path)
    merged_df = store_df.merge(extra_df, on="index")
    return merged_df
