def bubble_sort_queue(queue):
    priority = {
        "ambulance": 3,
        "bus": 2,
        "car": 1
    }

    for i in range(len(queue)):
        for j in range(len(queue) - 1 - i):
            if priority[queue[j]] < priority[queue[j + 1]]:
                queue[j], queue[j + 1] = queue[j + 1], queue[j]

    return queue


queue = ["car", "car", "bus"]
queue.append("ambulance")

print("Priority Queue:", bubble_sort_queue(queue))
