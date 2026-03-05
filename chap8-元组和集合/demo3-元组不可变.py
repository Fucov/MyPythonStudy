t = (10, [20, 30], 5)
print(t)
print((type(t)))
print(t[0], type(t[0]), id(t[0]))
print(t[1], type(t[1]), id(t[1]))
print(t[2], type(t[2]), id(t[2]))

'''尝试将t[1]修改成100'''
print(id(100))
# t[1]=100   元组不允许修改元素


# 但是向列表中添加元素可以，因为列表是可变的
t[1].append(100)
print(t)
