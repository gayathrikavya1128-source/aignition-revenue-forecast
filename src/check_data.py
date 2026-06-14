import pandas as pd

google = pd.read_csv("data/google_ads_campaign_stats.csv")
meta = pd.read_csv("data/meta_ads_campaign_stats.csv")
bing = pd.read_csv("data/bing_campaign_stats.csv")

print("Google Rows:", google.shape)
print("Meta Rows:", meta.shape)
print("Bing Rows:", bing.shape)