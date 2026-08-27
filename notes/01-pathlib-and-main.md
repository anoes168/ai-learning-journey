# pathlib 与 main的初步认识

## 原代码的问题

使用本电脑的绝对D盘路径，在更换电脑后不能直接运行;模块首次被导入时，写在顶层的语句也会执行。

## pathlib 解决的问题

`__file__`表示当前Python脚本文件的路径。

`Path(__file__).resolve().parent`中，`resolve()`将路径转换为规范的绝对路径，并处理路径中的相对部分；`.parent`取得当前脚本所在的父目录。

使用`/`继续拼接`data`与`tweet_irony`目录。`Path`会根据操作系统处理具体的路径分隔符。

首次运行且父目录不存在时，使用`data_dir.parent.mkdir(parents=True, exist_ok=True)`创建父目录。`parents=True`表示连同缺失的上级目录一起创建，`exist_ok=True`表示目录已经存在时不报错。

## main入口是什么

直接启动的文件中，`__name__`等于`"__main__"`。

被其他文件导入时，`__name__`通常等于模块名，因此不会自动执行入口中的`main()`。

## 本次重构

- 删除绝对路径；
- 将数据加载和数据打印拆成函数；
- 使用main组织执行步骤；
- 让代码可以被其他文件导入复用。

