n = int(input())
coin_count = 0

coins = [500, 100, 50, 10]

for coin in coins:
    coin_count += n // coin
    n %= coin

print(coin_count)
