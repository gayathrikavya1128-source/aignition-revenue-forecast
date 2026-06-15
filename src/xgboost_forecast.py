import pandas as pd
import numpy as np
from xgboost import XGBRegressor

# Load data
df = pd.read_csv("data/daily_revenue.csv")

# Create day number
df["Day"] = np.arange(len(df))

X = df[["Day"]]
y = df["Revenue"]

# Train XGBoost
model = XGBRegressor(
    n_estimators=200,
    max_depth=5,
    learning_rate=0.05,
    random_state=42
)

model.fit(X, y)

# Predict next 30 days
future_days = np.arange(
    len(df),
    len(df) + 30
).reshape(-1, 1)

predictions = model.predict(future_days)

forecast = pd.DataFrame({
    "Future_Day": range(1, 31),
    "Predicted_Revenue": predictions
})

print(forecast.head())

forecast.to_csv(
    "data/xgboost_forecast_30_days.csv",
    index=False
)

print("\nXGBoost forecast saved!")