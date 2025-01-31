import math


def is_prime(n):
    if n == 2:
        return True
    elif n < 2 or n % 2 == 0:
        return False
    else:
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
    return True


def dist_digits(n):
    s = {c for c in list(str(n))}
    return len(s)


def group_index(n):
    l = list(str(n))
    l.sort()
    return tuple(l)


prime_groups = {}
for n in range(1_000, 10_000):
    if is_prime(n):
        key = group_index(n)
        prime_groups.setdefault(key, []).append(n)


filtered_groups = {k: v for k, v in prime_groups.items() if len(v) >= 3}

for k, v in filtered_groups.items():
    for i in range(len(v) - 2):
        for j in range(i + 1, len(v) - 1):
            for m in range(j + 1, len(v)):
                if v[m] - v[j] == v[j] - v[i]:
                    print(str(v[i]), str(v[j]), str(v[m]))
                    print(str(v[i]) + str(v[j]) + str(v[m]))
