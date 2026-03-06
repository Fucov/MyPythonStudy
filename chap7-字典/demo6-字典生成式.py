items = ['fruits', 'books', "others"]
prices = [98, 32, 45]
lst = zip(items, prices)

print(list(lst))
d = {a.title(): b for a, b in zip(items, prices)}
print(d)

e = {item.title(): price for item, price in zip(items, prices)}
print(e)
