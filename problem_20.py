f = 1
for i in range(1, 101):
    f *= i

print(sum([int(x) for x in str(f)]))
