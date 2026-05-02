import numpy as np

with open("0083_matrix.txt", "r") as f:
    m = np.array([[int(x) for x in line.strip().split(",")] for line in f.readlines()])

limit = 80
m = m[:limit, :limit]


def sum_min_path(m):
    n = len(m)
    initial = sum(m[0][j] for j in range(n)) + sum(m[i][n - 1] for i in range(1, n))
    min_sum = [initial]
    inter_sum = [[initial for _ in range(len(m[0]))] for _ in range(len(m))]

    def helper(i, j, s, done):
        if s < inter_sum[i][j]:
            inter_sum[i][j] = s
        else:
            return
        if s > min_sum[0]:
            return
        if i == j == len(m) - 1:
            if s < min_sum[0]:
                min_sum[0] = s
            return

        steps = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        valid_steps = []
        for step in steps:
            k = i + step[0]
            l = j + step[1]
            if 0 <= k < len(m) and 0 <= l < len(m):
                if (k, l) not in done:
                    valid_steps.append((k, l, m[k][l]))
        if not valid_steps:
            return
        valid_steps.sort(key=lambda x: x[2])

        done.add((i, j))
        for step in valid_steps:
            helper(
                step[0],
                step[1],
                s + step[2],
                done,
            )
        done.remove((i, j))

    helper(0, 0, m[0][0], {(0, 0)})
    return min_sum[0]


print(sum_min_path(m))
