import heapq

def dijkstra(n, source, edges):
    graph = [[] for _ in range(n)]

    for u, v, w in edges:
        graph[u].append((v, w))

    dist = [float('inf')] * n
    parent = [-1] * n
    dist[source] = 0

    pq = [(0, source)]

    while pq:
        d, u = heapq.heappop(pq)

        if d > dist[u]:
            continue

        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                parent[v] = u
                heapq.heappush(pq, (dist[v], v))

    def get_path(v):
        path = []
        while v != -1:
            path.append(v)
            v = parent[v]
        return path[::-1]

    print("Distances from 0:", dist)
    print("Path to 1:", " → ".join(map(str, get_path(1))))
    print("Path to 3:", " → ".join(map(str, get_path(3))))
    print("Path to 4:", " → ".join(map(str, get_path(4))))


n = 5
source = 0
edges = [
    (0, 1, 4),
    (0, 2, 1),
    (2, 1, 2),
    (1, 3, 1),
    (2, 3, 5),
    (3, 4, 3)
]

dijkstra(n, source, edges)
