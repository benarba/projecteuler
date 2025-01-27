import math


def is_prime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


def get_perms(sln):
    perms = []

    def helper(lns, perm=""):
        if len(lns) == 1:
            perms.append(int(perm + lns[0]))
        else:
            for i in range(len(lns)):
                tmplns = lns.copy()
                tmpperm = str(perm)
                tmpperm += tmplns.pop(i)
                helper(tmplns, tmpperm)

    helper(sln)
    return perms


ln = list("987654321")

for i in range(len(ln) - 1):
    found_max = False
    for perm in get_perms(ln[i:]):
        if is_prime(perm):
            print(perm)
            found_max = True
            break

    if found_max:
        break
