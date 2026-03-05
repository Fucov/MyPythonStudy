# coding=GBK
# @Time : 2022/8/7 18:39
# @Author : YKW
# @File : demo5-os模块常用函数.py
# 开始奇妙的python之旅吧！！！

# os模块是与操作系统相关的一个模块
import os
# os.system('notepad.exe') 打开记事本 相当于win+r,运行notepad
# os.system('calc.exe') 打开计算器

# 直接调用可执行文件
# os.startfile('C:\\Program Files (x86)\\Tencent\\WeChat\\WeChat.exe')
# os.startfile(r'C:\Program Files (x86)\Tencent\WeChat\WeChat.exe')  #打开微信
"""
getcwd():返回当前的工作目录
listdir(path):返回指定路径下的文件和目录信息
mkdir(path[,mode]):创建目录
makedirs(path1/path2...[,mode]):创建多级目录
redir(path):删除目录
removedirs(path1/path2.......):删除多级目录
chdir(path):将path设置为当前工作目录
"""
print(os.getcwd())
print()

lst=os.listdir('../chap15-文件')
print(lst)
print()

# os.mkdir('newdir2')

# os.makedirs('A/B/C')

# os.rmdir('newdir2')

# os.removedirs('A/B/C')

# os.chdir()
