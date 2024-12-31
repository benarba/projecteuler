prev = 0
current = 1

for i in range(2, 1_000_000):
    temp = current
    current += prev
    prev = temp
    if len(str(current)) >= 1000:
        print(i)
        break
