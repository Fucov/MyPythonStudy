sc={'张三':100,'李四':98,'王五':45}

#获取key
keys=sc.keys()
print(type(keys),keys)
print(list(keys))#将所有key组成的视图转化成列表

#获取value
values=sc.values()
print(type(values),values)
print(list(values))

#获取key-value对

items=sc.items()
print(type(items),items)
print(list(items))#每一个（）都是一个元组