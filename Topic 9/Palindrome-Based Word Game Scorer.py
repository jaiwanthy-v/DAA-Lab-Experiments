def palindrome_score(s):
    n = len(s)

    if n == 0:
        return 0

    prev = [0] * n

    for i in range(n - 1, -1, -1):
        curr = [0] * n
        curr[i] = 1

        for j in range(i + 1, n):
            if s[i] == s[j]:
                curr[j] = prev[j - 1] + 2
            else:
                curr[j] = max(prev[j], curr[j - 1])

        prev = curr

    return prev[n - 1]


assert palindrome_score("bbbab") > palindrome_score("cbbd")
assert palindrome_score("a") == 1

print("All test cases passed!")
