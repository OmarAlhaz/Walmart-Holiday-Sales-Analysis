import pandas as pd

def transform(raw_data):
    """Clean and transform merged dataset."""
    # Handle missing values
    raw_data.fillna(
        {
            "Weekly_Sales": raw_data["Weekly_Sales"].mean(),
            "CPI": raw_data["CPI"].mean(),
            "Unemployment": raw_data["Unemployment"].mean(),
        },
        inplace=True,
    )

    # Extract month
    raw_data["Date"] = pd.to_datetime(raw_data["Date"], format="%Y-%m-%d")
    raw_data["Month"] = raw_data["Date"].dt.month

    # Filter & select columns
    clean_data = raw_data.loc[
        raw_data["Weekly_Sales"] > 10000,
        ["Store_ID", "Month", "Dept", "IsHoliday", "Weekly_Sales", "CPI", "Unemployment"],
    ]

    return clean_data
