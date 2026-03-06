# @Time : 2022/8/6 20:34
# @Author : YKW
# @File : demo3-导入模块.py
# 开始奇妙的python之旅吧！！！
import math  # 导入这个模块所有函数方法

print(id(math))
print(type(math))
print(math)
print(math.pi)
print('-------------------------------------------------')
print(dir(math))
print(math.pow(2, 3.2), type(math.pow(2, 3)))
print(pow(2, 3.2), type(pow(2, 3)))  # 幂
print(math.ceil(9.001))  # 向上取整
print(math.floor(9.9999))  # 向下取整

from math import pow  # 导入这个模块某一个函数方法

print('------------------------------------------')
print(pow(2, 3.2), type(pow(2, 3)))

#  导入自定义模块
import calc

print(calc.add(10, 30))
print(calc.div(10, 4))
print(dir(calc))

from calc import add

print(add(10, 50))
