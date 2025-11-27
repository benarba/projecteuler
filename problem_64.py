def bot_to_top(r, bias, factor):
    denom = r - bias**2
    return r, -bias, 1, denom / factor


def get_bias(r, bias, denom):
    b = 0
    while True:
        if (r**0.5 + bias - b) / denom < 1:
            return b
        b += denom


def extract_and_top_to_bot(r, bias, denom):
    b = get_bias(r, bias, denom)
    return r, bias - b, denom, b / denom


def root(n, l):
    seq_start = int(n**0.5)
    bias = -seq_start
    r = n
    factor = 1
    seqis = []

    seq_len = {}
    length = -1
    for i in range(l):
        r, bias, factor, denom = bot_to_top(r, bias, factor)
        r, bias, denom, seqi = extract_and_top_to_bot(r, bias, denom)
        factor = denom
        seqis.append(seqi)
        key = str(bias) + str(factor)
        if key in seq_len:
            length = i - seq_len[key]
            return length
        else:
            seq_len[key] = i

    raise Exception(f"seq length was not found (n, l): {n}, {l}")


counter = 0
for i in range(2, 10_001):
    if i**0.5 % 1 != 0:
        r = root(i, 1000)
        if r % 2 == 1:
            counter += 1
print(counter)
