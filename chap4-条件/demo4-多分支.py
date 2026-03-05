score=int(input('请输入成绩'))
if score>100 or score<0:
    print('成绩不符合格式')
elif score>=90:
    print('a')
elif score>=80:
    print('b')
elif score>=70:
    print('c')
else:
    print('d')