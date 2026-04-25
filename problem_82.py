import numpy as np

with open("0082_matrix.txt", "r") as f:
    s = f.readlines()


a = [[int(x) for x in line.strip().split(",")] for line in s]
a = np.array(a)
b = a.copy()

t = sum([sum(x) for x in a])
for j in range(1, len(a[0])):
    for i in range(len(a)):
        min_sum = t
        for k in range(len(a)):

            s = b[k, j - 1] + sum(a[min(k, i) : max(k, i) + 1, j])
            if s < min_sum:
                min_sum = s
        b[i][j] = min_sum

print(min(b[:, -1]))
