text = "ABCDABCABCDA"
pattern = "ABCDA"

alignment = 1

for i in range(len(text) - len(pattern) + 1):
    print("Alignment", alignment)

    if text[i:i + len(pattern)] == pattern:
        print("Matching result: Match")
        print("Pattern occurrence position:", i)
    else:
        print("Matching result: Mismatch")

    alignment += 1
    print()
