'''''第一种，C语言模式，%作为占位符'''''

name='张三'
age=20
print('我叫%s,今年%d岁'%(name,age))
print('我叫%s,今年%d岁' % (name,age))#元组

    # %的精度
print('%10d' % 99)
print('hellohello')
print('%f'% 3.1415926)
print('%.18f'% 3.1415926)
print()
    # 同时表示宽度和精度
print('%10.3f' % 3.1415926)#总宽度为10（包括小数位
print('')

'''第二种 {}作为占位符，使用format方法,槽机制'''

print('我叫{0}，今年{1}岁'.format(name,age))
print()

    # 槽内部对格式化的配置方法
'''
    :       <填充> <对齐>              <宽度> <,> <.精度> <类型>
    引导符号        <左对齐 >右对齐 ^居中     整数类型：b,c,  d, o,x, X 浮点数：e,E,f,%
                                                  2,uni,10,8,16,大写16
'''
print('{0:=>20}'.format('python'))
print('{0:*^20}'.format('bit'))
print('{:2}'.format('bit'))

print('{0:,.5f}'.format(12346789.123546))
print('{0:b},{0:c},{0:d},{0:o},{0:x},{0:X}'.format(425))
print('{0:e},{0:E},{0:f},{0:%}'.format(3.14))
print()

    # {}里面的序号是format方法的参数序号
print("{1}:计算机{0}的CPU占用率为{2}%".format('2018-10-10','C',10))
print()

    # {}的精度
print('{:.3}'.format(3.1415926))#3.14
print('{0:.3}'.format(3.1415926))#3.14   .3表示一共三位数

print('{:.3f}'.format(3.1415926))#3.142
print('{0:.3f}'.format(3.1415926))#3.142   .3f表示三位小数

print('{:10.3f}'.format(3.1415926)) #同时设置字符串的宽度和精度
print()

'''第三种 f-string'''
print(f'我叫{name}，今年{age}岁')