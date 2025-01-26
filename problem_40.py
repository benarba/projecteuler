p = 1
for i in range(7):
    l = 0
    j = 1
    n = 10**i
    while l < n:
        if l + len(str(j)) >= n and l < n:
            nsj = n - l
            d = list(str(j))[nsj - 1]
            print(d, n, l, j, nsj)
            p *= int(d)
            break
        l += len(str(j))
        j += 1

print(p)
