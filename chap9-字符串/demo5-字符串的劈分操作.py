# 字符串的劈分
# split()
'''
1.从字符串的左边分割，默认分隔符号是空格，返回一个列表
2.可以通过参数sep指定分割符号
3.通过参数maxsplit指定劈分字符串的最大劈分次数，
  经过最大劈分次数后，剩余的字串作为一个整体
'''
s = 'hello world python'
lst = s.split()
print(lst)

s1 = 'hello|world|python'
print(s1.split(sep='|'))
print(s1.split(sep='|', maxsplit=1))

# rsplit()  从右侧开始分割
print(s.rsplit())
print(s1.rsplit(sep='|'))
print(s1.rsplit(sep='|', maxsplit=1))
