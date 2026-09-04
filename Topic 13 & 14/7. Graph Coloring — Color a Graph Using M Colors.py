def is_safe(vertex, color, graph, colors, n):
    for i in range(n):
        if graph[vertex][i] == 1 and colors[i] == color:
            return False
    return True


def graph_coloring(vertex, n, m, graph, colors):
    if vertex == n:
        return True

    for color in range(1, m + 1):
        if is_safe(vertex, color, graph, colors, n):
            colors[vertex] = color

            if graph_coloring(vertex + 1, n, m, graph, colors):
                return True

            colors[vertex] = 0

    return False


n = 4
m = 3

graph = [
    [0, 1, 1, 1],
    [1, 0, 1, 0],
    [1, 1, 0, 1],
    [1, 0, 1, 0]
]

colors = [0] * n

if graph_coloring(0, n, m, graph, colors):
    for i in range(n):
        print("Vertex", i, "→ Color", colors[i])
else:
    print("No valid coloring possible")
