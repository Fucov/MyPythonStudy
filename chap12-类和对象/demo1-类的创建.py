# @Time : 2022/8/5 16:03
# @Author : YKW
# @File : demo1-类的创建.py
# 开始奇妙的python之旅吧！！！

# 创建
"""类的组成：类属性、实例方法、静态方法、类方法
第一、什么时候用实例方法？
需要改变实例属性的时候就用实例方法。
第二、什么时候用类方法？
需要改变类属性的时候用类方法
第三、什么时候用静态方法？
既不需要改变类属性，也不需要改变实例属性的时候用静态方法。"""


# Student是类的名称（）,由一个或多个单词组成，可以是驼峰命名，
class Student:
    native_place = '江苏'  # 直接写在类里的变量，称为类属性

    # 初始化方法，self.name叫做实例属性
    # 进行赋值的操作，将局部变量name赋值给实例属性
    def __init__(self, name, age):  # name,age为实例属性
        self.name = name
        self.age = age

    # 实例方法
    def info(self):  # self
        print('My name:', self.name, 'age:', self.age)

    # 类方法
    @classmethod
    def cm(cls):  # class,第一个参数必须是当前类对象，该参数名一般约定为“cls”
        print('我使用了classmethod进行修饰，类方法')

    # 静态方法
    @staticmethod
    def sm(self):  # 参数随意，没有“self”和“cls”参数，但是方法体中不能使用类或实例的任何属性和方法
        print('我使用了staticmethod进行修饰,静态方法')

    # 在类之外定义称为函数，在类之内定义称为方法

    pass


print(id(int))  # 140710743214832
print(id(Student))  # 2311840556720
print(type(Student))  # <class 'type'>
print(Student)  # <class '__main__.Student'>
