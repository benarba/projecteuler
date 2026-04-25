def count_sums(N):
    memo = {}

    def helper(r, n):
        if r == 0:
            return 1
        if n > r or n >= N:
            return 0
        total = 0
        i = 0
        while n * i <= r:
            if (r - n * i, n + 1) in memo:
                total += memo[(r - n * i, n + 1)]
            else:
                total += helper(r - n * i, n + 1)
            i += 1
        memo[(r, n)] = total
        return total

    return helper(N, 1)


print(count_sums(100))
