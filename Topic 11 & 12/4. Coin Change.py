def coin_change(coins, amount):
    coins.sort(reverse=True)
    result = []

    for coin in coins:
        while amount >= coin:
            amount -= coin
            result.append(coin)

    return result


coins = [1, 2, 5, 10]
amount = 28

result = coin_change(coins, amount)

print(*result)
print("Minimum coins =", len(result))
