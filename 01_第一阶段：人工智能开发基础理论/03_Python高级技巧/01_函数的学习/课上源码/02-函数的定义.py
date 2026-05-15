# 函数的定义


# 函数只有在调用的时候才会被执行
# 函数在定义时候，Python解释器只会检查语法，而不会主动执行函数
def myfunc():
    '''
    这是一个测试函数，会打印4遍人生苦短，我学Python！！！
    :return: None
    '''
    for i in range(4):
        print("人生苦短，我学Python！！！")


# 关于自定义函数的函数文档
help(myfunc)


# 函数的调用：函数名字+()
# myfunc()
# print(123)


# pass：就是在函数刚开始定义且没有写功能时，作为占位符
# 防止解释器报错
def myfunc1():
    print('123')

def myfunc2():
    pass


def myfunc3():
    pass

# myfunc1()


