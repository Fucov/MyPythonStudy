# 通用序列技巧
lst1 = [1, 2, 3]
lst2 = [4, 5, 6]
print(lst1, lst2)
print(lst1 + lst2)
print(lst1 * 2, lst2 * 3)
print(len(2 * lst1))
print(max(lst1 * 2 + lst2))
print(min(lst1 * 2 + lst2))
print(2 * lst1)

# print(2*lst1.index(1,1,5))  不行

lst3 = lst1 + lst1
print(lst3.index(1, 1, 5))

print(2 * lst1.count(1))  # 可行

print('-----------字符串技巧-------------------------')
str1 = 'python'
str2 = 'python2'
str3 = '123456'
list1 = [1, 'a', 'sad']
list1.reverse()  # 反向列表
print(list1)

print(str1.isalpha())
print(str2.isalnum())
print(str3.isdigit())
