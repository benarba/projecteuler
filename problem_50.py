def is_prime(n):
    if n == 2:
        return True
    elif n < 2 or n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


primes = []
for i in range(1_000_000):
    if is_prime(i):
        primes.append(i)

max_sum = 2
max_len = 1
max_list = [2]
for i in range(len(primes)):
    seq_sum = 0
    for j in range(i, len(primes)):

        seq_sum += primes[j]
        seq_len = j - i + 1

        if seq_sum % 2 == 0:
            continue

        if seq_sum > 1_000_000:
            break

        elif seq_len > max_len and is_prime(seq_sum):
            max_len = seq_len
            max_sum = seq_sum
            max_list = primes[i : j + 1]


print(max_sum)
print(max_len)
print(max_list)
