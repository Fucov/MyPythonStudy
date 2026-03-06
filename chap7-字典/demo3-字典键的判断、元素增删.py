sc = {'张三': 100, '李四': 98, '王五': 45}
print('张三' in sc)
print('张三' not in sc)

del sc['张三']  # 删除指定键值对
print(sc)
"""
sc.clear()  清空字典中的所有元素
print(sc)
"""
sc.popitem()

sc['陈留'] = 99  # 新增元素
print(sc)

sc['陈留'] = 30
print(sc)  # 修改元素
