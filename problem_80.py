from decimal import Decimal, getcontext

getcontext().prec = 150


s = 0
for i in range(1, 101):
    k = Decimal(i).sqrt()

    if k % 1 == 0:
        continue
    s += sum([int(x) for x in list(str(k).replace(".", "")[:100])])


print(s)
