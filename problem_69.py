N = 1_000_000
n = list(range(N + 1))

for i in range(2, N + 1):
    if n[i] == i:
        for j in range(i, N + 1, i):
            n[j] -= n[j] // i

max_tot = 0
max_n = 0

for i in range(2, N + 1):
    tot = i / n[i]
    if tot > max_tot:
        max_tot = tot
        max_n = i

print(max_n)
