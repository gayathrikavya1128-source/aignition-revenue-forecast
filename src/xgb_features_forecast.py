import pandas as pd
from xgboost import XGBRegressor

# Load features
df = pd.read_csv("data/features_revenue.csv")

# Input features
X = df[["Month", "DayOfWeek", "Lag1", "Rolling7"]]

# Target
y = df["Revenue"]

# Train model
model = XGBRegressor(
    n_estimators=300,
    max_depth=6,
    learning_rate=0.05,
    random_state=42
)

model.fit(X, y)

# Check training score
score = model.score(X, y)

print("Training R² Score:")
print(score)

import pickle

with open("pickle/model.pkl", "wb") as f:
    pickle.dump(model, f)

print("\nModel saved!")