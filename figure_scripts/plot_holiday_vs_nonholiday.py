import pandas as pd
import matplotlib.pyplot as plt
import os

# Paths
clean_data_path = os.path.join("outputs", "clean_data.csv")
figures_path = os.path.join("outputs", "figures")
os.makedirs(figures_path, exist_ok=True)

# Load data
clean_data = pd.read_csv(clean_data_path)

# Aggregate weekly sales
agg = clean_data.groupby(['Month', 'IsHoliday'])['Weekly_Sales'].mean().reset_index()
agg['IsHoliday'] = agg['IsHoliday'].map({0: 'Non-Holiday', 1: 'Holiday'})

# Pivot for bar chart
pivot_df = agg.pivot(index='Month', columns='IsHoliday', values='Weekly_Sales')

# Plot grouped bar chart
pivot_df.plot(kind='bar', stacked=True, figsize=(12,6), color=['skyblue','salmon'])
plt.title('Stacked Weekly Sales: Holiday vs Non-Holiday by Month')
plt.xlabel('Month')
plt.ylabel('Weekly Sales')
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.legend(title='')
plt.tight_layout()
plt.savefig(os.path.join(figures_path, "holiday_vs_nonholiday_stacked.png"))
plt.show()

# Save figure
plt.savefig(os.path.join(figures_path, "holiday_vs_nonholiday_bar.png"))
plt.show()
