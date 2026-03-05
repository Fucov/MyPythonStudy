
s='python python python'
# replace（）
# 第一个参数是被替换的，第二个是要用到的，第三个是最大替换次数 s= 'hello,python,python,python'
print(s.replace('python', 'java'))
print(s.replace('python', 'java', 2))

# join()，把列表或元组连接
# 列表
lst = ['hello', 'java', 'python']
print('|'.join(lst))
print(''.join(lst))
print(' '.join(lst))

# 元组
t = {'hello', 'java', 'python'}
print('|'.join(t))
print(''.join(t))
print(' '.join(t))

# 字符串
print('*'.join('Python'))
