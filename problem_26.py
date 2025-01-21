def div_step(nom, den):

    if nom < den:
        return (nom * 10, 0)
    else:
        return (nom % den, int(nom / den))


max_len = 0
max_d = 0
for i in range(7, 1000):
    nom = 1
    den = i
    searching = True
    states = {}
    count = 1
    while searching:
        t = div_step(nom, den)
        nom, s = t
        # print(f"t: {t}")
        if t in states:
            # print(1)
            # print(i, 1 / i, count - states[t])
            l = count - states[t]
            if l > max_len:
                max_len = l
                max_d = i

            searching = False
        else:
            # print(2)
            states[t] = count
            count += 1
        # searching = False

print(max_d, max_len, 1 / max_d)
