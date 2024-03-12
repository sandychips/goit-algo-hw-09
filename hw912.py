from faker import Faker
import time

# Жадібний алгоритм
def find_coins_greedy(amount):
    coins = [50, 25, 10, 5, 2, 1]
    result = {}
    for coin in coins:
        num_coin = amount // coin
        amount -= num_coin * coin
        if num_coin > 0:
            result[coin] = num_coin
    return result

# Алгоритм динамічного програмування
def find_min_coins(amount):
    coins = [1, 2, 5, 10, 25, 50]
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    result = {}
    for i in range(len(coins) - 1, -1, -1):
        while amount >= coins[i] and dp[amount] == dp[amount - coins[i]] + 1:
            if coins[i] in result:
                result[coins[i]] += 1
            else:
                result[coins[i]] = 1
            amount -= coins[i]
    return result

# Функція для вимірювання часу виконання та виведення результатів
def measurement(amounts):
    for amount in amounts:
        start_time_greedy = time.time()
        find_coins_greedy(amount)
        end_time_greedy = time.time()
        time_greedy = end_time_greedy - start_time_greedy
        print(f"Жадібний алгоритм для суми {amount}:")
        print("Кількість монет:", find_coins_greedy(amount))
        print("Час виконання:", "{:.9f}".format(time_greedy))
        print()

        start_time_dynamic = time.time()
        find_min_coins(amount)
        end_time_dynamic = time.time()
        time_dynamic = end_time_dynamic - start_time_dynamic
        print(f"Алгоритм динамічного програмування для суми {amount}:")
        print("Кількість монет:", find_min_coins(amount))
        print("Час виконання:", "{:.9f}".format(time_dynamic))
        print()
        

# Вказані суми для обчислення
amounts = [75, 1980, 10560, 15820]

# Виклик функції для вимірювання та виведення результатів
measurement(amounts)
