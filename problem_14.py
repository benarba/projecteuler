max = 0
max_n = 0
for i in range(1000_000):
    k = i
    count = 0
    while k > 1:
        if k % 2 == 0:
            k /= 2
        else:
            k = k * 3 + 1
        count += 1
    if count > max:
        max = count
        max_n = i

print(max_n, max)
