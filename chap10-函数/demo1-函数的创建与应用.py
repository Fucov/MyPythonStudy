
def calc(a ,b)  :  # 形参  函数定义中
    return a/ b


# 实参
a = int(input('第一个：'))
b = int(input('第二个：'))
# 位置实参
print(calc(a, b))

# 关键字实参
print(calc(a=a, b=b))
# 前面红色的是关键字参数，后面的是实参

print(calc(b=a, a=b
))