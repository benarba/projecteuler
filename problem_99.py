import math

with open("0099_base_exp.txt", "r") as f:
    s = f.readlines()
    a = [[int(x) for x in line.strip().split(",")] for line in s]


# transform the base to 10 and multiply the exponents
m = 0
ind = -1
for i in range(len(a)):
    v = math.log10(a[i][0]) * a[i][1]
    if v > m:
        m = v
        ind = i + 1

print(ind)
