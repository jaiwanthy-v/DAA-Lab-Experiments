text = "COMPUTERSCIENCE"
pattern = "SCI"

comparisons = 0
found = False

for i in range(len(text) - len(pattern) + 1):
    for j in range(len(pattern)):
        comparisons += 1

        if text[i + j] != pattern[j]:
            break
    else:
        print("First occurrence position =", i)
        print("Number of comparisons =", comparisons)
        found = True
        break

if not found:
    print("Pattern not found")
