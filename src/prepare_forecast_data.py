import pandas as pd

# Load merged dataset
df = pd.read_csv("data/merged_campaign_data.csv")

# Convert Date column
df["Date"] = pd.to_datetime(df["Date"])

# Aggregate revenue by day
daily_revenue = (
    df.groupby("Date")["Revenue"]
    .sum()
    .reset_index()
)

print("First 5 Rows:")
print(daily_revenue.head())

print("\nRows:")
print(daily_revenue.shape)

# Save
daily_revenue.to_csv(
    "data/daily_revenue.csv",
    index=False
)

print("\nSaved daily_revenue.csv")