import math


def combinations_count(n, r):
    return math.factorial(n) / (math.factorial(r) * math.factorial(n - r))


counter = 0

for i in range(2, 101):
    for j in range(1, i):
        comb_count = combinations_count(i, j)
        if comb_count > 1_000_000:
            counter += 1

print(f"answer: {counter}")
