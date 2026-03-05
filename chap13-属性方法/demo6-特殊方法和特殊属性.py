# @Time : 2022/8/6 16:44
# @Author : YKW
# @File : demo6-特殊方法和特殊属性.py
# 开始奇妙的python之旅吧！！！

# print(dir(object))
# 特殊属性

class A:
    pass


class B:
    pass


class C(A, B):
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 创建C类的实例对象
x = C('JACK', 20)  # x是C类型的一个实例对象
y = C('zhansgan', 50)
print(x.__dict__, y.__dict__)  # 实例对象的属性字典
print(C.__dict__)

print(x.__class__)  # 输出了对象所属的类<class '__main__.C'>
print(C.__bases__)  # C类的父类类型的元组(<class '__main__.A'>, <class '__main__.B'>)
print(C.__base__)  # 输出第一个父类
print(C.__mro__)  # 类的层次结构
print(A.__subclasses__())  # 输出所有的子类

# 特殊方法
a = 20
b = 100
c = a + b  # 整数相加
d = a.__add__(b)
print(c)
print(d)


class Student:
    def __init__(self, name):
        self.name = name

    def __add__(self, other):
        return self.name + other.name

    def __len__(self):
        return len(self.name)


stu1 = Student('张三')
stu2 = Student('李四')

s = stu1 + stu2  # 实现了两个对象的加法运算（因为在Student类中 编写了__add__）
print(s)
s = stu1.__add__(stu2)
print(s)
print('-------------------------------')
lst = [11, 22, 33, 44]
print(len(lst))  # len是内容函数len
print(lst.__len__())

print(len(stu1))
