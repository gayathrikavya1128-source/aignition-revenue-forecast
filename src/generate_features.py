import pandas as pd

# Load merged data
df = pd.read_csv("data/merged_campaign_data.csv")

# Date conversion
df["Date"] = pd.to_datetime(df["Date"])

# Daily revenue
daily = (
    df.groupby("Date")["Revenue"]
    .sum()
    .reset_index()
)

# Features
daily["Month"] = daily["Date"].dt.month
daily["DayOfWeek"] = daily["Date"].dt.dayofweek

daily["Lag1"] = daily["Revenue"].shift(1)
daily["Rolling7"] = daily["Revenue"].rolling(7).mean()

daily = daily.dropna()

# Save
daily.to_csv(
    "data/features_revenue.csv",
    index=False
)

print("Features generated successfully!")
print(daily.head())