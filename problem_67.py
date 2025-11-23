with open("0067_triangle.txt", "r") as f:
    lines = [l.strip() for l in f.readlines()]

levels = []

for line in lines:
    levels.append([int(x) for x in line.split()])


prev_level = levels[0]
for i in range(1, len(levels)):
    next_level = levels[i]
    for j in range(len(next_level)):
        if j == 0:
            next_level[0] += prev_level[0]
        elif j == len(next_level) - 1:
            next_level[-1] += prev_level[-1]
        elif prev_level[j] > prev_level[j - 1]:
            next_level[j] += prev_level[j]
        else:
            next_level[j] += prev_level[j - 1]

    prev_level = next_level

print(max(prev_level))
