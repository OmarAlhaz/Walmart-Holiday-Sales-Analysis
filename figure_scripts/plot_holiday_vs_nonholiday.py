import pandas as pd
import matplotlib.pyplot as plt
import os

# Paths
clean_data_path = os.path.join("outputs", "clean_data.csv")
figures_path = os.path.join("outputs", "figures")
os.makedirs(figures_path, exist_ok=True)

# Load clean data
clean_data = pd.read_csv(clean_data_path)

# Aggregate sales by Month and IsHoliday
agg = clean_data.groupby(['Month', 'IsHoliday'])['Weekly_Sales'].mean().reset_index()
pivot_df = agg.pivot(index='Month', columns='IsHoliday', values='Weekly_Sales')
pivot_df.columns = ['Non-Holiday', 'Holiday']

# Plot
plt.figure(figsize=(10,6))
plt.plot(pivot_df.index, pivot_df['Non-Holiday'], marker='o', label='Non-Holiday', color='blue')
plt.plot(pivot_df.index, pivot_df['Holiday'], marker='o', label='Holiday', color='red')
plt.title('Average Weekly Sales: Holiday vs Non-Holiday')
plt.xlabel('Month')
plt.ylabel('Average Weekly Sales')
plt.xticks(range(1,13))
plt.grid(True)
plt.legend()
plt.tight_layout()

# Save figure
plt.savefig(os.path.join(figures_path, 'holiday_vs_nonholiday.png'))
plt.show()
