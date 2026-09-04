text = "AABAACAADAABAABA"
pattern = "AABA"

positions = []
comparisons = 0

for i in range(len(text) - len(pattern) + 1):
    match = True

    for j in range(len(pattern)):
        comparisons += 1

        if text[i + j] != pattern[j]:
            match = False
            break

    if match:
        positions.append(i)

print("Pattern occurs at positions:", positions)
print("Total number of comparisons =", comparisons)
