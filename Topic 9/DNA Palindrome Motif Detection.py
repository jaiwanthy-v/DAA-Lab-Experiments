def lps_length(s):
    n = len(s)
    rev = s[::-1]

    dp = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if s[i - 1] == rev[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[n][n]


assert lps_length("bbbab") == 4
assert lps_length("cbbd") == 2
assert lps_length("") == 0

print("All test cases passed!")
