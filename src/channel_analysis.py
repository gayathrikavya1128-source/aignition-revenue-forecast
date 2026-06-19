import pandas as pd

df = pd.read_csv("data/merged_campaign_data.csv")

channel_summary = (
    df.groupby("Channel")
    .agg({
        "Revenue":"sum",
        "Spend":"sum"
    })
)

channel_summary["ROAS"] = (
    channel_summary["Revenue"] /
    channel_summary["Spend"]
)

print(channel_summary)