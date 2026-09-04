arr = [5, 10, 15, 20, 25, 30, 35]
key = 18
comparisons = 0
found = False

for i in range(len(arr)):
    comparisons += 1
    if arr[i] == key:
        print("Element found at position", i + 1)
        found = True
        break

if not found:
    print("Element not found")

print("Number of comparisons =", comparisons)
