def int_plus_fraction(n, num, denom):
    return n * denom + num, denom


def get_bias(n, bias, denom):
    b = 0
    while True:
        if (n**0.5 + bias - b) / denom < 1 and b % denom == 0:
            return bias - b, b / denom
        b += denom


def move_root_to_top(n, bias):
    denom = n - bias**2
    bias = -bias
    return denom, bias


def get_seq(n):
    denom = 1
    num = 1
    bias = 0
    seq = []
    states = set()
    loop = 1
    while True:
        # print(f"loop: {loop}, denom: {denom}, num: {num}, bias: {bias}")
        bias, i = get_bias(n, bias, denom)
        num = denom
        denom, bias = move_root_to_top(n, bias)
        denom = denom / num
        num = 1

        state = str(bias) + "k" + str(denom)
        if state in states:
            return seq
        else:
            seq.append(int(i))
            hash = str(bias) + "k" + str(denom)
            states.add(hash)
        loop += 1


def get_fraction(i, seq):
    num = 0
    denom = 1

    new_seq = []
    nseq = seq[1:]
    ls = len(nseq)
    i -= 1
    new_seq.append(seq[0])
    new_seq.extend(nseq * int(i / ls))
    new_seq.extend(nseq[: i % ls])

    # print(new_seq)
    for i in reversed(new_seq):
        denom, num = int_plus_fraction(i, num, denom)
    return denom, num


m = 0
dm = 0
for d in range(2, 1001):
    dr = int(d**0.5)
    if dr**2 == d:
        continue
    for i in range(1, 1000):
        num, denom = get_fraction(i, get_seq(d))
        e = num**2 - d * denom**2
        if e == 1:
            if num > m:
                m = num
                dm = d
            break

print(dm)
