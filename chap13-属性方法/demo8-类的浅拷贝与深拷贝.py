# @Time : 2022/8/6 18:14
# @Author : YKW
# @File : demo8-类的浅拷贝与深拷贝.py
# 开始奇妙的python之旅吧！！！
class Cpu:
    pass


class Disk:
    pass


class Computer:
    def __init__(self, cpu, disk):
        self.cpu = cpu
        self.disk = disk


# 1 变量的赋值
cpu1 = Cpu()
cpu2 = cpu1
print(cpu1, id(cpu1))  # 两个都一样
print(cpu2, id(cpu2))

# 2 浅拷贝
print('-----------------------------------------')
disk = Disk()  # 创建一个Disk类的对象
com = Computer(cpu1, disk)  # 创建一个Computer类的对象

import copy

'''
{赋值：贴上第二个门牌（主、子对象都不变
浅拷贝：开了第二个门（主对象变、子对象不变
深拷贝：租了一个一模一样的新家}
浅拷贝是重新建了一个Computer的实例对象 
相对于原来的实例对象id变了 但value(属性)不变 
因此新拷贝出来的Computer实例对象的cpu
和disk类属性还是原来的
'''
com2 = copy.copy(com)
com3 = com
print(com, com.cpu, com.disk)
print(com2, com2.cpu, com2.disk)
print(com3, com3.cpu, com3.disk)  # 第一个不一样，其他两个属性都一样

#3 深拷贝
print('---------------------------')
com4=copy.deepcopy(com)
print(com, com.cpu, com.disk)
print(com4, com4.cpu, com4.disk)  #三个都不一样