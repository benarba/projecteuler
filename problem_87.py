N = 50_000_000

primes = [i for i in range(N)]
for i in range(2, N):
    if i == primes[i]:
        for j in range(i * 2, N, i):
            primes[j] -= 1
    else:
        continue

triples = set()
for i in range(2, int(N ** (1 / 2)) + 1):
    if primes[i] != i:
        continue
    for j in range(2, int((N - i**2) ** (1 / 3)) + 1):
        if primes[j] != j:
            continue
        for k in range(2, int((N - i**2 - j**3) ** (1 / 4)) + 1):
            if primes[k] != k:
                continue
            if i**2 + j**3 + k**4 < N:
                triples.add(i**2 + j**3 + k**4)

print(len(triples))
