

#1-50，5的倍数

"""for i in range(1,51):
    if not bool(i%5):
        print(i)"""

for i in range(1,51):
    if bool(i%5):
        continue
    print(i)
