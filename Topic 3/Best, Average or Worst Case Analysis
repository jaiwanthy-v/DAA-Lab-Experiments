text = "AAAAAAAAAB"
pattern = "AAAAB"

comparisons = 0

for i in range(len(text) - len(pattern) + 1):
    for j in range(len(pattern)):
        comparisons += 1

        if text[i + j] != pattern[j]:
            break

print("Number of comparisons =", comparisons)
print("This represents a worst-case type search.")
