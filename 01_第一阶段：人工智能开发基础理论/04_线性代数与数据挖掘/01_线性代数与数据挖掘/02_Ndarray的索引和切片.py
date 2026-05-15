import numpy as np

arr1=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr1)
print(arr1[0])#[1,2,3]
print(arr1[0,1])
print(arr1[0][1])



row1=arr1[1:3]#只切行
print(row1)

col1=arr1[1:3,1:3]#切行也切列
print(col1)