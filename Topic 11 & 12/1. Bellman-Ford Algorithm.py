def bellman_ford(vertices, edges, source):
    distance = [float('inf')] * vertices
    distance[source] = 0

    for _ in range(vertices - 1):
        for u, v, weight in edges:
            if distance[u] != float('inf') and distance[u] + weight < distance[v]:
                distance[v] = distance[u] + weight

    for u, v, weight in edges:
        if distance[u] != float('inf') and distance[u] + weight < distance[v]:
            print("Negative Weight Cycle Detected")
            return

    print("Vertex Distance")
    for i in range(vertices):
        print(i, distance[i])


edges = [(0, 1, -1), (0, 2, 4), (1, 2, 3),
         (1, 3, 2), (1, 4, 2), (3, 2, 5),
         (3, 1, 1), (4, 3, -3)]

bellman_ford(5, edges, 0)
