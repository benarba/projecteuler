digits = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

combo = "".join(digits)


def next_perm(perm):
    i = 0
    pass_t = []
    perm = list(perm)
    while True:
        pass_t.append(perm[i])
        if perm[i] < perm[i + 1]:
            temp = perm[i + 1]

            candidate = [x for x in pass_t if x < perm[i + 1]]
            elected = max(candidate)
            candidate.remove(elected)
            perm[i + 1] = elected
            pass_t.append(temp)
            pass_t.remove(elected)
            pass_t.sort()
            next_p = pass_t + perm[i + 1 :]
            return "".join(next_p)
        i += 1


pandigital = set()
while combo != "987654321":
    for i in range(1, len(digits) - 2):
        for j in range(i + 1, len(digits) - 1):
            if int(combo[:i]) * int(combo[i:j]) == int(combo[j:]):
                pandigital.add(int(combo[j:]))
    combo = next_perm(combo)

print(sum(pandigital))
print(len(pandigital))
