"""
n^2 + n + 41
0 -> 39 : prime numbers
n^2 - 79n + 1601
0 -> 79 : prime numbers

n^2 + an + b

when n = 0, b has to be prime
when n = 1, b is prime so be is odd, b + a + 1 has to be prime thus odd, prime (odd) - b (odd) - 1 (odd) = a (odd)
when n = 2, 4 + 2a + b (prime)

n (n + a) + b
"""

import math


def is_prime(n):
    if n < 0:
        n = n * (-1)
    if n == 1 or n == 0:
        return False
    if n == 2:
        return True
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def get_quad(a, b, n):
    return n**2 + a * n + b


max_n = 0
coef = 0
max_a = 0
max_b = 0
for b in range(-1000, 1001):
    if is_prime(b):
        for a in range(-999, 1000, 2):
            n = 0
            cons = True
            while cons:
                p = get_quad(a, b, n)
                if is_prime(p) and p > 0:
                    n += 1
                else:
                    cons = False
                    if n > max_n:
                        max_n = n
                        max_a = a
                        max_b = b
                        coef = b * a
                        print("------------------------------------------")
                        print(
                            f"max_n: {max_n}\na: {a}\nb: {b}\ncoef: {coef}\nn: {n}\np: {p}"
                        )
