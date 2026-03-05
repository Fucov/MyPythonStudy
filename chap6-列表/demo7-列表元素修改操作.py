
lst=[i*10 for i in range(1,5)]
print(lst)

#一次修改一个值
lst[2]=100
print(lst)

lst[1:3]=[i*100 for i in range(3,7)]
print(lst)