n = 20
l = [1 for _ in range(n)]

sum = 1
for i in range(n):
    row_sum = 0
    for j in range(n):
        sum += l[j]
        row_sum += l[j]
        l[j] = row_sum

print(sum)
