import numpy as np

#astype方法，更改数组的数据类型
# arr1=np.array([1.1,2.2,3.3])
# new_arr=arr1.astype(int)
# print(new_arr)

#reshape方法，更改数组形状，返回新数组
# arr2=np.array(([1,2,3],[4,5,6]))
# print(arr2)
# #new_arr=arr2.reshape(3,2)
#  print(new_arr)
#

#resize方法，更改数组形状，改变原数组，返回None
# import numpy as np
# a = np.array([[1, 2, 3], [4, 5, 6]])
#
# a.resize((3, 2))
# print(a,end="\n\n")
# a.resize((2, 2))
# print(a,end="\n\n")
# a.resize((5, 5))
# print(a)

#flatten方法返回一个一维数组，它是原始数组的拷贝，它默认按行顺序展平数组，但可以通过参数order来指定展平顺序。

arr=np.array([[1,2,3],[4,5,6],[7,8,9]])
b=arr.flatten()
print(arr)
print(b)

#ravel方法返回一个连续的数组，它尝试以最低的复制操作来返回展平后的数组
arr=np.array([[1,2,3],[4,5,6],[7,8,9]])
b=arr.ravel()
print(arr)
print(b)

#T转置
arr=np.array([[1,2,3],[4,5,6],[7,8,9]])
b=arr.T
print(b)