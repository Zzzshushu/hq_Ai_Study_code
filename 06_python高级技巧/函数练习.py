"""
四、编程题
1.定义一个函数，它有一个名为x的参数,如果x是非负数则返回True,否则返回False


2.程序设计题，输入三角形的底和高，使用函数方式计算任意三角形的面积。（注：默认输入的数值能够构成三角形）。
提示：三角形面积公式：已知三角形底为a，高为h，则S=ah/2。



"""
# def judgment(self,x):
#     if x<0:
#         return False
#     else:
#         return True
#
# print(judgment(1))
# print(judgment(-2))

s=0
def S(a,h):
    s=a*h/2
    return s
print(S(2,2))

