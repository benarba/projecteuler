def factorial(d):
    p = 1
    for i in range(1, d + 1):
        p *= i
    return p


f = {}
for i in range(10):
    f[str(i)] = factorial(i)


chain_60_counter = 0
for m in range(1_000_000):
    n = m
    chain_set = {n}
    counter = 0
    while True:
        n = sum([f[d] for d in list(str(n))])
        counter += 1
        if n in chain_set:
            break
        chain_set.add(n)
    if counter == 60:
        chain_60_counter += 1


print(chain_60_counter)
