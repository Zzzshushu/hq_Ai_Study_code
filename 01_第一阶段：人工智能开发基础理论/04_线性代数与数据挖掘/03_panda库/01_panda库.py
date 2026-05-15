# import pandas as pd
# data = {
#  '姓名': ['小明', '小红', '小刚'],
#  '年龄': [20, 18, 22],
#  '成绩': [85, 90, 88]
# }
# df = pd.DataFrame(data, index=['a', 'b', 'c'])
# print(df)
# print(df.index)
# print(df.columns)
# import pandas as pd
# data = {
#     '姓名': ['小明', '小红', '小刚'],
#     '年龄': [20, 18, 22],
#     '成绩': [85, 90, 88]
# }
# df = pd.DataFrame(data)
# print(df)
# print()
# print(df['姓名'])
# print(df[['姓名', '年龄','成绩']])
#

import pandas as pd
import numpy as np
# 创建一个包含缺失值的 DataFrame
df = pd.DataFrame({
    'A': [1, 2, np.nan],
    'B': [4, np.nan, 6],
    'C': [7, 8, 9]
})
# 打印原始DataFrame
print(df)
# 使用 isnull() 方法检测缺失值
missing_values = df.isnull()
print(missing_values)

print("====================================")

import pandas as pd
import numpy as np
# 创建一个包含缺失值的 DataFrame
df = pd.DataFrame({
    'A': [1, 2, np.nan],
    'B': [4, np.nan, 6],
    'C': [7, 8, 9]
})
# 打印原始DataFrame
print(df)
# 删除任何含有 NaN 值的行
df_cleaned = df.dropna(axis=0,)
print(df_cleaned)
print("====================================")
import pandas as pd
import numpy as np
# 创建一个包含缺失值的 DataFrame
df = pd.DataFrame({
    'A': [1, 2, np.nan],
    'B': [np.nan, np.nan, 6],
    'C': [7, np.nan, 9]
})
'''
    标量填充
'''
# 打印原始DataFrame
print(df)
# 使用固定值填充缺失值
df_filled_value = df.fillna(value=0)
print(df_filled_value)


'''
    前向填充
'''
df_filled_value = df.fillna(method='ffill')
print(df_filled_value)

'''
    后向填充
'''
df_filled_value = df.fillna(method='bfill')
print(df_filled_value)

"""
    指定列标签填充
"""
data = {
    'A': 'a',
    'B': 'b',
    'C': 'c'
}
df_filled_value = df.fillna(value=data)
print(df_filled_value)

"""
    使用 limit 参数
"""

filled_with_limit = df.fillna(value=0, limit=1)
print(filled_with_limit)

print("====================================")

import pandas as pd
# 创建一个包含重复行的 DataFrame
df = pd.DataFrame({
    'A': [1, 2, 1, 2, 3, 3],
    'B': [1, 1, 2, 2, 3, 3],
    'C': [1, 1, 2, 2, 3, 3]
})
# 打印原始DataFrame
print(df)
# 删除重复行，保留第一次出现的重复项
df_dedup_first = df.drop_duplicates()
print(df_dedup_first)
# 根据指定列删除重复行
df_dedup_column = df.drop_duplicates(subset=['A'])
print(df_dedup_column)

print("====================================")

import pandas as pd
# 创建一个 DataFrame
df = pd.DataFrame({
    'A': [1, 2, 3, 4, 5],
    'B': ['a', 'b', 'a', 'b', 'a']
})
# 打印原始DataFrame
print(df,end="\n\n")
'''
    单一值替换
'''
# 用数字 100 替换所有的 1
df_replaced = df.replace(to_replace=1, value=100)
print('单一值替换\n',df_replaced)
'''
    列表替换所有匹配值
'''
df_replaced = df.replace(to_replace=[2,3,'a'], value='z')
print('列表替换所有匹配值\n',df_replaced)
'''
    字典替换所有匹配值
'''
df_replaced = ({
     2: 200,
    'b': 'y'
})
df_replaced = df.replace(to_replace=df_replaced)
print('字典替换所有匹配值\n',df_replaced)

# 使用正则表达式替换
import pandas as pd

df = pd.DataFrame({
    'col1': ['apple', 'banana', 'cherry', 'agerape', 'apricote'],
    'col2': ['apple pie', 'banana split', 'cherry tart', 'grape juice', 'apricote jam']
})
"""
    ^：匹配字符串的开始。
    a：匹配字符 "a"。
    .*：匹配任意数量的字符（包括零个字符）。
    e：匹配字符 "e"。
    $：匹配字符串的结束。
"""
df_replaced = df.replace(to_replace=r'^a.*e$', value='fruit', regex=True)
print(df_replaced)

