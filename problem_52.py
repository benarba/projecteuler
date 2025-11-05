# hash number
def has_number(n):
    n_set = set(str(n))
    h = hash(frozenset(n_set))
    return h


n = 10
while True:
    is_answer = True
    n1h = has_number(n)
    for i in range(2, 7):
        if has_number(n * i) != n1h:
            is_answer = False
            break
    if is_answer:
        print(f"answer: {n}")
        break

    n += 1
