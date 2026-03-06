"""
for的break

for i in range(3,0,-1):
    it=input("请输入密码:")
   # if i>0:
    if it=='123456':
        print('right!')
        break
    else:
        print('wrong!you only have',i-1,'times left')
   # else:
     #   print('you have 0 time left')"""

a = 0
while a < 3:
    a += 1
    it = input("请输入密码:")
    # if i>0:
    if it == '123456':
        print('right!')
        break
    else:
        print('wrong!you only have', 3 - a, 'times left')
# else:
#   print('you have 0 time left')