print("====================================")
import pandas as pd
# 创建一个示例 DataFrame
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4.5, 5.5, 6.5],
    'C': ['7', '8', '9']
})
# 打印原始DataFrame
print(df)
# 将列 'A' 转换为浮点数类型
c = df['A'].astype(float)
d=df.astype({'A':float})
print(c)
# 使用字典将多列转换为不同的数据类型
# 将列 'B' 转换为整数类型，列 'C' 也转换为整数类型
c = df.astype({
    'B': int,
    'C': int
})

# 打印DataFrame中各列的数据类型
print(c)

c = df.astype('float64')
print(c)
print("====================================")

import numpy as np
import pandas as pd
# 创建一个示例 DataFrame
df = pd.DataFrame({
    'col1': ['A', 'A', 'B', np.nan, 'D', 'C'],
    'col2': [2, 1, 9, 8, 7, 4],
    'col3': [0, 1, 9, 4, 2, 3],
    'col4': ['a', 'B', 'c', 'D', 'e', 'F']
})
# 打印原始DataFrame
print(df,end="\n\n")
# 根据 'col1' 列对DataFrame进行排序
res1 = df.sort_values(by=['col1'])
# 打印排序后的DataFrame
print(res1,end="\n\n")
# 根据 'col1' 和 'col2' 列对DataFrame进行排序
res2 = df.sort_values(by=['col1', 'col2'])
# 打印排序后的DataFrame
print(res2)

print("====================================")
import pandas as pd
import numpy as np
# 创建一个多级索引的DataFrame
arrays = [np.array(['qux', 'qux', 'foo', 'foo']),
          np.array(['two', 'one', 'two', 'one'])]
df = pd.DataFrame({'A': [1, 2, 3, 4], 'B': [4, 3, 2, 1]},index=arrays)
print(df)
# 按第一层索引升序排序
df_sorted_by_first_level = df.sort_index(level=0)
print(df_sorted_by_first_level)
# 按第二层索引降序排序
df_sorted_by_second_level_desc = df.sort_index(level=1,ascending=False)
print(df_sorted_by_second_level_desc)
# 按整个索引升序排序
df_sorted_by_full_index = df.sort_index(ascending=True)
print(df_sorted_by_full_index)
print("====================================")

import pandas as pd
data = {
    '姓名': ['小明', '小红', '小刚'],
    '年龄': [20, 18, 22],
    '成绩': [85, 90, 88]
}
df = pd.DataFrame(data)
print(df,end="\n\n")
print(df['成绩'] >= 90)
# 使用布尔索引选择成绩大于或等于90的学生
high_scores = df[df['成绩'] >= 90]
print(high_scores)

print("====================================")

import pandas as pd
# 创建两个 DataFrame
df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                    'B': ['B0', 'B1', 'B2', 'B3'],
                    'C': ['C0', 'C1', 'C2', 'C3'],
                    'D': ['D0', 'D1', 'D2', 'D3']},
                   index=[0, 1, 2, 3])
df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                    'B': ['B4', 'B5', 'B6', 'B7'],
                    'C': ['C4', 'C5', 'C6', 'C7'],
                    'F': ['F4', 'F5', 'F6', 'F7']},
                   index=[4, 5, 6, 7])
# 沿着竖直方向拼接两个DataFrame
result = pd.concat([df1, df2], axis=1)
print(result)

print("====================================")

import pandas as pd
import numpy as np
# 创建一个包含 NaN 值的 DataFrame
df = pd.DataFrame(
    {'A': [1, 2, np.nan, 4],
    'B': [5, np.nan, np.nan, 8],
    'C': ['foo', 'bar', 'baz', np.nan]
})
# 计算每列非 NaN 值的数量
count_per_column = df.count()
print("Count per column:")
print(count_per_column)
# 计算每行非 NaN 值的数量
count_per_row = df.count(axis=1)
print("\nCount per row:")
print(count_per_row)
# 只计算数值列的非 NaN 值的数量
count_numeric_only = df.count(numeric_only=True)
print("\nCount numeric only:")
print(count_numeric_only)

print("====================================")

