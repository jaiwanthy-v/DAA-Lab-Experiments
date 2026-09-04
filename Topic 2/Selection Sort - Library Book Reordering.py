def reorder_shelf(books):
    moves = 0

    for i in range(len(books)):
        min_index = i

        for j in range(i + 1, len(books)):
            if books[j] < books[min_index]:
                min_index = j

        if min_index != i:
            books[i], books[min_index] = books[min_index], books[i]
            moves += 1

    return books, moves


books = [305, 102, 250, 118, 199, 400, 101]

ordered, moves = reorder_shelf(books)

print("Ordered Book IDs:", ordered)
print("Number of Physical Moves:", moves)
