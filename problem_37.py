import math


def is_prime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def is_t_prime(n):

    if not is_prime(n):
        return False

    sn = str(n)
    for i in range(1, len(sn)):
        left = sn[:i]
        right = sn[i:]
        if not is_prime(int(left)) or not is_prime(int(right)):
            return False
    return True


ctp = 0
sm = 0
i = 11
evens = {"0", "2", "4", "6", "8"}
while ctp < 11:

    if is_t_prime(i):
        sm += i
        print(ctp, i, sm)
        ctp += 1

    i += 2
