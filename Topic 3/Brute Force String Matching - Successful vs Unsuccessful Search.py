text = "PROGRAMMINGLAB"

patterns = ["LAB", "TEST"]

for pattern in patterns:
    comparisons = 0
    found = False

    for i in range(len(text) - len(pattern) + 1):
        for j in range(len(pattern)):
            comparisons += 1

            if text[i + j] != pattern[j]:
                break
        else:
            found = True
            break

    if found:
        print(pattern, "- Successful search")
    else:
        print(pattern, "- Unsuccessful search")

    print("Comparison count =", comparisons)
