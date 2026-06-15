import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/daily_revenue.csv")

df["Date"] = pd.to_datetime(df["Date"])

plt.figure(figsize=(12, 6))
plt.plot(df["Date"], df["Revenue"])

plt.title("Daily Revenue Trend")
plt.xlabel("Date")
plt.ylabel("Revenue")

plt.tight_layout()

plt.savefig("data/revenue_trend.png")

print("Graph saved as revenue_trend.png")