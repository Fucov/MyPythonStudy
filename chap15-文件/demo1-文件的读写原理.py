# @Time : 2022/8/6 21:59
# @Author : YKW
# @File : demo1-文件的读写原理.py
# 开始奇妙的python之旅吧！！！

file = open('a.txt', 'r')
print(file.readlines())
print(file.readline())
file.close()