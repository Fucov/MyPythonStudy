# 字符串对齐

# center() 居中对齐，第一个参数是指定宽度，第二个参数是指定填充符
# 第二个参数默认是空格，如果设置宽度小于字符串宽度则返回原字符串
s = 'hello,python'
print(s.center(20))
print(s.center(20, '*'))

# ljust() 左对齐，两个参数.....
print(s.ljust(20, '*'))
print(s.ljust(20))
print(s.ljust(10))

# rjust() 右对齐，两个参数.....
print(s.rjust(20, '*'))
print(s.rjust(20))
print(s.rjust(10))

# zfill() 右对齐，左边用0填充，该函数只有一个参数为指定宽度
print(s.zfill(20))
print(s.zfill(10))

print('-8910'.zfill(8))
