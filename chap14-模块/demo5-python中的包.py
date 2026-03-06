# @Time : 2022/8/6 20:58
# @Author : YKW
# @File : demo5-python中的包.py
# 开始奇妙的python之旅吧！！！

"""
包时一个分层次的目录结构，它将一组功能相近的模块组织在一个目录下
作用：代码规范、避免模块名称冲突
包与目录的区别： 包含__init__.py文件的目录称为包

包的导入：import 包名.模块名
"""

import pageage1.moduleA as a

# 如果没有as 就这样：print(pageage1.moduleA.a)
print(a.a)  # 第一个a是模块的别名

# import这种方式 只能跟着包名或者模块名

# from...import可以导入包、模块、函数、变量
