

'''使用[]'''

sc={'张三':100,'李四':98,'王五':45}
print(sc['张三'])
#print(sc['张四']) 报错，keyerror

'''get方法'''
print(sc.get('张三'))
print(sc.get('陈武'))#不会报错

print(sc.get('张四',30))
#30是在查找“张四”不存在时，返回的默认值
