# 43.	基于 NumPy 完成以下操作：
# (1) 创建一个形状为 (3,4) 的二维数组，元素为 1-12 的连续整数；
# (2) 将该数组转置，修改形状为 (2,6)；
# (3) 计算数组每列的平均值（保留维度）。要求：写出完整 Python 代码，标注关键步骤注释

import numpy as np

arr=np.arange(1,13).reshape(3,4)#arange创建1到12的连续整数，reshape更改形状为(2,3)
print(arr)

arr_t=arr.T.reshape(2,6)#T方法用于转置，reshape将形状更改为(2,6)
print(arr_t)

arr_mean=arr.mean(axis=0,keepdims=True)#mean计算平均值，axis=0，按列计算，keepdims=True代表维度保持不变
print(arr_mean)

print("======================================")
# 44.	某班级的学生成绩数据如下：
#
# 学生姓名：张三、李四、王五、赵六
# 语文成绩：85、92、78、88
# 数学成绩：90、88、95、82
# 英语成绩：78、85、88、90
# 请完成以下任务：
# a. 创建包含这些数据的DataFrame，并为行设置自定义索引。
# b. 创建完成后，使用适当的属性查看DataFrame的行索引、列名、数据形状以及每列的数据类型。
# c. 使用head和tail方法查看前2行和后3行的数据。
# d. 使用loc和iloc两种方法分别获取"王五"的数学成绩。

import numpy as np
import pandas as pd

data={
    '学生姓名':['张三','李四','王五','赵六'],
    '语文成绩':[85,92,78,88],
    '数学成绩':[90,88,95,82],
    '英语成绩':[78,85,88,90]
}
df=pd.DataFrame(data,index=["stu1",'stu2','stu3','stu4'])

print(df,end='\n\n')
print(df.index,end='\n\n')
print(df.columns,end='\n\n')
print(df.shape,end='\n\n')
print(df.dtypes,end='\n\n')

df_head=df.head(2)
print(df_head)

df_tail=df.tail(3)
print(df_tail,end='\n\n')

grade_loc=df.loc['stu3','数学成绩']
print(grade_loc)

grade_iloc=df.iloc[2,2]
print(grade_iloc)