import heapq

def prim(n, start, edges):
    graph = [[] for _ in range(n)]

    for u, v, w in edges:
        graph[u].append((w, v))
        graph[v].append((w, u))

    visited = [False] * n
    pq = [(0, start)]
    mst = []
    total = 0

    while pq:
        w, u = heapq.heappop(pq)

        if visited[u]:
            continue

        visited[u] = True

        if u != start:
            mst.append((parent, u, w))
            total += w
            print("Step", len(mst), ": Add", (parent, u, w))

        for weight, v in graph[u]:
            if not visited[v]:
                parent = u
                heapq.heappush(pq, (weight, v))

    print("MST edges:", mst)
    print("Total weight:", total)


n = 4
start = 0
edges = [
    (0, 1, 10),
    (0, 2, 6),
    (0, 3, 5),
    (1, 3, 15),
    (2, 3, 4)
]

prim(n, start, edges)
