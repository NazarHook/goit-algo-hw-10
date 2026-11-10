import timeit

COINS = [50, 25, 10, 5, 2, 1]


def find_coins_greedy(amount):
    """Жадібний алгоритм: беремо найбільші монети, поки вони вміщуються в суму."""
    result = {}
    for coin in COINS:
        count = amount // coin
        if count > 0:
            result[coin] = count
            amount = amount - count * coin
    return result


def find_min_coins(amount):
    """Динамічне програмування: min_count[s] це мінімум монет для суми s."""
    min_count = [0] + [amount + 1] * amount
    last_coin = [0] * (amount + 1)

    for s in range(1, amount + 1):
        for coin in COINS:
            if coin <= s and min_count[s - coin] + 1 < min_count[s]:
                min_count[s] = min_count[s - coin] + 1
                last_coin[s] = coin

    # відновлюємо набір монет, рухаючись від суми до нуля
    result = {}
    s = amount
    while s > 0:
        coin = last_coin[s]
        result[coin] = result.get(coin, 0) + 1
        s = s - coin

    return dict(sorted(result.items()))


def main():
    amount = 113
    print("Жадібний алгоритм для 113:", find_coins_greedy(amount))
    print("Динамічне програмування для 113:", find_min_coins(amount))

    print()
    print("Сума | жадібний, с | динамічне, с")
    for amount, runs in [(113, 1000), (1000, 100), (10000, 10), (100000, 3), (1000000, 1)]:
        greedy_time = timeit.timeit(lambda: find_coins_greedy(amount), number=runs) / runs
        dp_time = timeit.timeit(lambda: find_min_coins(amount), number=runs) / runs
        print(f"{amount:>7} | {greedy_time:>11.7f} | {dp_time:>12.7f}")


if __name__ == "__main__":
    main()
