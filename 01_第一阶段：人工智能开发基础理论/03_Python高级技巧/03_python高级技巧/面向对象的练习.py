"""
四、编程题：
1.定义一个类,类的名称为Dog,为该类创建一个对象dog


2.定义一个类,类的名称为Dog.类里创建一个成员方法，方法的名称为run,方法返回信息“小狗正在奔跑”。

4.定义一个汽车类Car
(1)在构造方法中添加颜色color、型号type等属性
(2)类中定义一个move方法，方法输出“这辆车的颜色为XX,型号为XX”
(3)分别创建bmw、audi对象.bmw的颜色为red,型号为x1;audi的颜色为blue,型号为a4
(4)分别调用move方法

"""

#定义Dog类
# class Dog:
#     def say():
#         print("Hello")
# dog = Dog()
# dog.say()
#
#
# class Dog:
#     def run(self):
#         c="小狗正在奔跑"
#         return c
# dog=Dog()
# dog.run()
# print(dog.run())
class Car:
    def __init__(self,color,type):
        self.color=color
        self.type=type
    def move(self):
        print(f"这辆车的颜色为：{self.color}，型号为：{self.type}")
bmw=Car("red","x1")
audi=Car("blue","a4")
bmw.move()
audi.move()