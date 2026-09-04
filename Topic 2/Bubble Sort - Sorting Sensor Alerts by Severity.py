def bubble_sort_plain(arr):
    comparisons = 0

    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1 - i):
            comparisons += 1

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr, comparisons


def bubble_sort_optimized(arr):
    comparisons = 0

    for i in range(len(arr) - 1):
        swapped = False

        for j in range(len(arr) - 1 - i):
            comparisons += 1

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if not swapped:
            break

    return arr, comparisons


alerts = [2, 1, 3, 2, 1, 4, 3, 2, 5, 1, 2, 3, 4, 1, 2]

r1, c1 = bubble_sort_plain(alerts.copy())
r2, c2 = bubble_sort_optimized(alerts.copy())

print("Sorted Alerts:", r1)
print("Plain Comparisons:", c1)
print("Optimized Comparisons:", c2)
