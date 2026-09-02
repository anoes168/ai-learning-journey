from datasets import load_dataset,load_from_disk
import os

DATA_DIR = r"/data/tweet_irony"
cache_DIR = r"/datasets"
os.makedirs(cache_DIR, exist_ok=True)
os.makedirs(DATA_DIR, exist_ok=True)

ds = load_dataset(
    "cardiffnlp/tweet_eval",
    "irony",
    cache_dir = cache_DIR,
)

print(ds)
label_feature = ds["train"].features["label"]

print(label_feature.names)
ds.save_to_disk(DATA_DIR)


