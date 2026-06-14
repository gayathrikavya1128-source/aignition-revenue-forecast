import pandas as pd

google = pd.read_csv("data/google_ads_campaign_stats.csv")

print("Total Revenue:")
print(google["metrics_conversions_value"].sum())

print("\nTotal Spend:")
print(google["metrics_cost_micros"].sum()/1000000)

print("\nTotal Conversions:")
print(google["metrics_conversions"].sum())