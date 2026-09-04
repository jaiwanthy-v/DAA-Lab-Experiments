def fractional_knapsack(weights, profits, capacity):
    items = []

    for i in range(len(weights)):
        ratio = profits[i] / weights[i]
        items.append((ratio, weights[i], profits[i]))

    items.sort(reverse=True)

    total_profit = 0

    for ratio, weight, profit in items:
        if capacity >= weight:
            capacity -= weight
            total_profit += profit
        else:
            total_profit += ratio * capacity
            break

    return total_profit


weights = [10, 20, 30]
profits = [60, 100, 120]
capacity = 50

print("Maximum profit =", fractional_knapsack(weights, profits, capacity))
