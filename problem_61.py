def get_triangle(n):
    all_nz = [int(i * (i + 1) / 2) for i in range(1, n)]
    all_n = [x for x in all_nz if int(x / 10) % 10 != 0]
    return [i for i in all_n if i >= 1_000 and i < 10_000]


def get_square(n):
    all_nz = [i * i for i in range(1, n)]
    all_n = [x for x in all_nz if int(x / 10) % 10 != 0]
    return [i for i in all_n if i >= 1_000 and i < 10_000]


def get_penta(n):
    all_nz = [int(i * (i * 3 - 1) / 2) for i in range(1, n)]
    all_n = [x for x in all_nz if int(x / 10) % 10 != 0]
    return [i for i in all_n if i >= 1_000 and i < 10_000]


def get_hexa(n):
    all_nz = [int(i * (i * 2 - 1)) for i in range(1, n)]
    all_n = [x for x in all_nz if int(x / 10) % 10 != 0]
    return [i for i in all_n if i >= 1_000 and i < 10_000]


def get_hepta(n):
    all_nz = [int(i * (i * 5 - 3) / 2) for i in range(1, n)]
    all_n = [x for x in all_nz if int(x / 10) % 10 != 0]
    return [i for i in all_n if i >= 1_000 and i < 10_000]


def get_octa(n):
    all_nz = [int(i * (i * 3 - 2)) for i in range(1, n)]
    all_n = [x for x in all_nz if int(x / 10) % 10 != 0]
    return [i for i in all_n if i >= 1_000 and i < 10_000]


numbers = []
numbers.append(get_triangle(200))
numbers.append(get_square(200))
numbers.append(get_penta(200))
numbers.append(get_hexa(200))
numbers.append(get_hepta(200))
numbers.append(get_octa(200))


levels = set([i for i in range(len(numbers))])
totals = set()


def dfs(used_levels=set(), prev=0, total=0, start=0):
    for i in levels - used_levels:
        if not used_levels:
            for c in numbers[i]:
                dfs(used_levels | {i}, c, total + c, c)
        elif len(used_levels) == 5:
            for c in numbers[i]:
                if prev % 100 == int(c / 100) and c % 100 == int(start / 100):
                    totals.add(total + c)
        else:
            for c in numbers[i]:
                if prev % 100 == int(c / 100):
                    dfs(used_levels | {i}, c, total + c, start)


dfs()
print(totals)
