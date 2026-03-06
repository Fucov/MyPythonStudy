# 集合是没有value的字典

"""第一种创建方式"""
# 列表
lst = [i for i in range(1, 10)]

# 集合set
s = {i for i in range(1, 10)}

# 字典dict
dic = {a: b for a, b in zip(range(11, 20), range(1, 10))}

# generator
t = (i for i in range(1, 10))

print(lst, type(lst))
print(s, type(s))
print(dic, type(dic))
print(t, type(t))

'''第二种set函数'''

s1 = set(range(6))
print(type(s1), s1)

print(set([3, 4, 132]))
print(set((3, 3, 2, 4)))
print(set('python'))  # 无序
print(set({1, 123, 456}))
print(set())

# 定义空集合
s7 = set()
print(type(s7))
