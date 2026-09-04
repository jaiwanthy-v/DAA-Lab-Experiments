def optimized_bubble_sort(arr):
    passes = 0

    for i in range(len(arr)):
        swapped = False
        passes += 1

        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if not swapped:
            break

    return arr, passes


rolls = [101, 102, 104, 103, 105, 107, 106, 108]

result, passes = optimized_bubble_sort(rolls)

print("Sorted Roll Numbers:", result)
print("Passes:", passes)
