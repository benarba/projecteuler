from fractions import Fraction

N = 10**7
n = list(range(N))

for i in range(2, N):
    if n[i] == i:
        for j in range(i, N, i):
            n[j] -= n[j] // i

min_tot = Fraction(10**8, 1)
min_n = -1
for i in range(2, N):
    tot = Fraction(i, n[i])
    if tot < min_tot and sorted(str(i)) == sorted(str(n[i])):
        min_tot = tot
        min_n = i

print(min_n)
