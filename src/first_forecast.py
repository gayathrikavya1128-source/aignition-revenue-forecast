import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

# Load data
df = pd.read_csv("data/daily_revenue.csv")

# Create day number
df["Day"] = np.arange(len(df))

# Features and target
X = df[["Day"]]
y = df["Revenue"]

# Train model
model = LinearRegression()
model.fit(X, y)

# Predict next 30 days
future_days = np.arange(len(df), len(df) + 30).reshape(-1, 1)

predictions = model.predict(future_days)

# Create forecast dataframe
forecast = pd.DataFrame({
    "Future_Day": range(1, 31),
    "Predicted_Revenue": predictions
})

print(forecast.head())

forecast.to_csv(
    "data/forecast_30_days.csv",
    index=False
)

print("\nForecast saved as forecast_30_days.csv")