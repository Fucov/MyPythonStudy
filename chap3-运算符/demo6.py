# 布尔运算符
# and
a, b = 1, 2
print(a == 1 and b == 2)
print(a == 1 and b < 2)
print(a != 1 and b == 2)
print(a != 1 and b != 2)

# or
print(a == 1 or b == 2)
print(a == 1 or b < 2)
print(a != 1 or b == 2)
print(a != 1 or b != 2)

# not
f = True
f2 = False
print(not f)
print(not f2)

# in   , not in是否存在字符串中

s = 'helloworld'
print('k' in s)
print("sd" in s)
print("hell" in s)
