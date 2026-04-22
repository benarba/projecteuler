import math


def get_factors_dict(n):
    factors_dict = {}
    factors_dict[1] = set()
    for k in range(2, n + 1):
        i = k
        j = 2
        f = set()
        while j <= i**0.5:
            if i % j == 0:
                i = i // j
                f.add(j)
                break
            j += 1
        if i not in factors_dict:
            factors_dict[i] = {i}
        else:
            factors_dict[k] = f.union(factors_dict[i])
    return factors_dict


N = 12_000

fs = get_factors_dict(N)

counter = 0
start = 1 / 3
end = 1 / 2
for d in range(4, N + 1):
    start_n = math.ceil(d * start)
    end_n = math.floor(d * end)
    for n in range(start_n, end_n + 1):
        d_set = fs[d]
        n_set = fs[n]
        if not d_set.intersection(n_set):
            counter += 1

print(counter)
