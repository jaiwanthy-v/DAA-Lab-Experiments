def min_wrap_cost(words, width):
    n = len(words)
    dp = [float('inf')] * (n + 1)
    dp[n] = 0

    for i in range(n - 1, -1, -1):
        spaces = -1

        for j in range(i, n):
            spaces += words[j] + 1

            if spaces > width:
                break

            if j == n - 1:
                cost = 0
            else:
                extra = width - spaces
                cost = extra * extra

            dp[i] = min(dp[i], cost + dp[j + 1])

    return dp[0]


assert min_wrap_cost([3, 2, 2, 5], 6) == 19
assert min_wrap_cost([3], 6) == 0

print("All test cases passed!")
