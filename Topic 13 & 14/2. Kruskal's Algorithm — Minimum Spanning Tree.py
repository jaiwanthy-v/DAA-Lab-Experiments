def kruskal(n, edges):
    edges.sort(key=lambda x: x[2])

    parent = list(range(n))

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(a, b):
        a = find(a)
        b = find(b)

        if a != b:
            parent[b] = a
            return True

        return False

    mst = []
    total = 0

    for u, v, w in edges:
        if union(u, v):
            mst.append((u, v, w))
            total += w

    print("Edges in MST:", mst)
    print("Total weight of MST:", total)


n = 4
edges = [
    (0, 1, 10),
    (0, 2, 6),
    (0, 3, 5),
    (1, 3, 15),
    (2, 3, 4)
]

kruskal(n, edges)
