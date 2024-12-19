import math

s = str(int(math.pow(2, 1000)))

l = [int(x) for x in s]
print(sum(l))
