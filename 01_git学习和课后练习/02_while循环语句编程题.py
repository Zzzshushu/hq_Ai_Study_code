"""
i=0
while i **2<=12000:
	i+=1
print(i,i**2)

"""

"""
n = int(input("请输入一个数字："))
print("Collatz序列为：",end="")
step = 0
list1=[]
while n != 1:
    if n % 2 == 0:
        n = n / 2
    elif n % 2 != 0:
        n = n * 3 + 1
    step += 1
    list1.append(n)
print(list1)
print(f"步数为{step}")
"""
n_str = input("请输入一个正整数 n: ")
n = int(n_str)

if n <= 0:
    print("请输入一个正整数。")
else:
    current_num = n
    count = 0 # 步数计数器
    print("Collatz 序列:")
    print(current_num, end="") # 打印第一个数

    while current_num != 1:
        if current_num % 2 == 0: # 偶数
            current_num = current_num // 2 # 使用整数除法
        else: # 奇数
            current_num = 3 * current_num + 1
        print(f" -> {current_num}", end="")
        count += 1

    print(f"\n序列长度 (步数): {count}")