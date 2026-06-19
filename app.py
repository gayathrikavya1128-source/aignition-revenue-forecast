import streamlit as st
import pandas as pd

st.title("📈 AIgnition Revenue Forecast Dashboard")

# ROAS Summary
revenue = 11095456.29
spend = 2181943.02
roas = revenue / spend

st.subheader("Business Summary")

st.metric("Total Revenue", f"₹{revenue:,.0f}")
st.metric("Total Spend", f"₹{spend:,.0f}")
st.metric("Blended ROAS", round(roas, 2))

# Forecast Data
forecast = pd.read_csv("data/30_day_forecast.csv")

st.subheader("30 Day Revenue Forecast")

st.line_chart(
    forecast["Predicted_Revenue"]
)

st.dataframe(forecast.head())

st.subheader("Budget Simulator")

st.subheader("Channel Performance")

channel_data = {
    "Google": 9266678,
    "Meta": 1656751,
    "Bing": 172028
}

channel_df = pd.DataFrame(
    channel_data.items(),
    columns=["Channel", "Revenue"]
)

st.bar_chart(
    channel_df.set_index("Channel")
)

budget = st.slider(
    "Select Marketing Budget",
    5000,
    50000,
    10000,
    1000
)

avg_rev = forecast["Predicted_Revenue"].mean()

expected_revenue = avg_rev * (budget / 10000)

expected_roas = expected_revenue / budget

st.metric(
    "Expected Revenue",
    f"₹{expected_revenue:,.0f}"
)

st.metric(
    "Expected ROAS",
    round(expected_roas, 2)
)