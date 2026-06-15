import pandas as pd

df = pd.read_csv("data/daily_revenue.csv")

df["Date"] = pd.to_datetime(df["Date"])

# Calendar features
df["Month"] = df["Date"].dt.month
df["DayOfWeek"] = df["Date"].dt.dayofweek

# Lag feature
df["Lag1"] = df["Revenue"].shift(1)

# Rolling average
df["Rolling7"] = df["Revenue"].rolling(7).mean()

# Remove empty rows
df = df.dropna()

print(df.head())

print("\nShape:")
print(df.shape)

df.to_csv(
    "data/features_revenue.csv",
    index=False
)

print("\nFeatures saved!")