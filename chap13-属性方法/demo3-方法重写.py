# @Time : 2022/8/6 6:33
# @Author : YKW
# @File : demo3-方法重写.py
# 开始奇妙的python之旅吧！！！
"""
# 如果对继承的某个属性或方法不满意，
可以在子类中对方法体重新编写
# 子类重写后的方法体内可以通过
super().xxx()调用父辈这一方法体
"""


class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print('姓名：{0}，年龄：{1}'.format(self.name, self.age), end='\t')


# 定义子类
class Student(Person):
    def __init__(self, name, age, num):
        super().__init__(name, age)  # 调用父辈的属性
        self.num = num

    def info(self):
        super().info()
        print('学号：{0}'.format(self.num))


# 测试
stu = Student('Jack', 20, '1001')
stu.info()
Student.info(stu)
