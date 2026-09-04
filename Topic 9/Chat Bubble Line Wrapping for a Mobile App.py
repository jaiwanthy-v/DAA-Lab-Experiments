def min_wrap_cost(words, width):
    n = len(words)
    dp = [float('inf')] * (n + 1)
    dp[n] = 0

    for i in range(n - 1, -1, -1):
        length = 0

        for j in range(i, n):
            length += words[j]

            if j > i:
                length += 1

            if length > width:
                break

            if j == n - 1:
                cost = 0
            else:
                extra = width - length
                cost = extra * extra

            dp[i] = min(dp[i], cost + dp[j + 1])

    return dp[0]


def wrap_lines(words, width):
    n = len(words)
    dp = [float('inf')] * (n + 1)
    choice = [-1] * n
    dp[n] = 0

    for i in range(n - 1, -1, -1):
        length = 0

        for j in range(i, n):
            length += words[j]

            if j > i:
                length += 1

            if length > width:
                break

            if j == n - 1:
                cost = 0
            else:
                extra = width - length
                cost = extra * extra

            if cost + dp[j + 1] < dp[i]:
                dp[i] = cost + dp[j + 1]
                choice[i] = j

    lines = []
    i = 0

    while i < n:
        j = choice[i]
        lines.append(words[i:j + 1])
        i = j + 1

    return lines


assert min_wrap_cost([3, 2, 2, 5], 6) == 19

lines = wrap_lines([3, 2, 2, 5], 6)
assert sum(len(line) for line in lines) == 4

print("All test cases passed!")
