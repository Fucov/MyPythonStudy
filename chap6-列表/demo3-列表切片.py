

lst=[i*10 for i in range(1,10)]
print(lst)

#lst[start:stop:step]
#左开右闭
#step为正
print(lst[1:6:1])

#step不写，默认为1
print(lst[1:6])
print(lst[1:6:])

#start不写，默认为0
print(lst[:6:1])
print(lst[:6:])

#stop不写默认为最后一个
print(lst[1::1])
print(lst[1::])

#step为负数情况
print('----------------step为负数情况--------------------------')
print(lst[::-1])

print(lst[-2::-1])
print(lst[7::-1])

print(lst[9:-8:-1])

