import pandas as pd

df = pd.read_csv("data/merged_campaign_data.csv")

total_revenue = df["Revenue"].sum()
total_spend = df["Spend"].sum()

roas = total_revenue / total_spend

print("Total Revenue:", round(total_revenue, 2))
print("Total Spend:", round(total_spend, 2))
print("Blended ROAS:", round(roas, 2))