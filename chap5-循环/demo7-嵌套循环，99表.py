

"""#输出三行四列矩形
for i in range(1,4):
    for j in range(1,5):
        print('*',end='\t')# 横向制表符
    print()#换行"""

for i in range(1,10):
    for j in range(1,i+1):
        print(j,'*',i,'=',i*j,end='\t')
    print()


