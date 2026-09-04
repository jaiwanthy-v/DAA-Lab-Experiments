def can_segment(s, word_dict):
    words = set(word_dict)
    n = len(s)

    dp = [False] * (n + 1)
    dp[0] = True

    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in words:
                dp[i] = True
                break

    return dp[n]


assert can_segment("leetcode", ["leet", "code"]) == True
assert can_segment("catsandog", ["cats", "dog", "sand", "and", "cat"]) == False

print("All test cases passed!")
