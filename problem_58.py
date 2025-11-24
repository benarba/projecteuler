def is_prime(n):
    if n < 3:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


prime_counter = 0
diag_counter = 1
diag = 1
for i in range(2, 1_000_000, 2):
    for j in range(4):
        diag += i
        diag_counter += 1
        if is_prime(diag):
            prime_counter += 1

    if prime_counter / diag_counter < 0.1:
        print(i + 1)
        break
