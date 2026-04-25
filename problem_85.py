target = 2_000_000
limit = 2001
min_diff = target
min_area = -1
for n in range(1, limit):
    for m in range(n, limit):
        a = n * m * (n + 1) * (m + 1) // 4
        if abs(a - target) < min_diff:
            min_diff = abs(a - target)
            min_area = n * m

print(min_area)
