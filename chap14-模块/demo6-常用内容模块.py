# @Time : 2022/8/6 21:19
# @Author : YKW
# @File : demo6-常用内容模块.py
# 开始奇妙的python之旅吧！！！
import sys  # 与python解释器即其环境操作相关的标准库
import time  # 提供与时间有关的各种函数的标准库
import urllib  # 用于读取来自网上（服务器）的数据标准库

# print(dir(sys))
print(sys.getsizeof(82))  # 占字节数
print(sys.getsizeof(999))
print(sys.getsizeof(True))
print(sys.getsizeof(False))

print(time.time())  # 从1970.1.1到现在的秒数
print(time.localtime(time.time()))  # 转换为年月日时分秒
print(urllib.request.urlopen('http://www.baidu.com'))
