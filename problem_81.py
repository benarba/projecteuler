import numpy as np

with open("0081_matrix.txt", "r") as f:
    s = f.readlines()
    a = [[int(x) for x in line.strip().split(",")] for line in s]


a = np.array(a)

b = [[0 for _ in range(len(a[0]))] for _ in range(len(a))]
b = np.array(b)


b[0][0] = a[0][0]
for p in range(1, (len(a) - 1) * 2):
    # print("p: ", p)
    k = p % (len(a) - 1)
    start = min(k, p - k)
    end = max(k, p - k) + 1
    for i in range(start, end):
        j = p - i
        if i == 0:
            b[i][j] = b[i][j - 1] + a[i][j]
        elif j == 0:
            b[i][j] = b[i - 1][j] + a[i][j]
        else:
            b[i][j] = min(b[i][j - 1], b[i - 1][j]) + a[i][j]

b[-1][-1] = min(b[-1][-2], b[-2][-1]) + a[-1][-1]

print(b[-1][-1])
