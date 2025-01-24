n = 200
cs = [200, 100, 50, 20, 10, 5, 2, 1]
combos = []


def get_combinations(
    i,
    sum,
):
    if i >= len(cs):
        return
    m = int(n / cs[i]) + 1
    for j in range(m):
        csum = sum + j * cs[i]
        if csum == n:
            combos.append(1)
            break
        elif csum > n:
            break
        get_combinations(i + 1, csum)


get_combinations(0, 0)
print(len(combos))
