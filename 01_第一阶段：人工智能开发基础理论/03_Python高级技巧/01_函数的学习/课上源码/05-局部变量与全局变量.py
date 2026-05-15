# 局部变量：定义在函数内部的变量和参数
def test():
    x = 1
    print(x)
    return

# 变量x是在函数内部定义的，是局部变量
# 仅仅在函数生效的时候存在，当函数执行完毕后，就无法访问到该变量了
# test()

# 全局变量：定义在函数的外面的变量或者在函数内部使用global关键字修饰的变量
# 在函数内部是可以访问到全局变量的，但是函数外部是不可以访问到函数内部的变量的
# 当函数内部存在变量与函数外部的变量名字相同时，局部变量会覆盖掉全局变量
# global非必要不使用，因为global能够在函数的内部修改全局变量的值
# 使用很多的global会导致全局变量非常危险
y = 1
def test1():
    # global:用来将局部变量升级为全局变量
    global y
    print('函数内部修改值之前的id：', id(y))
    y = 10
    print('函数内部修改值之后的id：', id(y))

# print('函数外部修改值之前的id：', id(y))
# test1()
# print('函数外部修改值之后的id：', id(y))


# 关于列表的len函数的实现
def len_list(my_list):
    # 用来记录元素的个数
    count = 0
    for i in my_list:
        count += 1
    return count

my_list = [1, 2, 3, 'asdasd', [1, 2, 3]]
# ret = len_list(my_list)
# print(ret)


# 函数的名字或者变量的名字一定不要跟BIF的名字相同
# 否则就调用不到BIF
# 关于列表的sum函数
def sum(my_list):
    # 定义一个变量，用来存储求和的结果
    # result = 0
    # for i in my_list:
    #     result += i
    return 1

# my_list_num = [x for x in range(101)]
# ret = sum(my_list_num)
# print(ret)





# 嵌套函数
# 内部函数除了在外部函数中调用之外，是无法访问到的。
# def outer_func():
#     def inner_func():
#         print('这是内部函数')
#     inner_func()
#     print('这是外部函数')
#     return
#
# outer_func()


# 嵌套函数的作用域：内部函数的局部变量是可以覆盖外部函数的局部变量的
# 在内函数中：内函数的局部变量 > 外函数的局部变量 > 全局变量
x = 10
# def outer_func():
#     x = 1
#     def inner_func():
#         # 使用nonlocal关键字，可以在内函数中修改外函数的变量值
#         # global 和 nonlocal的区别：
#         # global修改的是局部变量 nonlocal修改的是上一层嵌套函数的变量
#         # global和nonlocal不能对同一个变量生效
#         nonlocal x
#         x = 2
#         print('在内函数中x的值：', x)
#     inner_func()
#     print('在外函数中x的值：', x)
#     return

# outer_func()
# print(x)



# 以内函数作为返回值进行返回，不需要带圆括号
# def outer_func():
#     def inner_func():
#         print("这是一个内函数")
#     inner_func()
#     print("这是一个外函数")
#     return inner_func
# ret = outer_func()
# ret()


# 嵌套函数的特性：当内部函数访问外部函数的某个变量时
# 改变量不会随着外部函数的调用完毕而销毁，而是被内部函数所保留
# def outer_func():
#     x = 1
#     def inner_func():
#         print(x)
#     return inner_func
#
# ret = outer_func()
# ret()


# pow函数
# def pow(x, y):
#     return x ** y
#
# pow(1, 3)

def outer_func(exp):
    def inner_func(base):
        return base ** exp
    return inner_func

ret = outer_func(2)
result = ret(3)
print(result)
res = ret(4)
print(res)
ret1 = outer_func(3)
res1 = ret1(3)
print(res1)