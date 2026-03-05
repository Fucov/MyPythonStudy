
# 1 使用（）
t= ('python', 'world', 98)
print(t)
print(type(t))

t2 = 'python', 'world', 98
print(t2)
print(type(t2))
# 如果元组内部只有一个元素，逗号不能省略
t3 = ('python',)
print(t3)
print(type(t3))

# 2使用tuple


t1 = tuple(('python', 'world', 98))
print(t1)
print(type(t1))

# 空元组创建

lst = []
lst1 = list()

d = {}
d1 = dict()

t4 = ()
t5 = tuple()
print('空列表', lst, lst1)
print('空字典', d, d1)
print('空元组', t4, t5)
