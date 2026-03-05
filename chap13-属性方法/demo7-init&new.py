# @Time : 2022/8/6 17:52
# @Author : YKW
# @File : demo7-init&new.py
# 开始奇妙的python之旅吧！！！

# 每创建一个新的类对象，都默认调用一次new，
# 每创建一个新实例对象,都会默认调用一次init(初始化)
"""
    讲的意思是：创建对象，先调用new，返回，再执行init  ，
    cls地址对应类的地址，self地址对应创建的实列对象地址
总结：执行实例创建：
    1.先将类名(Person)传给new的cls，开新空间(obj)用于后续实例对象创建
    2.接受到obj的self，实例对象p1指向self
"""


class Person(object):
    def __new__(cls, *args, **kwargs):
        print('__new__被调用执行了，cls的id值为{0}'.format(id(cls)))
        obj = super().__new__(cls)
        print('创建的对象的id为：{0}'.format(id(obj)))
        return obj

    def __init__(self, name, age):
        print('__init__被调用了，self的id值为：{0}'.format(id(self)))
        self.name = name
        self.age = age


print('object的id为：{0}'.format(id(object)))
print('Person的id为：{0}'.format(id(Person)))

# 创建实例对象
p1 = Person('张三', 20)
print('p1这个实例对象的id为：{0}'.format(id(p1)))
