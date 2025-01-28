def add_pens(d, n, p_set):
    while max(p_set) < d:
        n += 1
        p = get_pen(n)
        p_set.add(p)


def get_pen(n):
    return n * (3 * n - 1) // 2


pen_set = set()
i = 1
min_init = False
min_a = -1

while True:
    if i < 3:
        p = get_pen(i)
        pen_set.add(p)
        i += 1

    else:
        p = get_pen(i)
        pen_set.add(p)
        l1 = len(pen_set)
        add_pens(p * 2, i, pen_set)
        for j in range(1, i):
            pj = get_pen(j)
            a = p - pj
            d = p + pj
            if a in pen_set and d in pen_set:
                if not min_init:
                    min_a = a
                    min_init = True
                    print("--1", a, pj, p, d)
                elif a < min_a:
                    min_a = a
                    print("--2", a, pj, p, d)

        i += 1
