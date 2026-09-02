text = "TTATAGATCTCGTATTCTTTATAGATCTCCTATTCTT"
pattern = "TATCTT"

positions = []
comparisons = 0

for i in range(len(text) - len(pattern) + 1):
    print("Shift:", i)

    match = True

    for j in range(len(pattern)):
        comparisons += 1

        print("Compare", text[i + j], "with", pattern[j])

        if text[i + j] != pattern[j]:
            match = False
            break

    if match:
        positions.append(i)
        print("Match")
    else:
        print("Mismatch")

    print()

print("Pattern occurrences:", positions)
print("Total comparisons:", comparisons)

print("\nBest-case complexity: O(n)")
print("Worst-case complexity: O(nm)")
print("Space complexity: O(1)")
