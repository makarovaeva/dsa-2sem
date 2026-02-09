import time
import tracemalloc


def solve(prices):
    n = len(prices)
    INF = 10 ** 9

    # купонов не может быть больше n
    max_coupons = n + 1

    dp = [[INF] * max_coupons for _ in range(2)]
    parent = [[(-1, -1)] * max_coupons for _ in range(n + 1)]

    dp[0][0] = 0
    current = 0

    for i in range(n):
        next_idx = 1 - current
        price = prices[i]

        # Инициализируем следующий слой
        for j in range(max_coupons):
            dp[next_idx][j] = INF

        for j in range(max_coupons):
            if dp[current][j] == INF:
                continue

            # Вариант 1: Платим
            new_j = j + (price > 100)
            if new_j < max_coupons:
                new_cost = dp[current][j] + price
                if new_cost < dp[next_idx][new_j]:
                    dp[next_idx][new_j] = new_cost
                    parent[i + 1][new_j] = (j, 0)  # 0 - платил

            # Вариант 2: Используем купон
            if j > 0:
                new_cost = dp[current][j]
                if new_cost < dp[next_idx][j - 1]:
                    dp[next_idx][j - 1] = new_cost
                    parent[i + 1][j - 1] = (j, 1)  # 1 - использовал купон

        current = next_idx

    # Находим лучший результат
    min_cost = INF
    best_j = 0

    for j in range(max_coupons):
        if dp[current][j] < min_cost:
            min_cost = dp[current][j]
            best_j = j
        elif dp[current][j] == min_cost and j > best_j:
            best_j = j

    # Восстанавливаем ответ
    used_days = []
    current_j = best_j

    for i in range(n, 0, -1):
        prev_j, action = parent[i][current_j]
        if prev_j == -1:
            continue

        if action == 1:
            used_days.append(i)

        current_j = prev_j

    used_days.sort()
    k1 = best_j
    k2 = len(used_days)

    return min_cost, k1, k2, used_days

def main():
    with open("input.txt") as inp:
        n = int(inp.readline())
        prices = [int(inp.readline()) for _ in range(n)]
    min_cost, k1, k2, used_days = solve(prices)
    with open("output.txt", "w") as out:
        out.write(f"{min_cost}\n{k1} {k2}\n")
        out.write("\n".join(map(str, used_days)))

if __name__ == "__main__":
    t_start = time.time()
    main()
    print(f"Время работы программы: {time.time() - t_start}")
    tracemalloc.start()
    main()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    print(f"Текущий объем памяти: {current / 2 ** 20} Mбайт, максимальный объем выделенной памяти: {peak / 2 ** 20} Mбайт\n")




