def insert_updated_score(board, score):
    shifts = 0
    i = len(board) - 1

    board.append(score)

    while i >= 0 and board[i] < score:
        board[i + 1] = board[i]
        shifts += 1
        i -= 1

    board[i + 1] = score

    return board, shifts


board = [980, 875, 760, 690, 500]

result, shifts = insert_updated_score(board, 820)

print("Updated Leaderboard:", result)
print("Shifts:", shifts)
