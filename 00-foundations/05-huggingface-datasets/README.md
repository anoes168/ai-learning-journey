# Hugging Face数据集检查

## 我遇到的问题

此前知道标签0和1，但不知道如何从数据集本身查询含义。

## 数据集的层级

DatasetDict
→ train / validation / test
→ Dataset
→ text / label
→ label对应ClassLabel

## 查询标签

放最小代码和真实输出。

## 我的理解

变量名叫label并不能说明0和1的含义。
必须读取features中保存的ClassLabel信息。

## 容易犯的错误

不能因为模型输出LABEL_0，就直接假定它对应non_irony。