import sys
from collections import Counter
from pathlib import Path

from datasets import load_dataset, load_from_disk


DATA_DIR = Path(__file__).resolve().parent / "data" / "tweet_irony"

# 数据的加载、下载与保存
def load_or_download_dataset(data_dir):
    if data_dir.exists():
        dataset = load_from_disk(str(data_dir))
        print("Dataset loaded from local disk.")
        return dataset

    dataset = load_dataset(
        "cardiffnlp/tweet_eval",
        "irony",
    )
    data_dir.parent.mkdir(parents=True, exist_ok=True)
    dataset.save_to_disk(str(data_dir))
    print("Dataset downloaded and saved.")
    return dataset

# 数据的打印
def print_dataset_summary(dataset, sample_count=5):
    print(dataset)

    train_set = dataset["train"]

    for index in range(min(sample_count, len(train_set))):
        sample = train_set[index]
        label_name = "irony" if sample["label"] == 1 else "non-irony"
        print(index, sample["text"], label_name)

    label_counts = Counter(train_set["label"])
    print("标签分布：")
    print("irony (1) 数量：", label_counts[1])
    print("non-irony (0) 数量：", label_counts[0])
    print("总样本数：", len(train_set))


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    dataset = load_or_download_dataset(DATA_DIR)
    print_dataset_summary(dataset)


if __name__ == "__main__":
    main()
    