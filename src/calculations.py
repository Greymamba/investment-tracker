
def calculate_net_worth(df):
    df['NetWorth'] = df['Investments'] - df['Liabilities']
    return df

def monthly_summary(df):
    print("\n📅 Monthly Summary:")
    for _, row in df.iterrows():
        print(f"{row['Month'].strftime('%B %Y')}: Net Worth = Ksh {row['NetWorth']:,.0f}")