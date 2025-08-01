import pandas as pd
from calculations import calculate_net_worth, monthly_summary
from visualizations import plot_net_worth, plot_asset_allocation

# 🟢 Add this function near the top
def load_data(filepath):
    try:
        df = pd.read_csv(filepath, parse_dates=['Month'])
        if df.empty:
            raise ValueError("CSV file is empty.")
        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        return pd.DataFrame()

# 🟢 Load your data
df = load_data("data/sample_data.csv")

# 🧮 Perform calculations
df = calculate_net_worth(df)
monthly_summary(df)

# 📊 Visualize results
plot_net_worth(df)
plot_asset_allocation(df)