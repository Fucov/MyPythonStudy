#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :demo12-字符串处理方法.py
# @Time      :2022/8/14 18:13
# @Author    :YKW
str='  old-python-asSAD'
print(str.lower())
print(str.upper())
print(str.count('a'))
print(str.split('a'))
print(str.replace('old','new'))
print(str.center(26,'='))  # 第二个参数是默认为空格
print(str.strip())
print(str.strip(' '))
# 删除首尾特定字符（直接写成一个字符串就行），直到遇到第一个不属于要删除的字符

print(',,'.join(str+'_SAD'))
# 把某个字符串插入到后一个字符串的两个元素之间
