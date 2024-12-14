factor = [[0 for _ in range(21)] for _ in range(21)]
for i in range(2, 21):
    j = 2
    n = i
    while j <= n:
        if n == 1:
            break
        elif n % j == 0:
            n = n / j
            factor[i][j] += 1
        else:
            j += 1

max = [0 for _ in range(21)]
for r in factor:
    for i in range(len(r)):
        if r[i] > max[i]:
            max[i] = r[i]

product = 1
for i in range(1, len(max)):
    if max[i] > 0:
        for j in range(max[i]):
            product *= i

print(product)
