def vertex_cover(vertices, edges):
    cover = set()
    remaining_edges = edges[:]

    while remaining_edges:
        u, v = remaining_edges[0]

        cover.add(u)
        cover.add(v)

        remaining_edges = [
            edge for edge in remaining_edges
            if u not in edge and v not in edge
        ]

    return cover


vertices = 5
edges = [
    (0, 1),
    (0, 2),
    (1, 3),
    (2, 4)
]

cover = vertex_cover(vertices, edges)

print("Approximate Vertex Cover:")
print(cover)
print("Cover Size =", len(cover))
