# 匿名函数的使用
# 1. 计算两个数的和

# 普通函数：
# def add(x, y):
#     return x + y

# ret = add(1, 2)
# print(ret)


# lambda表达式：  lambda 参数列表 ：表达式
# res = lambda x, y : x + y
# print(res(1, 2))


# 2. 判断一个数是不是偶数
# ret = lambda x : x % 2 == 0
# num = int(input("请输入要判断的数："))
# print(ret(num))


# 3.使用lambda表达式配合map函数完成对列表中的所有元素加10
# result = map(lambda x : x + 10, [x for x in range(10)])
# print(list(result))



# 匿名函数的参数也可以使用默认参数
add = lambda x, y = 1: x + y
print(add(1))

