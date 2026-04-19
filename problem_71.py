max_value = 0
max_nom = 0

for d in range(1, 1_000_001):
    n = int(d * 3 / 7)
    if n == d * 3 / 7:
        continue
    if n / d > max_value:
        max_value = n / d
        max_nom = n

print(max_nom)
