import numpy as np

arr=np.array([1,2,3,4,5,6])

a=np.split(arr,3)
print(a)

b=np.split(arr,[3])
print(b)

