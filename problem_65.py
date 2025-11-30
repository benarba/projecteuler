import decimal

decimal.getcontext().prec = 200


def inverse(nom, denom):
    return denom, nom


def add_int_rational(n, nom, denom):
    return n * denom + nom, denom


def get_conv(n, seq):
    nom = 0
    denom = 1
    for i in reversed(range(n)):
        nom, denom = add_int_rational(seq[i], nom, denom)
        nom, denom = inverse(nom, denom)
    return denom, nom


e = decimal.Decimal(1).exp()

seq = []
for i in range(200):
    ie = int(e)
    seq.append(ie)
    e = 1 / (e - ie)

nom, denom = get_conv(100, seq)

print(sum([int(x) for x in list(str(nom))]))
