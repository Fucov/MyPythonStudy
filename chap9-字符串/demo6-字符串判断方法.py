
# 1.isidentifier() 是否只包含合法字符（字母、数字、下划线）
# 中文也会被python判定为字母，py支持中文作为变量
'''
合法标识符：
1.不能以数字开头
2.不能包含非法字符
3.数字不能作为标识符
4.不能包含空格
5.不能包含运算符
'''
s='hello,python'
print('1.',s.isidentifier())
print('2.','he llo'.isidentifier())
print('3.','123'.isidentifier())#True
print('4.','2张三_123'.isidentifier())

# 2.isspace()判断字符串是否全部由
# 空白字符（回车、换行、水平制表符）组成
print('5.',' \t \r'.isspace())

# 3.isalpha
print('6.','acssa'.isalpha())#True
print('7.','张三'.isalpha())
print('8.','张三1'.isalpha())

# 4.isdecimal()判断全部由十进制字母组成
print('9.','123'.isdecimal())#True
print('10.','123四'.isdecimal())
print('11.','ⅳⅱⅲⅳⅴⅵ'.isdecimal())#罗马数字

# 5.isnumeric()判断全由数字组成
print('12.','123'.isnumeric())#True
print('13.','123四'.isnumeric())#True
print('14.','ⅳⅱⅲⅳⅴⅵ'.isnumeric())#罗马数字#True
print('15.','④⑤⑤⑶⑷⑸⑻⒈⒔㈠㈡一二三四'.isnumeric())#True

# 6.isalnum()
print('16.','axdvs123'.isalnum())#True
print('16.','张三123'.isalnum())#True
print('16.','axdvs123！'.isalnum())

