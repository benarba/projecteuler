power = 7830457
p = 28433

while power > 0:
    if power >= 100:
        p *= 2**100 % (10**10)
        power -= 100
    else:
        p *= 2**power % (10**10)
        power = 0


print((p + 1) % (10**10))
