sum = 0
first = 1
last = 1
while last < 4_000_000:
    temp = last
    last = last + first
    first = temp
    if last % 2 == 0:
        sum += last

print(sum)
