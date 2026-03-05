
# 大小写转换 s= 'hello,python'

# 转大写
a = s.upper()
print(s, id(s))
print(a, id(a))  # 产生新字符串

# 转小写
print(s, id(s))
print(s.lower(), id(s.lower))

# 反转函数，大写变小写，小写变大写 swapcase()
s2 = 'hello,PYThON,fasd'
print(s2, id(s2))
print(s2.swapcase(), id(s2.swapcase()))

# 把第一个字符转为大写，其余的转为小写 capitalize
print(s2.capitalize())
# title()把每个单词的第一个字符转为大写，每个单词剩余字符转为小写
print(s2.title())

print("Are you dEmo?".upper().lower().swapcase().capitalize().title())
