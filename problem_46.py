import math


def is_cube(n):
    return int(math.sqrt(n)) ** 2 == n


def is_prime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
    return True


primes_list = [2, 3]

n = 9
search = True
while search:
    if is_prime(n):
        n += 2
        continue

    max_prime_cand = primes_list[-1]
    while max_prime_cand < n:
        max_prime_cand += 2
        if max_prime_cand >= n:
            break
        if is_prime(max_prime_cand):
            primes_list.append(max_prime_cand)

    has_cube = False
    for prime in primes_list:
        if is_cube((n - prime) // 2):
            has_cube = True
            break

    if not has_cube:
        print(n)
        break

    n += 2
