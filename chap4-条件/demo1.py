# 测试对象的布尔值
print('-----------------以下布尔运算为False-----------')

print(bool(False))
print(bool(0))
print(bool(0.0))
print(bool(None))
print(bool(''))
print(bool(""))
print(bool([]))  # 空列表
print(bool(list()))  # 空列表
print(bool(()))  # 空元组
print(bool(tuple()))  # 空元组
print(bool({}))  # 空字典
print(bool(dict()))  # 空字典
print(bool(set()))  # 空集合

print('----------------以下布尔运算为True---------------')

print(bool(18))
print(bool(True))
print(bool('helloworld'))
