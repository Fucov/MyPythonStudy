# @Time : 2022/8/7 20:43
# @Author : YKW
# @File : demo8-.py
# 开始奇妙的python之旅吧！！！
import os

path = os.getcwd()
lst_files = os.walk(path)
for dirpath, dirname, filename in lst_files:
    """print(dirpath)
    print(dirname)
    print(filename)
    print('-----------------------------')"""
    for dir in dirname:
        print(os.path.join(dirpath, dir))
        # 所有目录名
    print('---------------------------------------')
    for file in filename:
        print(os.path.join(dirpath, file))
        # 所有文件名
