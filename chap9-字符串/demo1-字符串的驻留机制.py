# 字符串的驻留机制
"""
交互模式（idle即shell)下驻留情况：
* 字符串长度为0或者1
* 符合标识符(由字母、数字、下划线组成)的字符串
* 字符串只在编译时进行驻留，而非运行时
* [-5,256]的整数数字
"""
str1 = 'python'
str2 = "python"
str3 = '''python'''  # 三个单引号
str4 = """python"""
'''132'''
print(str1, id(str1))
print(str2, id(str2))
print(str3, id(str3))
print(str4, id(str4))
