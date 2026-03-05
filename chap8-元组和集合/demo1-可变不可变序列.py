"""可变序列  列表  字典"""

lst=[i*10 for i in range(1,10,2)]
print(id(lst))
lst.append(300)
print(id(lst))


'''不可变序列   字符串，元组'''
s='hello'
print(id(s))
s+='world'
print(id(s))