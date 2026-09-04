import heapq

def huffman_coding(characters, frequencies):
    heap = [[freq, char] for char, freq in zip(characters, frequencies)]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        new_node = [
            left[0] + right[0],
            left[1] + right[1]
        ]

        heapq.heappush(heap, new_node)

    codes = {}

    def generate_codes(node, code=""):
        if len(node[1]) == 1:
            codes[node[1]] = code
            return

        left_char = node[1][0]
        right_char = node[1][1]

        generate_codes([0, left_char], code + "0")
        generate_codes([0, right_char], code + "1")

    root = heap[0]

    def build_codes(node, code=""):
        if len(node[1]) == 1:
            codes[node[1]] = code
            return

        build_codes([0, node[1][0]], code + "0")
        build_codes([0, node[1][1]], code + "1")
      
    heap = [[freq, char] for char, freq in zip(characters, frequencies)]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        heapq.heappush(heap, [
            left[0] + right[0],
            left,
            right
        ])

    def create_codes(node, code=""):
        if len(node) == 2:
            codes[node[1]] = code
        else:
            create_codes(node[1], code + "0")
            create_codes(node[2], code + "1")

    codes = {}
    create_codes(heap[0])

    print("Huffman Codes:")
    for char in characters:
        print(char + ":", codes[char])


characters = ["a", "b", "c", "d", "e", "f"]
frequencies = [5, 9, 12, 13, 16, 45]

huffman_coding(characters, frequencies)
