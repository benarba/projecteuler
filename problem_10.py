import math


def is_prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


sum = 0
n = 2_000_000
for i in range(2, n):
    if is_prime(i):
        sum += i

print(sum)
