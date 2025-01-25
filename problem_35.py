import math

evens = {"0", "2", "4", "6", "8"}
pc = 4


def no_even_digit(n):
    ns = set(list(str(n)))
    if evens.intersection(ns):
        return False
    else:
        return True


def next_cycle_step(n):
    nl = list(str(n))
    return int("".join(nl[1:] + nl[:1]))


def is_prime(n):
    for i in range(3, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


for n in range(10, 1_000_000):
    if no_even_digit(n):
        k = n
        cycle_prime = True
        for i in range(len(str(n))):
            if not is_prime(k):
                cycle_prime = False
                break
            k = next_cycle_step(k)
        if cycle_prime:
            print(n)
            pc += 1

print(pc)
