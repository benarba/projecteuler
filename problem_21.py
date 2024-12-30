import math


def get_devisors_sum(n):
    sum = 0
    for i in range(1, int(math.ceil(n / 2) + 1)):
        if n % i == 0:
            sum += i
    return sum


sum = 0

for i in range(1, 10_000):
    a = get_devisors_sum(i)
    if get_devisors_sum(a) == i and i != a:
        sum += i

print(sum)
