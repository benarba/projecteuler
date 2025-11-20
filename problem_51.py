import math

unit_digits = {1, 3, 7, 9}
digits_to_replace = list(range(10))


def is_prime(n):
    if n < 3:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


def masking(n, m, d, mask_length):

    n_list = list(str(n))
    mask_str = format(m, f"0{mask_length}b")

    for i in range(len(mask_str)):
        if mask_str[i] == "1":
            n_list[i] = str(d)

    return "".join(n_list)


primes_list = []
for x in range(13, 1_000_000, 2):
    if is_prime(x):
        primes_list.append(x)

primes_set = set(primes_list)

solution_flag = False
for x in primes_list:
    mask_length = len(str(int(x / 10)))
    max_mask_bin = 2**mask_length
    max_mask_str = format(max_mask_bin, f"0{mask_length}b")

    for m in range(1, max_mask_bin):  # mask loop
        solution_set = set()
        for d in range(10):  # digit loop
            i = masking(x, m, d, mask_length)
            if i[0] != "0" and is_prime(int(i)):
                solution_set.add(int(i))

        if len(solution_set) >= 8:
            print(min(solution_set))
            solution_flag = True
            break
    if solution_flag:
        break
