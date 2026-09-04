def is_safe(vertex, pos, path, graph):
    if graph[path[pos - 1]][vertex] == 0:
        return False

    if vertex in path:
        return False

    return True


def hamiltonian_cycle(pos, path, graph, n):
    if pos == n:
        return graph[path[pos - 1]][path[0]] == 1

    for vertex in range(1, n):
        if is_safe(vertex, pos, path, graph):
            path[pos] = vertex

            if hamiltonian_cycle(pos + 1, path, graph, n):
                return True

            path[pos] = -1

    return False


n = 5

graph = [
    [0, 1, 0, 1, 0],
    [1, 0, 1, 1, 1],
    [0, 1, 0, 0, 1],
    [1, 1, 0, 0, 1],
    [0, 1, 1, 1, 0]
]

path = [-1] * n
path[0] = 0

if hamiltonian_cycle(1, path, graph, n):
    print("Hamiltonian Cycle Exists:")
    print(" → ".join(map(str, path + [path[0]])))
else:
    print("Hamiltonian Cycle Does Not Exist")
