matrix = [
    [12, 8, 15],
    [5, 18, 27],
    [9, 11, 24]
]

key = 24
found = False

for i in range(3):
    for j in range(3):
        if matrix[i][j] == key:
            print("Element found at Row", i + 1, "Column", j + 1)
            found = True
            break
    if found:
        break
