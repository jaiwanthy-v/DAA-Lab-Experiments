def warshall(graph):
    n = len(graph)
    closure = [row[:] for row in graph]

    for i in range(n):
        closure[i][i] = 1

    for k in range(n):
        for i in range(n):
            for j in range(n):
                closure[i][j] = (
                    closure[i][j] or
                    (closure[i][k] and closure[k][j])
                )

    return closure


graph = [
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1],
    [0, 0, 0, 0]
]

result = warshall(graph)

for row in result:
    print(row)
