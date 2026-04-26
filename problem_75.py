L = 1_500_000
m_limit = int((L / 2) ** 0.5)

factors = {1: set(), 2: {2}}
for i in range(3, m_limit):
    n = i
    j = 2
    while j < n and j < i**0.5 + 1:
        while n % j == 0:
            n = n // j
            if i in factors:
                factors[i].add(j)
            else:
                factors[i] = {j}
        j += 1

    if n > 1:
        if i in factors:
            factors[i].add(n)
        else:
            factors[i] = {n}


l_counts = [0 for _ in range(L + 1)]
for m in range(2, m_limit):
    for n in range(1 + (m % 2), m, 2):
        if not factors[m].intersection(factors[n]):
            a = m**2 - n**2
            b = 2 * m * n
            c = m**2 + n**2
            l = a + b + c
            for i in range(L // l + 1):
                l_counts[l * i] += 1

one_count = 0
for count in l_counts:
    if count == 1:
        one_count += 1

print(one_count)
