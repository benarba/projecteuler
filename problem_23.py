def get_divisors(n):
    divisors = []
    for i in range(1, int(n / 2) + 1):
        if n % i == 0:
            divisors.append(i)
    return divisors


def is_abundant(n):
    return sum(get_divisors(n)) > n


abundants = []
for i in range(1, 28124):
    if is_abundant(i):
        abundants.append(i)

abuns = set(abundants)
sum_nb = 0
for i in range(1, 28124):
    for j in range(len(abundants)):
        if abundants[j] >= i:
            sum_nb += i
            break
        elif i - abundants[j] in abuns:
            break

print(sum_nb)
