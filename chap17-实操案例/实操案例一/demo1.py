#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :demo1.py
# @Time      :2022/8/10 16:59
# @Author    :YKW

# 方式一：使用print函数进行输出
fp = open('demo1.txt', 'a')
print('writing demo1.txt...', file=fp)  # 不会追加\n
fp.close()

# 方式二：使用文件读写操作
with open('demo1.txt ', 'a') as wfile:
    wfile.write('writing demo1.txt...')  # 会自动换到下一行输出

# f
