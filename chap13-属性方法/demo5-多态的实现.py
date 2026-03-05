# @Time : 2022/8/6 7:57
# @Author : YKW
# @File : demo5-多态的实现.py
# 开始奇妙的python之旅吧！！！

"""
多态（具有多种形态）：即使不知道一个变量所引用的对象到底是什么类型，
仍然可以通过这个变量调用方法，在运行过程中改变所引用对象的类型，
动态决定调用哪个对象中的方法

##不管类型到底是什么，只要内部包括这个方法，就可以调用
"""


class Animal(object):
    def eat(self):
        print('动物要吃东西')


class Dog(Animal):
    def eat(self):
        print('狗吃肉')


class Cat(Animal):
    def eat(self):
        print('猫吃鱼')


class Person(object):
    def eat(self):
        print('人吃五谷杂粮')


cat1 = Cat()
cat1.eat()
'''
问为什么括号Cat要加括号的绝对是前面没能理解透彻的
Cat()是类，这其实是一个实例化过程，只是没有将其赋值。如果将c=Cat()，然后再传fun(c)是与前面等效的
而Cat单纯是一个类名，它没有实例化，传进去也就缺少self参数，就无法运行实例方法

n(Cat也是可以的)

'''
a = Cat()
a.eat()


def fun(animal):
    animal.eat()


fun(Dog())
fun(Cat())
fun(Animal())
print('--------------------------------')
fun(Person())
