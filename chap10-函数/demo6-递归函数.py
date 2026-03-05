# 求阶乘
def fun(a):
    if a == 1:
        return 1
    return a * fun(a - 1)


print(fun(5))


# 斐波那契数列
def fib(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


# 输出第几位
print(fib(6))

# 输出前几位
for i in range(1, 2):
    print(fib(i))

a = 2
for i in range(3):
    if a > 3:
        break
    else:
        print('错误')
else:
    print("gui")
