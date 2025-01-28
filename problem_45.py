def get_t(n):
    return n * (n + 1) // 2


def get_p(n):
    return n * (3 * n - 1) // 2


def get_h(n):
    return n * (2 * n - 1)


i = 143
tset = set()
pset = set()
hset = set()

ti = 1
tset.add(get_t(ti))
pi = 1
pset.add(get_p(pi))
hi = 143


while True:
    h = get_h(hi)
    hset.add(h)

    max_t = max(tset)
    while max_t < h:
        ti += 1
        t = get_t(ti)
        tset.add(t)
        max_t = t

    max_p = max(pset)
    while max_p < h:
        pi += 1
        p = get_p(pi)
        pset.add(p)
        max_p = p

    if h in tset and h in pset:
        print(h)
    hi += 1
