# range是开区间
# 1
r = range(10)  # 从0开始，步长为1
print(r)  # range[0, 10)
print(list(r))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 2
r = range(1, 10)  # 步长为1,指定起始值
print(list(r))

# 3
r = range(1, 10, 2)
print(list(r))
'''判断指定整数是否在序列中'''

print(10 in r)  # False
print(9 not in r)

print(list(range(1, 101, 2)))
