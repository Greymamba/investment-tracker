import matplotlib.pyplot as plt

def plot_net_worth(df):
    plt.figure(figsize=(10, 5))
    plt.plot(df['Month'], df['NetWorth'], marker='o', color='green')
    plt.title('Net Worth Over Time')
    plt.xlabel('Month')
    plt.ylabel('Net Worth (Ksh)')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def plot_asset_allocation(df):
    latest = df.iloc[-1]
    labels = ['Investments', 'Liabilities']
    values = [latest['Investments'], latest['Liabilities']]
    colors = ['skyblue', 'salmon']

    plt.figure(figsize=(6, 6))
    plt.pie(values, labels=labels, autopct='%1.1f%%', colors=colors, startangle=140)
    plt.title(f'Asset Allocation ({latest["Month"].strftime("%B %Y")})')
    plt.tight_layout()
    plt.show()