# @Time : 2022/8/6 22:07
# @Author : YKW
# @File : demo2-常用文件打开模式.py
# 开始奇妙的python之旅吧！！！
"""
r 以只读模式打开文件，指针放在文件的开头

file = open('a.txt', 'r')
print(file.readlines())
print(file.readline())
file.close()
"""

"""
w 以只写模式打开文件，不存在则创造，存在则覆盖，指针放在文件的开头

file = open('b.txt', 'w')
file.write('Python')
file.close()
"""


'''
# a 以追加模式打开文件，不存在则创造，存在则在末尾追加内容，指针放在文件的开头
file = open('b.txt', 'a')
file.write('\n#Python')
file.close()
'''

"""
b 以二进制方式打开文件，不能单独使用，需要与其他模式一起使用，rb,或者wb

#复制图片
src_file=open('logo.png','rb')
target_file=open('copylogo.png','wb')
target_file.write(src_file.read())
target_file.close()
src_file.close()
"""

"""
+ 以读写方式打开，不能单独使用，需要与其他模式一起使用，a+
"""
str1 = []
with open('b.txt','r',encoding='utf-8') as w:
    str1 = w.readlines()
with open('b.txt','a',encoding='utf-8') as afile:
    afile.write(str('12331')+'\n')
    for it in str1:
        afile.write(it)