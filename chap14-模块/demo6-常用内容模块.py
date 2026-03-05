# @Time : 2022/8/6 21:19
# @Author : YKW
# @File : demo6-常用内容模块.py
# 开始奇妙的python之旅吧！！！
import sys  # 与python解释器即其环境操作相关的标准库
import time  # 提供与时间有关的各种函数的标准库
import os  # 提供了访问操作系统服务功能的标准库
import urllib  # 用于读取来自网上（服务器）的数据标准库
import calendar  # 提供了与日期相关的各种函数的标准库
import json  # 用于使用JSON序列化和反序列化对象
import re  # 用于在字符串中执行正则表达式匹配和替换
import math  # 提供标准算术运算函数的标准库
import decimal  # 用于进行精确控制运算精度、有效位数和四舍五入的十进制运算
import logging  # 提供了灵活的记录事件、错误、警告和调试信息等日志信息的功能
# print(dir(sys))
print(sys.getsizeof(82))  #占字节数
print(sys.getsizeof(999))
print(sys.getsizeof(True))
print(sys.getsizeof(False))

print(time.time())  # 从1970.1.1到现在的秒数
print(time.localtime(time.time()))  # 转换为年月日时分秒
print(urllib.request.urlopen('http://www.baidu.com'))