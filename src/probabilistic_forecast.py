import pandas as pd

df = pd.read_csv("data/30_day_forecast.csv")

df["Lower_Bound"] = df["Predicted_Revenue"] * 0.90
df["Upper_Bound"] = df["Predicted_Revenue"] * 1.10

print(df.head())

df.to_csv(
    "data/probabilistic_forecast.csv",
    index=False
)

print("\nProbabilistic Forecast Saved!")