import pandas as pd
import numpy as np
# 创建一个包含 NaN 值的 DataFrame
df = pd.DataFrame({
'A': [1, 2, np.nan, 4],
'B': [5, np.nan, np.nan, 8],
'C': [12, np.nan,np.nan, np.nan]
})
# 计算每列的总和
print(df)
sum_per_column = df.sum()
print("Sum per column:")
print(sum_per_column)
# 计算每行的总和
sum_per_row = df.sum(axis='columns')
print("\nSum per row:")
print(sum_per_row)
# 只计算数值列的总和
sum_numeric_only = df.sum(numeric_only=True)
print("\nSum numeric only:")
print(sum_numeric_only)
# 使用 min_count 参数
sum_with_min_count = df.sum(min_count=2)
print("\nSum with min_count=2:")
print(sum_with_min_count)

print("====================================")

import pandas as pd
import numpy as np
# 创建一个包含 NaN 值的 DataFrame
df = pd.DataFrame({
'A': [1, 2, np.nan, 4],
'B': [5, np.nan, np.nan, 8],
# 'C': ['foo', 'bar', 'baz', 'qux'] # 非数值列
})
# 计算每列的平均值
mean_per_column = df.mean()
print("Mean per column:")
print(mean_per_column)
# 计算每行的平均值
mean_per_row = df.mean(axis='columns')
print("\nMean per row:")

print(mean_per_row)
# 只计算数值列的平均值
mean_numeric_only = df.mean(numeric_only=True)
print("\nMean numeric only:")
print(mean_numeric_only)

print("====================================")
import pandas as pd
# 创建一个简单的DataFrame
data = {
    '姓名': ['张三', '李四', '王五'],
    '年龄': [28, 34, 29],
    '城市': ['北京', '上海', '广州']
}
df = pd.DataFrame(data)
# 将DataFrame保存为CSV文件
df.to_csv('人员信息.csv', index=False, encoding='utf_8_sig')

print("====================================")
import pandas as pd
# 创建一个简单的DataFrame
data = {
    '姓名': ['张三', '李四', '王五'],
    '年龄': [28, 34, 29],
    '城市': ['北京', '上海', '广州']
}
df = pd.DataFrame(data)
# 将DataFrame保存为Excel文件
df.to_excel('人员信息.xlsx', index=False)

print("====================================")
import pandas as pd

data = pd.read_csv('人员信息.csv', nrows=1)
print(data)
print("====================================")
"""
22.	某公司销售数据如下：
日期       产品   销售额   地区
2023-01-01  A     1200    华北
2023-01-01  B     800     华东
2023-01-02  A     1500    华北
2023-01-02  B     NaN     华东
2023-01-03  A     1100    华北
2023-01-03  B     950     华东
2023-01-04  A     NaN     华北
2023-01-04  B     1300    华东
请完成以下任务：
a. 创建包含上述数据的DataFrame。
b. 使用适当的方法检测数据中的缺失值，并统计每列缺失值的数量。
c. 对缺失的销售额数据进行处理：使用每种产品的平均销售额填充缺失值
d. 删除所有包含缺失值的行，观察删除后的结果。
e. 将数据按照日期升序、销售额降序进行排序。
f. 筛选出销售额大于1000且地区为"华北"的所有记录。
g. 假设有另一份2023-01-05的数据，请演示如何使用concat()方法将其拼接到原DataFrame中。
"""
import pandas as pd
import numpy as np

# a. 创建包含上述数据的DataFrame
data = {
    '日期': ['2023-01-01', '2023-01-01', '2023-01-02', '2023-01-02',
            '2023-01-03', '2023-01-03', '2023-01-04', '2023-01-04'],
    '产品': ['A', 'B', 'A', 'B', 'A', 'B', 'A', 'B'],
    '销售额': [1200, 800, 1500, np.nan, 1100, 950, np.nan, 1300],
    '地区': ['华北', '华东', '华北', '华东', '华北', '华东', '华北', '华东']
}

df = pd.DataFrame(data)
print("a. 原始DataFrame:")
print(df)
print("\n" + "="*50)

# b. 检测数据中的缺失值，并统计每列缺失值的数量
missing_values = df.isnull().sum()
print("b. 每列缺失值统计:")
print(missing_values)
print("\n" + "="*50)

# c. 对缺失的销售额数据进行处理：使用每种产品的平均销售额填充缺失值
# 先计算每种产品的平均销售额（忽略NaN）
product_means = df.groupby('产品')['销售额'].transform('mean')
df_filled = df.copy()
df_filled['销售额'] = df_filled['销售额'].fillna(product_means)

