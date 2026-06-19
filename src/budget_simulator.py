import pandas as pd

# Load forecast data
forecast = pd.read_csv("data/30_day_forecast.csv")

# Average forecasted revenue
avg_revenue = forecast["Predicted_Revenue"].mean()

# Budget scenarios
budgets = [5000, 10000, 15000, 20000]

results = []

for budget in budgets:

    expected_revenue = avg_revenue * (budget / 10000)

    roas = expected_revenue / budget

    results.append({
        "Budget": budget,
        "Expected_Revenue": round(expected_revenue, 2),
        "Expected_ROAS": round(roas, 2)
    })

result_df = pd.DataFrame(results)

print(result_df)

result_df.to_csv(
    "data/budget_simulation.csv",
    index=False
)

print("\nBudget Simulation Saved!")