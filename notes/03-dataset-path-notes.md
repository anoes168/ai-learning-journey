# 数据集脚本随记

这次代码主要做了两件事：把数据保存路径改成跟着脚本走，还有就是从数据集本身查看0和1对应什么标签。

`__file__`表示当前这个Python文件的位置。`Path(__file__).resolve()`会得到它完整的路径，后面的`.parent`再取出文件所在的文件夹。所以：

```python
BASE_DIR = Path(__file__).resolve().parent
```

得到的是当前脚本所在目录，不再依赖我电脑上写死的D盘路径。

Path后面使用的`/`不是除法，而是在拼接路径：

```python
DATA_DIR = BASE_DIR / "data" / "tweet_irony"
```

`mkdir()`用来创建文件夹。`parents=True`表示上级文件夹不存在时一起创建，`exist_ok=True`表示文件夹已经存在也不要报错。

有些库接收路径时更习惯普通字符串，所以代码用了`str(cache_DIR)`，把Path对象转成字符串。Path本身更适合在自己的代码里拼接和修改路径。

`load_dataset()`负责从Hugging Face加载数据集。这里的`"cardiffnlp/tweet_eval"`是数据集名称，后面的`"irony"`是这个数据集使用的配置名称，不是标签编号。

```python
ds["train"]
```

这里是在DatasetDict中取出训练集。再通过：

```python
ds["train"].features["label"]
```

取得label这一列的说明。它是ClassLabel，`.names`中保存了数字标签对应的名称。这次实际看到的是0对应`non_irony`，1对应`irony`，以后不能只靠猜或者问AI。

`save_to_disk()`把整个DatasetDict保存到本地，之后可以用`load_from_disk()`重新读取。当前脚本虽然导入了`load_from_disk`，但暂时没有真正调用它，是原始代码里留下来的。
