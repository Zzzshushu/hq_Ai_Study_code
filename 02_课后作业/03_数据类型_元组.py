"""items = [("apple", 2.5), ("banana", 1.8), ("orange", 3.0), ("grape", 2.8)]

# 方法1：将价格放在元组前面，然后排序，再还原
# 1. 重组元组：(价格, 商品)
temp = [(price, name) for name, price in items]
# 2. 排序（元组默认按第一个元素比较）
temp.sort()
# 3. 还原为原始格式
sorted_items = [(name, price) for price, name in temp]

print("按价格排序:", sorted_items)
# 输出: [('banana', 1.8), ('apple', 2.5), ('grape', 2.8), ('orange', 3.0)]

"""

data=[1,2,3,4,5,6,7,8,9,]
group_size=3
size=len(data)//group_size
i=0
list2=[]
while i<size:
    list1=[tuple(data[i*group_size:(i+1)*group_size])]
    i+=1
    list2+=list1
print(list2)