def rev_n(n):
    return int(str(n)[::-1])


def is_pal(n):
    return n == rev_n(n)


def is_lychrel(n):
    for _ in range(0, 50):
        if is_pal(n + rev_n(n)):
            return False
        else:
            n = n + rev_n(n)
    return True


counter = 0
for n in range(1, 10_000):
    if is_lychrel(n):
        counter += 1

print(counter)
