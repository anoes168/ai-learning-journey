import csv
from pathlib import Path


OUTPUT_DIR = Path(__file__).resolve().parent / "output"


def write_text_file():
    text_path = OUTPUT_DIR / "example.txt"
    with text_path.open("w", encoding="utf-8") as file:
        file.write("第一次练习文件写入。\n")
        file.write("write() 写入的是字符串。\n")
    return text_path


def write_csv_file():
    csv_path = OUTPUT_DIR / "example.csv"
    with csv_path.open("w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["experiment", "accuracy", "f1"])
        writer.writerow(["baseline", 0.6531, 0.6450])
    return csv_path


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    print("文本文件：", write_text_file())
    print("CSV文件：", write_csv_file())


if __name__ == "__main__":
    main()
