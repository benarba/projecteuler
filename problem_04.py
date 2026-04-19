def is_pal(num):
    num = str(num)
    return num == num[::-1]


largest_pal = 1
for i in range(999, 99, -1):
    for j in range(999, 99, -1):
        product = i * j
        if is_pal(product) and product > largest_pal:
            largest_pal = product

print(largest_pal)
