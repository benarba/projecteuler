def sum_digits(n):
    return sum([int(d) for d in list(str(n))])


m = 0

for a in range(1, 100):
    for b in range(1, 100):
        s = sum_digits(a**b)
        if s > m:
            m = s

print(m)
