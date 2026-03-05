'''
常见异常：
#  ZeroDivisionError:除（或者取模）零（所有数据类型）
print(10/0)

#  IndexError：序列中没有此索引
lst=[11,22,33]
print(lst[4])

#  KeyError：映射中没有这个键
dic={'name':'张三','age':20}
print(dic['gender'])

#  NameError：未声明/初始化对象（没有属性）
print(num)

#  SyntaxError：Python语法错误
int a=20

#  ValueError ：传入无效的参数
a=int('hello')
'''

# try- except-else-finally
# 如果try没有异常，执行else
# 如果try出现异常，执行except
# 无论try是否异常，finally都会执行
'''try:
    n1=int(input('第一个整数：'))
    n2=int(input('第二个整数：'))
    ans=n1/n2
except ZeroDivisionError:
    print('除数不能为0哦！！！')
except ValueError:
    print('你输入的是数字吗！！！')
except BaseException as e:
    print('出错了',e)
else:
    print('结果为：', ans,type(ans))
    '''
try:
    n1 = int(input('第一个整数：'))
    n2 = int(input('第二个整数：'))
    ans = n1 / n2
except BaseException as e:
    print('出错了', e)
else:
    print('结果为：', ans, type(ans))
finally:
    # 可以用来清空变量
    n1 = n2 = 0
    # print(n1,n2)
    print('谢谢您的使用(无论是否异常，都会执行')
    print('程序结束')
