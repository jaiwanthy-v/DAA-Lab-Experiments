def first_fit_decreasing(items, capacity):
    items.sort(reverse=True)
    bins = []

    for item in items:
        placed = False

        for bin in bins:
            if sum(bin) + item <= capacity:
                bin.append(item)
                placed = True
                break

        if not placed:
            bins.append([item])

    return items, bins


capacity = 10
items = [2, 5, 4, 7, 1, 3, 8]

sorted_items, bins = first_fit_decreasing(items, capacity)

print("Sorted Items:")
print(sorted_items)

for i, bin in enumerate(bins, 1):
    print("Bin", i, ":", *bin)

print("Total Bins Used =", len(bins))
