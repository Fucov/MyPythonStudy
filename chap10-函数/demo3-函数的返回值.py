def fun(num):
    odd = []  # 奇数
    even = []  # 偶数
    for i in num:
        if i % 2:
            odd.append(i)
        else:
            even.append(i)
    odd.sort()
    even.sort()
    return odd, even


print(fun([10, 29, 34, 23, 44, 53, 55]))

'''
函数的返回值
1. 如果函数没有返回值，则return可以省略不写
2. 函数的返回值如果只有一个，则返回该类型
3. 函数的返回值如果有多个，返回的类型为元组
'''


# 1
def fun1():
    print('hello')
    return


fun1()


# 2
def fun2():
    return 'hello'


res = fun2()
print(res)


# 3
def fun3():
    return 'hello', 'world'


print(fun3())
