def insertion_sort_count_shifts(arr):
    shifts = 0

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            shifts += 1
            j -= 1

        arr[j + 1] = key

    return arr, shifts


log = [18.2, 18.5, 18.9, 17.9, 19.1, 19.4, 19.0]

result, shifts = insertion_sort_count_shifts(log)

print("Sorted Sensor Log:", result)
print("Number of Shifts:", shifts)
