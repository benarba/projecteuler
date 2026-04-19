n = 1000
for i in range(1, n - 1):
    for j in range(1, n - i):
        k = 1000 - i - j
        if i * i + j * j == k * k:
            print(f"i: {i}, j: {j}, k: {k}")
            print(i * j * k)
