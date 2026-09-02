def distribute_prizes(participants):
    for i in range(len(participants)):
        max_index = i

        for j in range(i + 1, len(participants)):
            if participants[j][1] > participants[max_index][1]:
                max_index = j

        participants[i], participants[max_index] = \
            participants[max_index], participants[i]

    return participants


participants = [
    ("Asha", 88),
    ("Ravi", 95),
    ("Meera", 79),
    ("Dev", 95)
]

ranking = distribute_prizes(participants)

for name, score in ranking:
    print(name, score)
