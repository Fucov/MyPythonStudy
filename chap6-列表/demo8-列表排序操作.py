lst = [20, 40, 65, 32, 95, 54]

print(lst, id(lst))

# sort方法，默认升序
lst.sort()
print(lst, id(lst))

lst.sort(reverse=False)
print(lst, id(lst))

# 通过指定关键词，进行降序排列
lst.sort(reverse=True)
print(lst, id(lst))

# 使用内置函数sorted,产生一个新列表
newlst = sorted(lst)
print(newlst)

# 通过指定关键词，降序
newlst2 = sorted(lst, reverse=True)
print(newlst2)
