



a,b=10,20
print('a>b?',a>b)
print('a<b?',a<b)
print('a>=b?',a>=b)
print('a<=b?',a<=b)
print('a!=b?',a!=b)
print('a==b?',a==b)
'''
    ==比较的是值
    is比较的是标识
'''
a=10
b=10
print(a==b) #比较值
print(a is b)#比较id标识
print(a is not b)

list1=[11,22,33,44]
list2=[11,22,33,44]
print(list1==list2)
print(list1 is list2)
print(list1 is not list2)
print(id(list1))
print(id(list2))