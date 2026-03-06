# @Time : 2022/8/5 20:51
# @Author : YKW
# @File : demo4-动态绑定属性和方法.py
# 开始奇妙的python之旅吧！！！
class student:
    def __init__(self, name, age):  # 只有两个共有实例属性
        self.name = name
        self.age = age

    def eat(self):
        print(self.name + ' is eating')


stu1 = student('zhangsan', 20)
stu2 = student('lisi', 30)

print(id(stu1))
print(id(stu2))
print('----------为stu2添加gender属性----------------------------')
stu2.gender = 'female'  # 只为stu1添加gender属性
print(stu1.name, stu1.age)
print(stu2.name, stu2.age, stu2.gender)

stu1.eat()
stu2.eat()

print('----------为stu1绑定show方法----------------------')


def show():
    print('定义在类以外的，称为函数')


stu1.show = show
stu1.show()
