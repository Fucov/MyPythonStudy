# 输出：print函数

# 输出数字
print(123)
print(98.5)

# 输出字符串
print("gellowe")
print('sdaj')

# 输出运算的结果
print(3 * 2)
# 输出在文件内
# ‘a+’: 如果文件不存在，就建立文件；如果存在，直接在后面附加
fp = open('D:/常用文件/学习/编程/pycharm/text.txt', 'a+')
print('helloworld', file=fp)
fp.close()

# 不换行输出
print('hello', 'world', 'python')
