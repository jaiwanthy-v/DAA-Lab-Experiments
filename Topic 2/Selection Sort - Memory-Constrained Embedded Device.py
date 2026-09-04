def selection_sort_min_writes(arr):
    swaps = 0

    for i in range(len(arr)):
        min_index = i

        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j

        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
            swaps += 1

    return arr, swaps


readings = [23.5, 19.2, 25.1, 18.8, 21.4]

result, swaps = selection_sort_min_writes(readings)

print("Sorted Temperature Readings:", result)
print("Number of Swaps:", swaps)
print("Maximum Possible Swaps:", len(result) - 1)
