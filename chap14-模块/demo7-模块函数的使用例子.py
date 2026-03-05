# @Time : 2022/8/6 21:41
# @Author : YKW
# @File : demo7-模块函数的使用例子.py
# 开始奇妙的python之旅吧！！！
import schedule
import time
import sys

sum=0
def job():
    print('sum:', sum, '！！！！！！！！！')

schedule.every(2).seconds.do(job)
while True:
    sum+=1
    schedule.run_pending()
    time.sleep(1)