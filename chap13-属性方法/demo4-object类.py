# @Time : 2022/8/6 7:25
# @Author : YKW
# @File : demo4-object类.py
# 开始奇妙的python之旅吧！！！
"""
* object类是所有类的父类，所有类都有object类的属性和方法
* 内置函数dir()可以查看指定对象的所有属性
* object有一个__str__()方法，用于返回一个对于’对象的描述‘
  print(实例名)等价于print(实例名.__str__)
  因此常对__str__()进行改写
"""


class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print('姓名：{0}，年龄：{1}'.format(self.name, self.age))

    def __str__(self):
        return '姓名：{0}，年龄：{1}'.format(self.name, self.age)


o = object()
p = Person('Jack', 20)
'''print(dir(o))
print(dir(p))'''
print(p)
print(p.__str__())  # 就是print(p)
p.info()
print(type(p))
print()