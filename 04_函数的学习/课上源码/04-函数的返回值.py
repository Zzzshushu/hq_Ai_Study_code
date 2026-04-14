
# 函数的返回值
def sub(x, y):
    z = x - y
    return z


# ret = sub(1, 1)
# print(ret)

def div(x, y):
    if y == 0:
        return '除数不能为0'
    else:
        return x / y

# ret = div(1, 0)
# print(ret)


def calculate(x, y):
    z1 = x + y
    z2 = x - y
    z3 = x * y
    z4 = x / y
    return z1, z2, z3, z4

z1, z2, z3, z4 = calculate(3, 4)
print(z1, z2, z3, z4)

a, b = 1, 2
print('a和b的值为：', a, b)




