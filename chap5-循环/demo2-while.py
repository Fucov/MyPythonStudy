sum = 0
ans = int(input('请输入初始值:'))
ans_1 = int(input('请输入结束值:'))
ans_2 = int(input('请输入步长:'))

while ans <= ans_1:
    sum += ans
    ans += ans_2
print(sum)
