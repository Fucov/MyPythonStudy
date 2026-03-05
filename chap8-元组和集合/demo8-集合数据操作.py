# 求交集
s1 = {i * 10 for i in range(1, 5)}
s2 = {i * 10 for i in range(3, 6)}
print(s1.intersection((s2)))
print(s1 & s2)  # intersection 和 & 等价，都是交集操作

# 求并集
print(s1.union(s2))
print(s1 | s2)  # union和 | 等价，都是并集

# 求差集
print(s1.difference(s2))  # s1比s2多出来的元素
print(s1 - s2)
print(s2.difference(s1))
print(s2 - s1)

# 对称差集
print(s1.symmetric_difference(s2))
print(s2.symmetric_difference(s1))
# 两个差集的并集
