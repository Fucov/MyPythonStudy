# 1增加元素--append
lst = [i * 10 for i in range(1, 5)]
print(lst, id(lst))
lst.append(100)
print(lst, id(lst))
print()

# 2增加元素--extend
lst2 = ['hello', 'world']
# lst.append(lst2)
# 将lst2作为一个元素--['hello','world']
lst.extend(lst2)  # 一次性添加多个元素
print(lst, id(lst))
print()

# 3增加元素--insert
lst.insert(-2, 90)
print(lst, id(lst))
print()
lst.insert(1, 90)
print(lst, id(lst))
print()

# 4在任意位置添加n多个元素
lst[1:2] = lst2
lst[1:] = '2'
print(lst)
