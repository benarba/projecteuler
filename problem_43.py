def get_next_perm(perm):
    pass_set = set()
    for i in range(len(perm) - 1):
        if perm[i] < perm[i + 1] and not pass_set:
            temp = perm[i]
            perm[i] = perm[i + 1]
            perm[i + 1] = temp
            break
        elif perm[i] > perm[i + 1]:
            pass_set.add(perm[i])
        elif perm[i] < perm[i + 1]:
            pass_set.add(perm[i])
            cand = max({x for x in pass_set if x < perm[i + 1]})
            pass_set.remove(cand)
            pass_set.add(perm[i + 1])
            l = list(pass_set)
            l.sort()
            perm = l + [cand] + perm[i + 2 :]
            break
    return perm


def is_special(perm):
    for i in range(len(divisors)):
        k = i + 1
        subp = int("".join(perm[k : k + 3]))
        divisor = int(divisors[i])
        if subp % divisor != 0:
            return False
    return True


# tests = "1406357289"

ds = "0123456789"
digits = list(ds)

divisors = [2, 3, 5, 7, 11, 13, 17]

sm = 0
while True:
    if is_special(digits):
        sm += int("".join(digits))
    digits = get_next_perm(digits)

    if "".join(digits) == "9876543210":
        break

print(sm)
