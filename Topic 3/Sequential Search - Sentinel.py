arr = [14, 9, 22, 35, 18, 41, 27]
key = 18

last = arr[-1]
arr[-1] = key

i = 0
comparisons = 0

while arr[i] != key:
    i += 1
    comparisons += 1

arr[-1] = last

if i < len(arr) - 1 or arr[-1] == key:
    print("Position found:", i + 1)
else:
    print("Element not found")

print("Comparison count =", comparisons + 1)
