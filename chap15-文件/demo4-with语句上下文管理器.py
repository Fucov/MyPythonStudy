# @Time : 2022/8/7 17:58
# @Author : YKW
# @File : demo4-with语句上下文管理器.py
# 开始奇妙的python之旅吧！！！
"""
MyContentMgr实现了特殊方法__enter__(),__exit__()称为该类对象遵守了上下文管理器协议
这类对象的实例对象，称为上下文管理器
"""


# 在上下文管理器中，无论是否异常都会调用__exit__()自动关闭

class MyContentMgr(object):
    def __enter__(self):
        print('enter方法被调用')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # __exit__ 函数中这三个参数：
        # exc_type：异常类型
        # exc_val：异常值
        # exc_tb：异常的错误栈信息
        print('exit方法被调用')

    def show(self):
        print('show方法被调用')


with MyContentMgr() as file:
    file.show()

"""print(type(open('a.txt', 'r')))
with open('a.txt', 'r') as file:
    print(file.read())"""
