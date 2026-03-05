

#第一种方式,使用[]
lst1=[1,2,3,4,3,4,5]


#第二种方式，使用函数，list
lst2=list(['12',12,'wof'])
"""print(lst1[-2],lst1[2],lst2)"""

#指定元素的索引
print(lst1.index(3))
print(lst1.index(3,3,6))