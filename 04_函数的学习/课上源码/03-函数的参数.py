# 带有参数的函数的定义
# 参数在子代码块里如果出现某数据类型所拥有的独特标志之后
# 那么传入其他类型的数据之后，就会报错
def myfunc(x, y):
    x += 1
    print(x)
    print(y)

# 带有参数的函数的调用
# 函数的实参除了可以直接使用数据之外
# 也可以传入变量且传入变量的使用会更多
a = 1
b = 2
# myfunc(b, a)


# 位置参数：参数传递时实参的顺序和个数必须和形参保持一致
def sub(x, y):
    print(x - y)

# sub(2, 1)


# 关键字参数：使用 形参名字=实参 的方式传递，不用考虑形参的位置
# 关键字参数使用的场景很多
# sub(y = 2, x = 1)
# Python解释器规定位置参数必须在关键字参数之前传参
# 也就是说，当调用函数时，第一个传入的参数是关键字传参时，那么后面的参数就不能使用位置传参了
# sub(y=2, 1)
# help(sum)
ls = [1, 2, 3]
# print('使用关键字传参：', sum(ls, start=1))
# print("使用位置参数传参：", sum(ls, 1))
# help(dict.fromkeys)

# 默认参数
# 默认在定义时，必须放在形参的最右边
def add(x, y = 2, z = 1):
    print('x的值为：', x)
    print('y的值为：', y)
    print('z的值为：', z)

# 默认参数在调用函数时如果不需要修改默认参数的值就可以不传递
# 如果需要修改默认参数的值，可以传递实参来覆盖掉默认参数的默认值
# add(1, y=3, z = 5)




# 位置不定长参数： 在函数定义时，使用*args来表示
def myfunc1(*args):
    for i in args:
        print(i)
    print(len(args))
    print(type(args))
    print(args)

# myfunc1(1, 2, 3, 'asd')


# 向输入的人名打招呼
def say(*args):
    for i in args:
        print(f'hello {i}')

# say('zhangsan', 'lisi', 'wangwu')


# 得到传入参数中的最大值
# 不定长位置参数在定义时，如果右边还有其他的参数，必须要使用关键字参数传参
def max_args(*args):
    max_num = args[0]
    # 循环遍历args里的值
    for i in args:
        # 如果i的值比max_num值大，说明max_num不是最大的值，i是较大的值，将i的值赋值给max_num
        if i > max_num:
            max_num = i
        # 如果i的值比max_nun值小，说明max_num就是较大的值，就不用再将i的值赋值给max_num
    print(max_num)
# max_args(1, 2, 3, 4, 5)

# 为什么要打包成元组而不是别的数据类型
# 是因为元组有一个特性叫做：打包和解包
# 打包就是将多个值打包为一个元组

# 打包的用法
def test():
    return 1, 2, 3, 4
# ret = test()

# 解包：将一个元组的元素拆开分别赋值给对应的变量
# x, y, z, m = test()

def test1(*args, x, y):
    print(args)
    print(x)
    print(y)

# test1(1, 2, 3, x = 4, y = 5)



# 关键字不定长参数：以**kwargs 作为标志，**是必须的， kwargs是程序员约定成俗的
# 它会将输入的关键字参数中的关键字当作键值对的键，将关键字参数中的实参当作键值对的值
# 放到字典里进行存储
def func(**kwargs):
    print(kwargs)
    print(type(kwargs))

# func(name = 'zhangsan', age = 18)


# 对传入的关键字参数的值进行相乘
def mul(**kwargs):
    result = 1
    # 使用kwargs.keys()获取字典中所有的键
    # 通过for循环取遍历这些键，从而获取对应的值并令该值参与运算
    for key in kwargs.keys():
        result = kwargs[key] * result
    print(result)

# mul(a = 1, b = 2, c = 3)



# *args与**kwargs出现在同一个函数中
# kwargs里的关键字参数不能与其他的参数同名
def test2(x, *args, **kwargs):
    print(x)
    print(args)
    print(kwargs)

# test2(1, 2, 3, z = 4, y = 5)


# 元组的解包功能的用法，使用*元组名就可以做到一次性传递多个参数
def test3(x, y, m, n):
    print(x, y, m, n)

args = (1, 2, 3, 4)
# test3(*args)

kwargs = {'x': 1, 'y': 2, 'm': 3, 'n': 4}

# 需要注意：键值对的键必须要和函数的形参名称相同，才能直接传递参数
test3(**kwargs)





