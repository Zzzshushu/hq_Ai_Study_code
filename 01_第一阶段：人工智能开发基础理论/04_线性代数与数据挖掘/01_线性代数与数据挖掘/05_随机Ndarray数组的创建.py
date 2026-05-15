import numpy as np

# #设置随机数种子
# np.random.seed(10)
# #random.rand
# arr1=np.random.rand(5)
# print(arr1)
# arr2=np.random.rand(3,3)
# print(arr2)
# arr2=np.random.rand()
# print(arr2)

# #random.random
# arr3=np.random.random((3,3))
# print(arr3)
#
# #random.randn
# arr1=np.random.randn(2,3)
# print(arr1)

# #random.normal
# print(np.random.normal())
# print(np.random.normal(size=3))
# print(np.random.normal(loc=5,scale=2,size=4))
# print(np.random.normal(loc=10,scale=1,size=(3,3)))

# # random.randint
# print(np.random.randint(10))
# print(np.random.randint(1,10,size=(3,3)))

# # random.uniform
# import numpy as np`
# # # 设置随机数种子
# # np.random.seed(10)
# # 在 [0, 1) 范围内抽取一个浮点数
# print(np.random.uniform())
# # 在 [5, 10) 范围内抽取一个浮点数
# print(np.random.uniform(5, 10))
# # 在 [0, 1) 范围内抽取一个 3x3 的浮点数数组
# print(np.random.uniform(size=(3, 3)))
# # 在 [5, 10) 范围内抽取一个 2x3 的浮点数数组
# print(np.random.uniform(5, 10, size=(2, 3)))

#random.shuffle
# # 设置随机数种子
# np.random.seed(10)
# 创建一个numpy数组
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# 打乱数组
np.random.shuffle(arr)
print(arr)
