
# 赋值运算符 a= 3 + 4
print(a)
# 链式赋值

a = b = c = 200000000
print(a, id(a))
print(b, id(b))
print(c, id(c))

# 参数赋值

a = 20
print(a, id(a))
a += 30
print(a, id(a))
a -= 30
print(a, id(a))
a *= 30
print(a, id(a), type(a))
a /= 3
print(a, id(a), type(a))
a //= 15
print(a, id(a))
a %= 3
print(a, id(a), type(a))

# 系列解包赋值
a, b, c = 10, 20, 30
print(a, b, c)
a, b, c = c, b, a
print(a, b, c)
