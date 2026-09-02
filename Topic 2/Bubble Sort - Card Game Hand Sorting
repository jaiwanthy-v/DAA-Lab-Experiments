def bubble_sort_hand(hand):
    passes = 0

    for i in range(len(hand)):
        swapped = False
        passes += 1

        for j in range(len(hand) - 1 - i):
            if hand[j] > hand[j + 1]:
                hand[j], hand[j + 1] = hand[j + 1], hand[j]
                swapped = True

        if not swapped:
            break

    return hand, passes


hand = [2, 4, 6, 8, 9, 11, 13]
hand.append(7)

result, passes = bubble_sort_hand(hand)

print("Sorted Hand:", result)
print("Passes:", passes)
