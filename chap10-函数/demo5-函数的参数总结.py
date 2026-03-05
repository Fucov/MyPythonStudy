'''#列表作为形参时，要加上一个*'''


def fun(a, b, c):
    # a,b,c在函数的定义处，所以是形式参数
    print('a=', a)
    print('b=', b)
    print('c=', c)


fun(10, 20, 30)  # 函数调用时的参数传递，称为位置传参

lst = [11, 22, 33, ]
# 报错 fun(lst)
fun(*lst)
# 在函数调用时，将列表中的每个元素都转换为位置形参传入

'''#字典作为形参时，要加上一个**'''
fun(a=2021, c=5023, b=3012)

dic = {'a': 265, 'b': 3265, 'c': 213}
# 报错 fun(dic)
fun(**dic)
# 在函数调用时，将字典中的每个元素都转换为关键字形参传入

'''#位置实参传递和关键字实参传递可以混合使用'''


def fun2(a, b, *, c, d):
    # *之后只能用关键字实参传递，否则会报错
    print('a=', a)
    print('b=', b)
    print('c=', c)
    print('d=', d)


# fun2(10,20,30,40) #位置实参传递
print()
fun2(a=10, b=20, c=30, d=40)  # 关键字实参传递
print()
fun2(10, 20, c=30, d=40)  # 混合传递
'''假需求，c,d只能采用关键字实参传递'''


def fun3(a, b, *, c, d, **args):
    pass


def fun4(*args1, **args2):
    pass


def fun5(a, b=10, *args1, **args2):
    pass
