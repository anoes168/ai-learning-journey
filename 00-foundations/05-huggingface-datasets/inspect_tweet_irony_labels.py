from datasets import load_dataset,load_from_disk
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data" / "tweet_irony"
cache_DIR = BASE_DIR / "hf-cache"
cache_DIR.mkdir(parents=True, exist_ok=True)
DATA_DIR.mkdir(parents=True, exist_ok=True)

ds = load_dataset(
    "cardiffnlp/tweet_eval",
    "irony",
    cache_dir = str(cache_DIR),
)

print(ds)
label_feature = ds["train"].features["label"]

print(label_feature.names)
ds.save_to_disk(str(DATA_DIR))

