p_max = 0
p_max_sc = 0


for p in range(3, 1001):
    p_sc = 0
    for a in range(1, p):
        for b in range(1, p - a):
            c = p - a - b
            if a**2 + b**2 == c**2:
                p_sc += 1
    if p_sc > p_max_sc:
        p_max_sc = p_sc
        p_max = p

print(p_max)
