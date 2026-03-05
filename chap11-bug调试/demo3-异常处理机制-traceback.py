# @Time : 2022/8/5 11:36
# @Author : YKW
# @File : demo3-异常处理机制-traceback.py
# 开始奇妙的python之旅吧！！！

# print(10/0)
import traceback

try:
    print('----------------------------------')
    print(1 / 0)
except:
    traceback.print_exc()
