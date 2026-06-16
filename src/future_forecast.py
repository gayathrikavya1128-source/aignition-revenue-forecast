import pandas as pd
import pickle

# Load model
with open("pickle/model.pkl", "rb") as f:
    model = pickle.load(f)

# Load feature data
df = pd.read_csv("data/features_revenue.csv")

# Last known values
last_row = df.iloc[-1]

month = int(last_row["Month"])
dow = int(last_row["DayOfWeek"])

lag1 = float(last_row["Revenue"])
rolling7 = float(df["Revenue"].tail(7).mean())

forecast = []

for day in range(1, 31):

    X_future = pd.DataFrame({
        "Month": [month],
        "DayOfWeek": [(dow + day) % 7],
        "Lag1": [lag1],
        "Rolling7": [rolling7]
    })

    pred = model.predict(X_future)[0]

    forecast.append({
        "Future_Day": day,
        "Predicted_Revenue": pred
    })

    lag1 = pred

forecast_df = pd.DataFrame(forecast)

forecast_df.to_csv(
    "data/30_day_forecast.csv",
    index=False
)

print(forecast_df.head())
print("\n30 Day Forecast Saved!")