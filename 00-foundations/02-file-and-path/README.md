# 文件写入、CSV与路径处理

## 我在哪里遇到了它

实验结果需要保存到文本文件或CSV文件，但此前会读取数据，还没有独立创建和写入文件。

## 它解决什么问题

- `write()`：向已经打开的文件写入字符串。
- `csv.writer()`：按照CSV格式写入一行数据。
- `Path`：构造跨设备、跨目录更容易维护的路径。

CSV本质上是按行保存的文本文件。例如：

```text
experiment,accuracy,f1
baseline,0.6531,0.6450
```

## 最小示例

运行：

```powershell
python "00-foundations/02-file-and-path/examples.py"
```

程序会在本章的 `output` 目录中创建：

- `example.txt`
- `example.csv`

## 容易犯的错误

- `"w"` 会覆盖原文件；`"a"` 才是在文件末尾追加。
- `write()` 只能直接写字符串，数字通常要先转换为字符串。
- Windows写CSV时应设置 `newline=""`，避免产生多余空行。
- 中文文本建议明确设置 `encoding="utf-8"`。
