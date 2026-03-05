def fun(a1, a2):
    print('a1:', a1)
    print('a2:', a2)
    a1 = 100
    a2.append(100)
    print('a1:', a1)
    print('a2:', a2)


n1 = 10
n2 = [20, 30, 40]
fun(n1, n2)
print(n1, n2)
# int 元组不可变，形参不会影响实参
# 字典、列表、集合，形参会影响实参
