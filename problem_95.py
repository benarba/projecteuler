def get_divisors(n):
    d = {1}
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            d.add(i)
            d.add(n // i)
    return d


print("Getting mapping...")
sumd = {}
il = []
for i in range(1, 1_000_000):
    s = sum(get_divisors(i))
    if s > 1 and s < 1_000_000 and s != i:
        sumd[i] = s
        il.append(i)

print("Done!")
print("Finding amicable chains...")

max_chain_len = 0
max_chain_set = []
for i in range(len(il)):
    sj = il[i]
    j = il[i]
    countr = 1
    chainset = [j]
    active_chain = True
    while sumd[j] in sumd and active_chain:
        j = sumd[j]
        countr += 1
        if j in chainset and j != sj:
            break
        chainset.append(j)
        if j == sj and countr > max_chain_len:
            max_chain_len = countr
            max_chain_set = chainset
            print(f"sj: {sj}")
            print(max_chain_set)
            print(max_chain_len)
            break
        elif j == sj:
            break
print(f"min number of longest chain: {min(max_chain_set)}")
