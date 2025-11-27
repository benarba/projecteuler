counter = 0
d = 1
for d in range(1, 10):
    for i in range(1, 100):
        if len(str(d**i)) == i:
            counter += 1

print(counter)
