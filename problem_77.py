def is_prime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def sum_count(N):

    primes = []
    for i in range(1, N):
        if is_prime(i):
            primes.append(i)

    cache_ = {}

    def helper(r, n):
        if r == 0:
            return 1
        if n >= len(primes):
            return 0
        if r < 0:
            return 0
        p = primes[n]
        i = 0
        total = 0
        while i * p <= N and n < len(primes):
            if (r - (i * p), n + 1) in cache_:
                total += cache_[(r - (i * p), n + 1)]
            else:
                total += helper(r - (i * p), n + 1)
            i += 1

        cache_[(r, n)] = total
        return total

    return helper(N, 0)


for i in range(10, 100):
    if sum_count(i) > 5_000:
        print(i)
        break
