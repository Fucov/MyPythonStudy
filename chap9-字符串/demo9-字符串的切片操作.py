# 字符串是不可变类型 不能进行增删改操作 切片会产生新的对象
s = 'hello,Python'
print(s[:5])
print(s[6:])
print(s[1:9:2])
print(s[6:] + s[:5])

# 切片     [start:stop:step] 不包括stop,从start开始算
print(s[1:5:1])
print(s[::2])
print(s[::-1])
print(s[-6::])  # 从索引为-6开始，到字符串的最后一个结束
"""lst=s.split(sep=',')
print(lst[1])"""
