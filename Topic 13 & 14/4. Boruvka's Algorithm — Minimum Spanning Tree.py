def boruvka(n, edges):
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
    components = n
    first_pass = True

    while components > 1:
        cheapest = [None] * n

        for u, v, w in edges:
            set_u = find(u)
            set_v = find(v)

            if set_u == set_v:
                continue

            if cheapest[set_u] is None or w < cheapest[set_u][2]:
                cheapest[set_u] = (u, v, w)

            if cheapest[set_v] is None or w < cheapest[set_v][2]:
                cheapest[set_v] = (u, v, w)

        if first_pass:
            print("Pass 1 cheapest edges:")

            for i in range(n):
                if cheapest[i] is not None:
                    print(
                        "Component {" + str(i) + "}: cheapest =",
                        cheapest[i]
                    )

            first_pass = False

        for i in range(n):
            edge = cheapest[i]

            if edge is not None:
                u, v, w = edge

                if union(u, v):
                    mst.append(edge)
                    total += w
                    components -= 1

        print("MST edges:", mst)
        print("Total weight:", total)


n = 4
edges = [
    (0, 1, 10),
    (0, 2, 6),
    (0, 3, 5),
    (1, 3, 15),
    (2, 3, 4)
]

boruvka(n, edges)
