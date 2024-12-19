import math


def get_factors(n):
    k = n
    n_ = int(math.ceil(n / 2))
    d = 2
    factors = {}
    while k > 1:
        if k % d == 0:
            ds = str(d)
            if ds in factors:
                factors[ds] += 1
            else:
                factors[ds] = 1
            k /= d
        else:
            if d > n_ or d > k:
                break
            d += 1
    return factors


def get_divisors(factors):
    p = 1
    for key in factors:
        p *= factors[key] + 1
    return p


t = 0
max = 0
for i in range(1, 100_000):
    t += i
    factors = get_factors(t)
    count = get_divisors(factors)
    if count > 500:
        print(t)
        break
