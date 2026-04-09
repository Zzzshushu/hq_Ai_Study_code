"""
str1=input("请输入文本：")
str2=input("请输入目标字符：")

str1=str1.lower()
str2=str2.lower()

a=str1.count(str2)
print(a)
"""

str1=input("请输入字符串：")

str1=str1.lower()
list1=str1.split()
str1="".join(list1)
str2=str1[::-1]
if(str1==str2):
    print("是回文字符串")
else:
    print("不是回文字符串")



