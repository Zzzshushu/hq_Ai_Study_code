
"""

    基本概念
    原始数组的形状： 假设你有若干个数组，它们的形状都相同，比如都为 (m, n)。
    np.stack 的作用： 当你调用 np.stack([a, b, ...], axis=k) 时，NumPy 会在结果数组的第 k 个位置插入一个新维度，
    这个新维度的大小正好等于你堆叠的数组个数。
    结果： 如果你有 N 个 (m, n) 的数组，使用 np.stack 后得到的数组形状将会是：
    当 axis=0 时： (N, m, n)
    当 axis=1 时： (m, N, n)
    当 axis=2 时： (m, n, N)
    也就是说，axis 参数控制新插入维度的位置，其他维度的顺序保持不变。
"""
import numpy as np
# 创建三个一维数组
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(f'数组a的形状为{a.shape}, 数组a为：\n', a)
print(f'数组b的形状为{b.shape}, 数组b为：\n', b)
# 沿着新的轴堆叠数组
d = np.stack((a, b), axis=0)
print(f'数组d的形状为{d.shape}, 数组d为：\n', d)
# 沿着第二个轴堆叠数组
e = np.stack((a, b), axis=1)
print(f'数组e的形状为{e.shape}, 数组e为：\n', e)

# c=np.concatenate((a, b), axis=1)
# print(c)