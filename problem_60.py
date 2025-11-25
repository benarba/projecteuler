def is_prime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def is_prime_pair(n, m):
    # return is_prime(int(str(n) + str(m))) and is_prime(int(str(m) + str(n)))
    return is_prime(int(str(n) + str(m))) and is_prime(int(str(m) + str(n)))


def is_prime_pair_map(n, m, map):
    return n in map[m] and m in map[n]


def is_prime_pair_set(prime_list, map):
    for i in range(len(prime_list) - 1):
        for j in range(i + 1, len(prime_list)):
            if not is_prime_pair_map(prime_list[i], prime_list[j], map):
                return False
    return True


print(f"get primes")
prime_list = []
for i in range(10_000):
    if is_prime(i):
        prime_list.append(i)


print("get prime pairs")
prime_pairs = []
for i in range(len(prime_list) - 1):
    for j in range(i + 1, len(prime_list)):
        if is_prime_pair(prime_list[i], prime_list[j]):
            prime_pairs.append([prime_list[i], prime_list[j]])

print(f"searchable mapping")
prime_pairs_map = {}
for pair in prime_pairs:
    if pair[0] not in prime_pairs_map:
        prime_pairs_map[pair[0]] = set([pair[1]])
    else:
        prime_pairs_map[pair[0]].add(pair[1])
    if pair[1] not in prime_pairs_map:
        prime_pairs_map[pair[1]] = set([pair[0]])
    else:
        prime_pairs_map[pair[1]].add(pair[0])


print("get prime fours")
prime_fours = []
prime_fours_set = set()
for i in range(len(prime_pairs) - 1):
    for j in range(i + 1, len(prime_pairs)):
        fours = prime_pairs[i] + prime_pairs[j]
        if is_prime_pair_set(fours, prime_pairs_map):
            fours_str = "".join([str(x) for x in sorted(fours)])
            if fours_str not in prime_fours_set:
                prime_fours.append(fours)
                prime_fours_set.add(fours_str)


print("get prime pair fives")
min = 10**100
for four in prime_fours:
    for prime in prime_list:
        if prime in four:
            continue
        is_five = True
        for i in four:
            if not is_prime_pair_map(prime, i, prime_pairs_map):
                is_five = False
                break
        if is_five:
            five = four + [prime]
            s = sum(five)
            if s < min:
                min = s


print(f"min sum: {min}")
