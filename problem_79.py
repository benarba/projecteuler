with open("0079_keylog.txt", "r") as f:
    lines = f.readlines()
    seqs = [l.strip() for l in lines]

mat = [[0 for _ in range(10)] for _ in range(10)]
for seq in seqs:
    d = [int(x) for x in seq]
    mat[d[0]][d[1]] = 1
    mat[d[0]][d[2]] = 1
    mat[d[1]][d[2]] = 1


befores = []
afters = []
for i in range(len(mat)):
    before = []
    after = []
    for j in range(len(mat[0])):
        if mat[i][j]:
            after.append(j)
        elif mat[j][i]:
            before.append(j)

    befores.append(before)
    afters.append(after)

ordered = []

for j in range(len(mat)):
    min_i = 10
    min_l = 11
    for i in range(len(mat)):

        if ((not befores[i]) and (not afters[i])) or i in ordered:
            continue
        if len(befores[i]) < min_l:
            min_i = i
            min_l = len(befores[i])

    if min_i == 10:
        continue
    ordered.append(min_i)

print("".join([str(x) for x in ordered]))
