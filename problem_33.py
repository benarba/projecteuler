"""
    4 2 digit rational numbers (nominator/denominator)
    find all of them
"""


def get_simplified_ratio(n, m):
    ln = list(str(n))
    lm = list(str(m))
    for i in range(len(ln)):
        for j in range(len(lm)):
            if ln[i] == lm[j]:
                nom = int("".join(ln[:i] + ln[i + 1 :]))
                den = int("".join(lm[:j] + lm[j + 1 :]))
                if nom * m == den * n and (n % 10 != 0 and m % 10 != 0):
                    print(f"{n}/{m} -> {nom}/{den}")
                    return nom, den
    return 1, 1


pnom = 1
pden = 1
for i in range(10, 99):
    for j in range(i + 1, 100):
        nom, den = get_simplified_ratio(i, j)
        pnom *= nom
        pden *= den


print(f"{pnom}/{pden}")
