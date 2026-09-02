arr = [45, 23, 67, 12, 89, 34, 56, 78, 90, 11,
       29, 73, 18, 64, 37]

keys = [73, 18, 100]

for key in keys:
    comparisons = 0
    found = False

    print("\nSearching for:", key)

    for i in range(len(arr)):
        comparisons += 1
        print("Compare", arr[i], "with", key)

        if arr[i] == key:
            found = True
            break

    if found:
        print("Element found at position", i + 1)
    else:
        print("Element not found")

    print("Comparisons =", comparisons)

print("\nBest-case complexity: O(1)")
print("Average-case complexity: O(n)")
print("Worst-case complexity: O(n)")
print("Space complexity: O(1)")
