def int_plus_rational(i, n, d):
    return i * d + n, d


t = 1000

counter = 0
for i in range(t):
    n = 1
    d = 2
    for j in range(i + 1):
        if j == i:
            nn, dd = int_plus_rational(1, n, d)
            if len(str(nn)) > len(str(dd)):
                counter += 1
        else:
            d, n = int_plus_rational(2, n, d)

print(counter)