print("c. 使用产品平均销售额填充缺失值后的DataFrame:")
print(df_filled)
print("\n" + "="*50)

# d. 删除所有包含缺失值的行，观察删除后的结果
# 注意：这里我们使用原始的DataFrame进行删除操作，以展示删除效果
df_dropped = df.dropna()
print("d. 删除所有包含缺失值的行后的结果:")
print(df_dropped)
print(f"删除后剩余 {len(df_dropped)} 行数据")
print("\n" + "="*50)

# e. 将数据按照日期升序、销售额降序进行排序
# 使用填充后的DataFrame进行排序
df_sorted = df_filled.sort_values(by=['日期', '销售额'], ascending=[True, False])
print("e. 按照日期升序、销售额降序排序后的DataFrame:")
print(df_sorted)
print("\n" + "="*50)

# f. 筛选出销售额大于1000且地区为"华北"的所有记录
filtered_data = df_filled[(df_filled['销售额'] > 1000) & (df_filled['地区'] == '华北')]
print("f. 销售额大于1000且地区为'华北'的记录:")
print(filtered_data)
print("\n" + "="*50)

# g. 使用concat()方法拼接新数据
# 创建2023-01-05的新数据
new_data = {
    '日期': ['2023-01-05', '2023-01-05'],
    '产品': ['A', 'B'],
    '销售额': [1400, 900],
    '地区': ['华北', '华东']
}
df_new = pd.DataFrame(new_data)

# 使用concat拼接
df_concatenated = pd.concat([df_filled, df_new], ignore_index=True)
print("g. 拼接2023-01-05数据后的DataFrame:")
print(df_concatenated)
print("\n" + "="*50)

# 补充：显示每种产品的平均销售额
print("补充：每种产品的平均销售额")
print(df.groupby('产品')['销售额'].mean())

