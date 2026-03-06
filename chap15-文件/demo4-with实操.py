# @Time : 2022/8/7 18:21
# @Author : YKW
# @File : demo4-with实操.py
# 开始奇妙的python之旅吧！！！

with open('logo.png', 'rb') as src:
    with open('copy2.png', 'wb') as tar:
        tar.write(src.read())
