



for item in 'python':
    print(item)


#range产生一个整数序列
for i in range(10):
    print(i)


#如果在循环体中不需要用到自定义变量，
# 可以将自定义变量写为“_”
for i in 'range(5)':
    print("dsb")
    print(i)


#使用for循环，进行求和计算
sum=0
for i in range(1,101):
    if not bool(i%2):
        sum+=i
print(sum)