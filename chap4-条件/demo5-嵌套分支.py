ans = input('您是会员吗？y/n\n')
mon = int(input("请输入金额:"))
if ans == 'y':
    print('会员')
    if mon >= 200:
        print('付款：', mon * 0.8)
    elif mon >= 100:
        print('付款：', mon * 0.9)
    else:
        print('付款：', mon)
else:
    print('非会员')
    if mon >= 200:
        print('付款：', mon * 0.95)
    else:
        print('付款：', mon)
