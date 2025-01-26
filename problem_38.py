def is_pandigital(s):
    digits = {str(x) for x in range(1, 10)}
    ssn = set(s)
    return not bool(digits.difference(ssn))


for n in range(192, 1_000_000):
    sd = set()
    is_lt9 = True
    i = 1
    s = ""
    while is_lt9:
        s += str(n * i)
        if len(s) > 9:
            is_lt9 = False
        elif len(s) == 9 and i > 1 and is_pandigital(s):
            print(n, i, s)
            is_lt9 = False
        else:
            is_p = False
        i += 1
