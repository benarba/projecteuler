permutation = 1_000_000
n = 10
factorial = 1

factorials = []
for i in range(1, n):
    factorial *= i
    factorials.append(factorial)

digits = [i for i in range(n)]
solution = []
for f in factorials[::-1]:
    if permutation == 0:
        break
    if permutation / f >= 1:
        shift = int(permutation / f)
        permutation %= f
        solution.append(digits.pop(shift))
    else:
        solution.append(digits.pop(0))

solution.extend(digits)

# reverse last permutation
for i in range(n - 1, 0, -1):
    if solution[i] < solution[i - 1]:
        prefix = solution[: i - 1]
        previous_power = max([x for x in solution[i:] if x < solution[i - 1]])
        prefix.append(previous_power)
        suffix = solution[i - 1 :]
        suffix.remove(previous_power)
        suffix.sort(reverse=True)
        fsolution = prefix + suffix
        print("".join([str(i) for i in fsolution]))
        break