print("====================================")
"""
18.	某公司销售数据如下，已保存为'sales.csv'文件：
日期,产品,销售额,数量,地区
2023-01-01,A,1200,10,华北
2023-01-01,B,800,8,华东
2023-01-02,A,1500,12,华北
2023-01-02,B,,5,华东
2023-01-03,A,1100,9,华北
2023-01-03,B,950,10,华东
2023-01-04,A,,11,华北
2023-01-04,B,1300,13,华东
请完成以下任务：
a. 使用read_csv()读取该文件，要求只读取前6行，并将"日期"的数据转为日期类型。
b. 计算每列的非NaN值数量、每列的总和、平均值、中位数、最小值和最大值。
e. 将处理后的数据（包含原始数据和累积计算结果）保存为一个新的Excel文件'sales_analysis.xlsx'，要求包含两个工作表：'原始数据'和'分析结果'。

"""
# import pandas as pd
# import numpy as np
#
# # a. 使用read_csv()读取该文件，要求只读取前6行，并将"日期"的数据转为日期类型
# df = pd.read_csv('sales.csv', nrows=6, parse_dates=['日期'])
#
# print("a. 读取的前6行数据:")
# print(df)
# print(f"数据类型:\n{df.dtypes}")
# print("\n" + "=" * 60)
#
# # b. 计算每列的非NaN值数量、每列的总和、平均值、中位数、最小值和最大值
# # 注意：对于非数值列，某些统计量可能不适用
#
# # 首先，创建统计摘要
# statistics_summary = pd.DataFrame()
#
# # 遍历每列计算统计量
# for column in df.columns:
#     col_stats = {}
#
#     # 1. 非NaN值数量
#     col_stats['非NaN值数量'] = df[column].count()
#
#     # 2-6. 数值列的统计量
#     if pd.api.types.is_numeric_dtype(df[column]):
#         col_stats['总和'] = df[column].sum()
#         col_stats['平均值'] = df[column].mean()
#         col_stats['中位数'] = df[column].median()
#         col_stats['最小值'] = df[column].min()
#         col_stats['最大值'] = df[column].max()
#     elif pd.api.types.is_datetime64_any_dtype(df[column]):
#         # 对于日期列，计算最小和最大日期
#         col_stats['最小值'] = df[column].min()
#         col_stats['最大值'] = df[column].max()
#         col_stats['总和'] = 'N/A'
#         col_stats['平均值'] = 'N/A'
#         col_stats['中位数'] = 'N/A'
#     else:
#         # 对于非数值列（如产品、地区）
#         col_stats['总和'] = 'N/A'
#         col_stats['平均值'] = 'N/A'
#         col_stats['中位数'] = 'N/A'
#         col_stats['最小值'] = df[column].min() if len(df[column]) > 0 else 'N/A'
#         col_stats['最大值'] = df[column].max() if len(df[column]) > 0 else 'N/A'
#
#     # 将列统计添加到统计摘要
#     statistics_summary[column] = pd.Series(col_stats)
#
# print("b. 数据统计摘要:")
# print(statistics_summary)
# print("\n" + "=" * 60)
#
# # 补充：对缺失值进行处理（题目中提到的c、d任务类似，但这里题目只要求到e）
# # 我们将填充缺失值并计算累积销售额
# df_processed = df.copy()
#
# # 填充缺失的销售额（使用产品平均销售额）
# product_mean_sales = df_processed.groupby('产品')['销售额'].transform('mean')
# df_processed['销售额'] = df_processed['销售额'].fillna(product_mean_sales)
#
# # 填充缺失的数量（使用产品平均数量）
# product_mean_quantity = df_processed.groupby('产品')['数量'].transform('mean')
# df_processed['数量'] = df_processed['数量'].fillna(product_mean_quantity)
#
# # 计算累积销售额（按日期排序后）
# df_processed = df_processed.sort_values('日期')
# df_processed['累计销售额'] = df_processed['销售额'].cumsum()
# df_processed['累计数量'] = df_processed['数量'].cumsum()
#
# print("数据处理后（包含累计计算）：")
# print(df_processed)
# print("\n" + "=" * 60)
#
# # e. 将处理后的数据保存为Excel文件，包含两个工作表
# with pd.ExcelWriter('sales_analysis.xlsx', engine='openpyxl') as writer:
#     # 保存原始数据到'原始数据'工作表
#     df.to_excel(writer, sheet_name='原始数据', index=False)
#
#     # 保存分析结果到'分析结果'工作表
#     # 包括统计摘要和处理后的数据
#     analysis_data = pd.concat([df_processed, statistics_summary.T], keys=['处理后的数据', '统计摘要'])
#     df_processed.to_excel(writer, sheet_name='分析结果', index=False)
#
#     # 在分析结果工作表中添加统计摘要
#     # 我们需要写入到同一个工作表的不同位置
#     with writer.book as workbook:
#         worksheet = writer.sheets['分析结果']
#
#         # 在工作表中找到写入统计摘要的位置
#         start_row = len(df_processed) + 3
#
#         # 写入统计摘要标题
#         worksheet.cell(row=start_row, column=1, value='统计摘要')
#
#         # 写入统计摘要
#         statistics_summary.to_excel(writer, sheet_name='分析结果',
#                                     startrow=start_row + 1, startcol=0)
#
# print("e. 数据已保存到 'sales_analysis.xlsx'")
# print("工作表结构:")
# print("  - 原始数据: 包含读取的原始6行数据")
# print("  - 分析结果: 包含处理后的数据和统计摘要")
#
# # 验证文件保存
# try:
#     # 读取保存的Excel文件验证
#     with pd.ExcelFile('sales_analysis.xlsx') as xls:
#         print(f"\nExcel文件包含的工作表: {xls.sheet_names}")
#
#         # 显示原始数据工作表
#         df_original_saved = pd.read_excel(xls, sheet_name='原始数据')
#         print("\n原始数据工作表前3行:")
#         print(df_original_saved.head(3))
#
#         # 显示分析结果工作表
#         df_analysis_saved = pd.read_excel(xls, sheet_name='分析结果')
#         print("\n分析结果工作表前3行:")
#         print(df_analysis_saved.head(3))
#
# except Exception as e:
#     print(f"读取保存的文件时出错: {e}")
#
# # 补充：显示更多统计信息
# print("\n" + "=" * 60)
# print("补充统计信息:")
#
# # 按产品分组统计
# product_stats = df_processed.groupby('产品').agg({
#     '销售额': ['count', 'sum', 'mean', 'median', 'min', 'max'],
#     '数量': ['sum', 'mean']
# }).round(2)
#
# print("\n按产品统计:")
# print(product_stats)
#
# # 按地区分组统计
# region_stats = df_processed.groupby('地区').agg({
#     '销售额': ['sum', 'mean'],
#     '数量': ['sum', 'mean']
# }).round(2)
#
# print("\n按地区统计:")
# print(region_stats)