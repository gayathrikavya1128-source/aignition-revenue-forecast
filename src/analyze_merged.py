import pandas as pd

df = pd.read_csv("data/merged_campaign_data.csv")

print("Shape:")
print(df.shape)

print("\nRevenue Summary:")
print(df["Revenue"].describe())

print("\nSpend Summary:")
print(df["Spend"].describe())

print("\nMissing Values:")
print(df.isnull().sum())