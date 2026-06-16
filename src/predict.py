import pandas as pd
import pickle

# Load features
df = pd.read_csv("data/features_revenue.csv")

# Load model
with open("pickle/model.pkl", "rb") as f:
    model = pickle.load(f)

# Features used by model
X = df[["Month", "DayOfWeek", "Lag1", "Rolling7"]]

# Predict
predictions = model.predict(X)

# Save output
output = pd.DataFrame({
    "Actual_Revenue": df["Revenue"],
    "Predicted_Revenue": predictions
})

output.to_csv(
    "data/predictions.csv",
    index=False
)

print("Predictions generated successfully!")
print(output.head())