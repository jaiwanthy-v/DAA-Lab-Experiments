def pick_up_card(hand, card):
    i = len(hand) - 1
    hand.append(card)

    while i >= 0 and hand[i] > card:
        hand[i + 1] = hand[i]
        i -= 1

    hand[i + 1] = card

    return hand


hand = []

for card in [7, 2, 9, 4, 1]:
    hand = pick_up_card(hand, card)

print("Sorted Hand:", hand)
