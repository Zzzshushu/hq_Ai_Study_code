"""
height=float(input("请输入身高："))
weight=float(input("请输入体重："))

BMI=weight/(height**2)
if BMI<18.5:
	print("过轻")
elif 18.5<=BMI<24:
	print("正常")
elif 24<=BMI<28:
	print("过重")
elif 28<=BMI:
	print("肥胖")
print(BMI)
"""

a=int(input("请输入a："))
b=int(input("请输入b："))
c=int(input("请输入c："))

delta=b**2-4*a*c
if delta>0:
    x1=(-b+delta)/(2*a)
    x2=(-b-delta)/(2*a)
    print(x1,x2)
elif delta==0:
    x=-b/(2*a)
    print(x)
elif delta<0:
    print("无实数根")