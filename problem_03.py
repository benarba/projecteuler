import math

n = 600851475143

ns = int(math.sqrt(n))
max_prime = 1

for i in range(1, ns):
    if n % i == 0:
        max_prime = i
        n = n / i


print(max_prime)
print(n)
