# 集合元素判断操作
s = {i * 10 for i in range(1, 6)}  # 集合是无无序的
print(s)
print(10 in s)
print(100 in s)
print(10 not in s)
print(100 not in s)

# 集合元素新增操作
# add一次增加一个元素
s.add(80)
print(s)

# update一次增加多个元素（至少一个
s.update({200, 300, 400})
print(s)

s.update([123, 456])  # []列表
s.update((963, 951))  # ()元组
print(s)

'''集合元素删除操作'''

# 1 remove()要求删除元素必须存在，有返回值
s.remove(300)
print(s)

# 2 dicard()不要求删除元素必须存在，没有返回值
s.discard(999)
print(s)

# 3 pop(),不能指定删除特定，而是随机删除某一项（应该是第一项，但是集合无序
s.pop()
print(s)
s.pop()
print(s)

# 4 clear(),清空集合为空集合，没有删除数组
s.clear()
print(s)
