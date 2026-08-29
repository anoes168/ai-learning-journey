# PyTorch张量基础

## 我在哪里遇到了它

已经能够理解张量和矩阵形状，但在写代码时遇到了 `torch.arange()` 等基础API缺口。

## `torch.arange()` 解决什么问题

它按照起点、终点和步长生成一维张量：

```python
torch.arange(start, end, step)
```

其中包含 `start`，但不包含 `end`。

## 最小示例

运行：

```powershell
python "00-foundations/04-pytorch-tensors/examples.py"
```

## 容易犯的错误

- `torch.arange(0, 5)` 的结果不包含 `5`。
- `reshape()` 前后元素总数必须相同。
- `shape` 描述每个维度的长度，不等于张量中的具体数值。
