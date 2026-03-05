# 存在字符

s = 'hello,hello'
print(s.index('lo'))
print(s.find('lo'))
print(s.rindex('lo'))
print(s.rfind('lo'))

# 不存在字符

# print(s.index('k'))  如果没有该字符，则报错
print(s.find('k'))  # 返回-1
# print(s.rindex('k'))
print(s.rfind('k'))
