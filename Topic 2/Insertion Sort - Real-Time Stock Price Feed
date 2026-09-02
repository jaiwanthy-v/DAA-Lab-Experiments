def insert_price(prices, price):
    i = len(prices) - 1
    prices.append(price)

    while i >= 0 and prices[i] > price:
        prices[i + 1] = prices[i]
        i -= 1

    prices[i + 1] = price

    return prices


prices = []

for p in [102.5, 98.3, 105.1, 100.0, 97.8]:
    prices = insert_price(prices, p)

print("Sorted Prices:", prices)
print("Minimum Price:", prices[0])
print("Maximum Price:", prices[-1])
