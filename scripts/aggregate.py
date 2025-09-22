def avg_weekly_sales_per_month(clean_data):
    """Aggregate data by month and compute average weekly sales."""
    agg_data = clean_data.groupby("Month")["Weekly_Sales"].mean().reset_index()
    agg_data.rename(columns={"Weekly_Sales": "Avg_Sales"}, inplace=True)
    return agg_data
