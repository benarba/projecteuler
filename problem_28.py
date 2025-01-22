sum = 1
for i in range(3, 1002, 2):
    sum += i**2 * 4 - (i - 1) * 6

print(sum)
