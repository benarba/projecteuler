import math


def is_prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


count = 1
n = 3
while count < 10_001:
    if is_prime(n):
        count += 1
        if count == 10_001:
            print(n)
    n += 2
