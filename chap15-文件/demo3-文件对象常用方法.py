# @Time : 2022/8/7 12:02
# @Author : YKW
# @File : demo3-文件对象常用方法.py
# 开始奇妙的python之旅吧！！！
"""
read([size]):从文件中读取size个字节或字符的内容返回。若省略[size],则读取到文件末尾，即一次读取文件所有内容
readline():从文本文件中读取一行内容
readlines():把文件的每一行作为独立的字符串对象，并将这些对象放入列表返回
write(str):将字符串str内容写入文件
writelines(s_lst):将字符串列表s_list写入文本，不添加换行符
seek(offset[,whence]):把文件指针移动到新的位置，offset表示相对于whence的位置:offset为正往结束方向移动，为负往开始方向移动。
whence为不同的值代表不同的含义：0：从文件头开始计算（默认值）1：从当前位置开始计算2：从文件尾开始计算
tell():返回文件指针的当前位置
flush():把缓冲区的内容写入文件，但不关闭文件
close():把缓冲区的内容写入文件，同时关闭文件，释放文件对象相关的资源
"""

# file=open('a.txt','r')
# print(file.read())
# print(file.read(2))
# print(file.readlines()
# print(file.readline())
# file.close(


# file=open('a.txt','a')
# file.write('hello')
# lst=['123','hj','ghj']  # 必须是str形式
# file.writelines(lst)
# file.close()

"""
file=open('a.txt', 'r')
file.seek(2)  # 跳转到2字节（GBK一个汉字两个字节，字节从0开始数
print(file.read())  # （读取接下来的内容
print(file.tell())
file.close()
"""

"""
向文件中写入数据的时候，python并不会立刻写入，
而是会写到缓冲区，等待清空的时候写入文件
file=open('c.txt', 'a')
file.write('hello')
file.flush()
file.write('world')
file.close()
"""
