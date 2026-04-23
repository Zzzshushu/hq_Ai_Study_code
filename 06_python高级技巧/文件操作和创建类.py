"""
1. 使用函数和文件操作完成一个学生成绩记录程序。
要求：
（1）定义一个函数 save_score(name, score)
（2）函数接收学生姓名和成绩两个参数
（3）将数据以 姓名,成绩 的格式写入 scores.txt 文件
（4）每次写入一条记录后换行
（5）程序中至少调用该函数 3 次，保存 3 名学生成绩
2. 使用类实现一个简单的学生信息管理程序。
要求：
（1）定义一个 Student 类
（2）在构造方法中接收姓名和年龄两个属性
（3）定义一个 show_info() 方法，打印学生信息
（4）创建 2 个 Student 对象并分别调用 show_info()
（5）输出格式清晰，能够区分类和对象的作用

"""
class Student:
   def __init__(self,name,score):
      self.name=name
      self.score=score
   def show_info(self):
      print('name:',self.name,end=' ')
      print('score:',self.score)


student_1=Student('李四','60')
student_1.show_info()
student_2=Student('张三','59')
student_2.show_info()












def save_score(name, score):
   with open('scores.txt', 'a', encoding='utf-8') as f:
      f.write(name + ',' + str(score) + '\n')

save_score('张三','100')
save_score('李四','60')
save_score('王五','59')