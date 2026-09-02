import time

def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i

        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


items = [499, 129, 899, 45, 275, 60, 310, 150]

start = time.perf_counter()

result = selection_sort(items)

end = time.perf_counter()

print("Sorted Prices:", result)
print("Execution Time:", end - start)
