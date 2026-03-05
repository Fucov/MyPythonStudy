# 两个集合是否相等

s1 = {10, 20, 30, 40}
s2 = {40, 30, 20, 10}
print(s1, s2)
print(s1 == s2)  # 只比较元素值，与顺序无关
print(s1 != s2)

# 是否是子集

s1 = {i * 10 for i in range(1, 7)}
s2 = {i * 10 for i in range(1, 4)}
s3 = {10, 20, 90}
print(s2.issubset(s1))  # True
print(s3.issubset(s1))  # False

# 是否是超子集

print(s1.issuperset(s2))
print(s1.issuperset(s3))

# 集合有没有交集
print(s2.isjoint(s3))  # True
print(s2.isdisjoint(s3))  # False
