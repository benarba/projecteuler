import math


def uniq_prime_divisors(n):
    prime_divisors = set()
    while n % 2 == 0:
        prime_divisors.add(2)
        n //= 2
    for d in range(3, int(math.sqrt(n)) + 1):
        while n % d == 0:
            prime_divisors.add(d)
            n //= d
    if n > 1:
        prime_divisors.add(n)
    return prime_divisors


def four_divisors(n):

    prime_divisors = uniq_prime_divisors(n)
    if len(prime_divisors) == 4:
        return True
    else:
        return False


i = 20
consecutive_set = set()

while True:
    if four_divisors(i):
        consecutive_set.add(i)
    else:
        consecutive_set = set()

    if len(consecutive_set) == 4:
        print(i, i - 1, i - 2, i - 3)
        break

    i += 1
