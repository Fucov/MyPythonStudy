# 转义字符

# \  +转义功能的首字符
# n-->newline的首字符

print('hello\nworld')
# t-->tab
print('hello\tworld')  # 三个空格
print('helloooo\tworld')  # 四个空格
# r-->return
print('hello\r')
print('hello\rworld')  # \r回车，world把hello覆盖
# b-->backspace
print('hello\bworld')  # \b退格

print('http:\\\\www.baidu.com')
print('老师说:\'大家好\'')
print("老师说:\'大家好\'")

# 原字符，不希望字符串中的转义字符起作用，
# 就使用原字符，就是在字符串之前加上r,或R
print(r'老师说:\'大家好\'')
print(R'hello\rworld')

# 注意事项，最后一个字符不能是反斜杠\
# print(r'hello\rworld\')
print(r'hello\rworld\\')
