n = 1_000_000
N = list(range(n + 1))

for i in range(2, n + 1):
    if N[i] == i:
        for j in range(i, n + 1, i):
            N[j] -= N[j] / i

print(sum(N[2:]))
