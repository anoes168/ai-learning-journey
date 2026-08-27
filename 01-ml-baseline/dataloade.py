from datasets import load_dataset,load_from_disk
import os
DATA_DIR = r"D:\all_study\my-ml-study\data\tweet_irony"
# 数据下载
if not os.path.exists(DATA_DIR):
    ds = load_dataset(
        "cardiffnlp/tweet_eval",
        "irony",
    cache_dir=r"D:\all_study\my-ml-study\datasets"
    )
else:
    ds = load_from_disk(DATA_DIR)
print(ds)
print(ds["train"][:5])
for i in range(5):
    label = "irony" if ds["train"][i]["label"] == 1 else "no-irony"
    print(i,ds["train"][i]["text"],label)

labels = [sample["label"] for sample in ds["train"]]
print("标签分布：")
print("irony (1) 数量:", labels.count(1))
print("no-irony (0) 数量:", labels.count(0))
print("总样本数:", len(labels))

from collections import Counter
print("\nCounter统计：", Counter(labels))

if os.path.exists(DATA_DIR):
    print("already saved")
else:
    ds.save_to_disk(DATA_DIR)
    print("first save")
