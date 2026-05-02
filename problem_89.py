with open("0089_roman.txt", "r") as f:
    l = [x.strip() for x in f.readlines()]

N = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1_000,
}


R = {
    "I": 1,
    "V": 2,
    "X": 3,
    "L": 4,
    "C": 5,
    "D": 7,
    "M": 8,
}

NL = [1, 5, 10, 50, 100, 500, 1_000]
ANL = [0, 1, 1, 10, 10, 100, 100]
LL = ["I", "V", "X", "L", "C", "D", "M"]
ALL = ["K", "I", "I", "X", "X", "C", "C"]
RNL = list(reversed(NL))
RANL = list(reversed(ANL))
RLL = list(reversed(LL))
RALL = list(reversed(ALL))


def read_roman(n):
    s = 0
    for i in range(len(n)):
        if i + 1 == len(n):
            s += N[n[i]]
        elif N[n[i + 1]] > N[n[i]]:
            s -= N[n[i]]
        else:
            s += N[n[i]]
    return s


def write_roman(s):
    n = ""
    for i in range(len(LL)):
        # print("i:", i)
        while s >= RNL[i]:
            # print("while")
            n += RLL[i]
            s -= RNL[i]

        if s < RNL[i] and s >= RNL[i] - RANL[i]:
            # print("if")
            n += RALL[i] + RLL[i]
            s -= RNL[i] - RANL[i]

    return n


original_sum = sum([len(x) for x in l])
updated_sum = sum([len(write_roman(read_roman(x))) for x in l])


print(original_sum - updated_sum)
