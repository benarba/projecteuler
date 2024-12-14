n = 100

sum_of_squares = 0
sum = 0
for i in range(1, n + 1):
    sum_of_squares += i * i
    sum += i

print((sum * sum) - sum_of_squares)
