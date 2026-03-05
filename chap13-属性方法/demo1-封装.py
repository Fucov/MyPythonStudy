# @Time : 2022/8/5 21:29
# @Author : YKW
# @File : demo1-封装.py
# 开始奇妙的python之旅吧！！！
class Car:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print('start!!!')


car1 = Car('汗血宝马')


# car1.start()
# print(car1.brand)

class student:
    def __init__(self, name, age):
        self.name = name
        # 如果不希望该属性阿紫类外部访问，
        # 可以在前面加上__(两个下划线)
        self.__age = age

    def show(self):
        print(self.name, self.__age)


stu = student('zhangssan', 20)
stu.show()
print(stu.name)
# print(stu.__age) 不能正常使用
print(dir(stu))
# 在类的外部也可以访问，（实例名._类名称__属性名称）
print(stu._student__age)
