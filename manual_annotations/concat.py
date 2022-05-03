import pandas as pd


names = ["Marie", "Frida", "Magnus", "gustav", "viggo"]
tweet_ids = pd.read_csv(f"annotation_result_{names[0]}.csv")
tweet_ids = sorted(tweet_ids["idx"])

df = pd.DataFrame({"idx": tweet_ids})
for i, name in enumerate(names):
    df[name.title()] = pd.read_csv(f"annotation_result_{names[i]}.csv")[" irony"]
df.to_csv("annotation_results.csv")
