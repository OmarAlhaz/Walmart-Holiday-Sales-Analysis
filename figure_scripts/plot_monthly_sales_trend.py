import pandas as pd
import matplotlib.pyplot as plt
import os

# Paths
clean_data_path = os.path.join("outputs", "clean_data.csv")
figures_path = os.path.join("outputs", "figures")
os.makedirs(figures_path, exist_ok=True)

# Load clean data
clean_data = pd.read_csv(clean_data_path)

# Aggregate average weekly sales by month
monthly_avg = clean_data.groupby('Month')['Weekly_Sales'].mean().reset_index()

# Plot
plt.figure(figsize=(10,6))
plt.plot(monthly_avg['Month'], monthly_avg['Weekly_Sales'], marker='o', color='green', label='Avg Weekly Sales')
plt.title('Monthly Average Weekly Sales Across All Stores')
plt.xlabel('Month')
plt.ylabel('Average Weekly Sales')
plt.xticks(range(1,13))
plt.grid(True)
plt.legend()
plt.tight_layout()

# Save figure
plt.savefig(os.path.join(figures_path, 'monthly_sales_trend.png'))
plt.show()
