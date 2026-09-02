def top_k_scores(scores, k):
    result = []

    for i in range(k):
        if len(scores) == 0:
            break

        max_index = 0

        for j in range(1, len(scores)):
            if scores[j] > scores[max_index]:
                max_index = j

        result.append(scores[max_index])
        scores.pop(max_index)

    return result


scores = [72, 88, 65, 90, 77, 95, 60, 83, 91, 68]

top5 = top_k_scores(scores, 5)

print("Top 5 Scores:", top5)
