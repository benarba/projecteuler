sum = 0

for i in range(10_000_000):

    s = str(i)
    isum = 0
    for c in s:
        isum += int(c) ** 5
    if isum == i and i > 1:
        print(i)
        sum += i

print("===========")
print(sum)
