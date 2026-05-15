income=int(input("请输入月收入："))
if income<=5000:
    print(f"月收入为{income}")
elif 5000<income<=8000:
    income=5000+(income-5000)*0.97
    print(f"月收入为{income}")
elif 8000<income<=17000:
    income=5000+3000*0.97+(income-8000)*0.9
    print(f"月收入为{income}")
elif 17000<income<=30000:
    income=5000+3000*0.97+9000*0.9+(income-17000)*0.8
    print(f"月收入为{income}")
else:
    income=5000+3000*0.97+9000*0.9+13000*0.8+(income-30000)*0.75
    print(f"月收入为{income}")
