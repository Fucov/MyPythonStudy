# @Time : 2022/8/7 20:31
# @Author : YKW
# @File : demo7-os实际使用（列出指定目录下所有py文文件.py
# 开始奇妙的python之旅吧！！！
import os

path = os.getcwd()
lst = os.listdir(path)
for filename in lst:
    if filename.endswith('.py'):
        print(filename)

'''将指定目录下面的指定后缀更改为另一指定后缀'''
import os

path = 'D:\常用文件\学习\大二上\大二资料\试题\复变函数\测验题\\'
lst = os.listdir(path)
for filename in lst:
    if filename.endswith('.html'):
        url = path + filename
        os.chdir(path)
        print('url:' + url, end=' -->')
        ext = os.path.splitext(filename)  # 将文件名路径与后缀名分开
        newname = ext[0] + '.docx'
        print(newname)
        os.rename(filename, newname)
        print(filename)
