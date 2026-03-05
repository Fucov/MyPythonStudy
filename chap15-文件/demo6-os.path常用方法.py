# @Time : 2022/8/7 19:16
# @Author : YKW
# @File : demo6-os.path常用方法.py
# 开始奇妙的python之旅吧！！！
"""
abspath(path):用于获取文件或目录的绝对路径
exists(path):用于判断文件或目录是否存在，如果存在返回True,否则返回False
join(path.name):将目录与目录或者文件名拼接起来
splitext():分离文件名和扩展名
basename(path):从一个目录中提取文件名
dirname(path):从一个路径中提取文件路径，不包括文件名
isdir(path):用于判断是否为路径
"""
"""
abspath(path)只会单纯的获取文件或目录的绝对路径，
即使文件不存在，也不会报错且仍会正常返回路径
根据这个特性可以将参数path传入空字符串，
会返回代码工作目录（在没有重设工作目录时，等同于os.getcwd()）
注：传入空字符串时，返回的目录不会加上\
"""
import os.path
print(os.path.abspath('demo6-os.path常用方法.py'))
print(os.path.exists('demo6.py'), os.path.exists('demo6-os.path常用方法.py'))
print(os.path.join('E:\\Python','dmeo19.py'))
print(os.path.split('E:\Python\dmeo19.py'))
print(os.path.splitext('E:\Python\dmeo19.py'))
print(os.path.basename('E:\Python\dmeo19.py'))
print(os.path.dirname('E:\Python\dmeo19.py'))
print(os.path.isdir('E:\Python\dmeo19.py'))
print(os.path.isdir('E:\Python\d'))
"""
我们经常见到形如‘./path’或‘../path’的路径，
其中的一个.表示当前所处的文件夹的绝对路径；
两个.表示当前所处的文件夹上一级文件夹的绝对路径
"""
