#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :demo7-字典相等比较.py
# @Time      :2022/9/11 17:47
# @Author    :YKW

import operator

a = {'a': 1, 'b': 2}
b = {'a': 1, 'b': 2}
c = {'a': 2, 'b': 2}
print(operator.eq(a, b))  # True
print(operator.eq(a, c))  # False

print(a == b)  # True
print(a == c)  # False
