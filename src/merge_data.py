import pandas as pd

# Google
google = pd.read_csv("data/google_ads_campaign_stats.csv")

google_clean = pd.DataFrame({
    "Date": google["segments_date"],
    "Channel": "Google",
    "Revenue": google["metrics_conversions_value"],
    "Spend": google["metrics_cost_micros"] / 1000000,
    "Campaign": google["campaign_name"]
})

print("Google Done")
print(google_clean.head())

# Meta
meta = pd.read_csv("data/meta_ads_campaign_stats.csv")

meta_clean = pd.DataFrame({
    "Date": meta["date_start"],
    "Channel": "Meta",
    "Revenue": meta["conversion"],
    "Spend": meta["spend"],
    "Campaign": meta["campaign_name"]
})

print("\nMeta Done")
print(meta_clean.head())

# Bing
bing = pd.read_csv("data/bing_campaign_stats.csv")

bing_clean = pd.DataFrame({
    "Date": bing["TimePeriod"],
    "Channel": "Bing",
    "Revenue": bing["Revenue"],
    "Spend": bing["Spend"],
    "Campaign": bing["CampaignName"]
})

print("\nBing Done")
print(bing_clean.head())

# Merge all datasets
merged = pd.concat(
    [google_clean, meta_clean, bing_clean],
    ignore_index=True
)

print("\nMerged Dataset Shape:")
print(merged.shape)

print("\nChannels:")
print(merged["Channel"].value_counts())

# Save merged dataset
merged.to_csv("data/merged_campaign_data.csv", index=False)

print("\nFile Saved Successfully!")