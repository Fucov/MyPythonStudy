# @Time : 2022/8/5 21:43
# @Author : YKW
# @File : demo2-继承.py
# 开始奇妙的python之旅吧！！！

class person(object):#默认是object
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print('姓名：%s,年龄：%d' % (self.name,self.age))
        print('姓名：{0}，年龄：{1}'.format(self.name,self.age))

# 定义子类
class student(person):
    def __init__(self,name,age,num):
        super().__init__(name,age)#调用父辈的属性
        self.num=num

class teacher(person):
    def __init__(self,name,age,toy):
        super().__init__(name,age)
        self.tof=toy

#测试
stu=student('jack',20,1001)
tec=teacher('sam',50,20)

stu.info()
tec.info()
#可以多继承
class A(object):
    pass
class B(object):
    pass
class C(A,B):
    pass

