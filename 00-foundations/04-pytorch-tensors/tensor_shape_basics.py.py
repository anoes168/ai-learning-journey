import torch
#arange 生成一维向量
x = torch.arange(0,12)
print(x)

# shape检查x的形状
print(x.shape)

#numel() 计算张量元素的多少
print(x.numel())

# reshape 重塑指定可行形状
matrix = x.reshape(3, 4)
print(matrix)
print(matrix.shape)