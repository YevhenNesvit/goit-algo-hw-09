def find_coins_greedy(amount):
    coins = [50, 20, 10, 5, 2, 1]  # доступні номінали монет
    coins_count = {}

    for coin in coins:
        if amount >= coin:
            coins_count[coin] = amount // coin
            amount %= coin

    return coins_count


def find_min_coins(amount):
    coins = [1, 2, 5, 10, 20, 50]  # доступні номінали монет
    coins_count = {}

    for coin in coins[::-1]:
        while amount >= coin:
            if coin not in coins_count:
                coins_count[coin] = 0
            coins_count[coin] += 1
            amount -= coin

    return coins_count


if __name__ == "__main__":
    print(find_coins_greedy(146))
    print(find_min_coins(146))
