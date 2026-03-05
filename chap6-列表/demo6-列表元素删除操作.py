
lst=[i*10 for i in range(1,6)]
print(lst)
lst.append(30)
print(lst)
# 1 remove
#从列表中移除一个元素，如果有多个，则移除第一个
lst.remove(30)
print(lst)

# 2 pop
#根据索引删除元素,如果未指定是哪个，就删除最后一个
lst.pop(1)
print(lst)

lst.pop()
print(lst)

# 3 切片
#制作一个新列表
new_list=lst[0:2]
print(new_list)

lst[1:3]=[]
print(lst)

# 4 clear
#删除所有元素,保存列表名称

lst.clear()
print(lst)

# 5 del
#删除整个列表
del lst
#print(lst)