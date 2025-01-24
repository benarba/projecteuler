uniq = set()

for a in range(2, 101):
    for b in range(2, 101):
        uniq.add(a**b)

print(len(uniq))
