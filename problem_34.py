def factorial(n):
    p = 1
    for i in range(1, n + 1):
        p *= i
    return p


ssm = 0
for n in range(3, 1_000_000_000):
    if n % 10_000_000 == 0:
        print(f"n: {n}")
    ln = list(str(n))
    sm = 0
    for d in ln:
        sm += factorial(int(d))
    if sm == n:
        ssm += n
        print(f"-- {n} -> {ssm}")
