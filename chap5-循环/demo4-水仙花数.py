for i in range(99, 1000):
    if i == (i % 10) ** 3 + ((i // 10) % 10) ** 3 + (i // 100) ** 3:
        print(i)
