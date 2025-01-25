def is_pali(sn):
    rsn = "".join(list(sn)[::-1])
    return sn == rsn


sm = 0
for n in range(1_000_000):
    if is_pali(str(n)) and is_pali(format(n, "b")):
        sm += n

print(sm)
