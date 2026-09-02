def bubble_sort_with_frames(arr):
    frames = [arr.copy()]

    for i in range(len(arr)):
        swapped = False

        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        frames.append(arr.copy())

        if not swapped:
            break

    return frames


arr = [5, 1, 4, 2, 8]

frames = bubble_sort_with_frames(arr)

for i, frame in enumerate(frames):
    print("Pass", i, ":", frame)
