def get_next(n):
    sl = list(str(n))
    return sum([int(x) ** 2 for x in sl])


counter = 0
for i in range(1, 10**7):
    n = i
    while n not in [1, 89]:
        n = get_next(n)
    else:
        if n == 89:
            counter += 1


print(counter)
