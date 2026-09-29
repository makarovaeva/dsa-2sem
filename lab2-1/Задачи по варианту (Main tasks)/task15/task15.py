import time
import tracemalloc

def solve(s):
    n = len(s)
    dp = [[0] * n for _ in range(n)]
    # split[i][j] хранит точку разбиения для восстановления
    split = [[-1] * n for _ in range(n)]

    for length in range(1, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if length == 1:
                dp[i][j] = 0  # Один символ не может быть ПСП
                continue

            # Вариант 1: s[i] и s[j] являются парными
            if (s[i] == '(' and s[j] == ')') or \
                    (s[i] == '[' and s[j] == ']') or \
                    (s[i] == '{' and s[j] == '}'):
                dp[i][j] = (dp[i + 1][j - 1] if i + 1 <= j - 1 else 0) + 2
                split[i][j] = -2  # Маркер пары

            # Вариант 2: ищем лучшую точку разбиения
            for k in range(i, j):
                if dp[i][k] + dp[k + 1][j] > dp[i][j]:
                    dp[i][j] = dp[i][k] + dp[k + 1][j]
                    split[i][j] = k

    # Восстановление строки
    def get_result(i, j):
        if i > j: return ""
        if dp[i][j] == 0: return ""
        if split[i][j] == -2:
            return s[i] + get_result(i + 1, j - 1) + s[j]
        elif split[i][j] != -1:
            k = split[i][j]
            return get_result(i, k) + get_result(k + 1, j)
        else:
            return ""

    return get_result(0, n - 1)


def main():
    with open("input.txt") as inp, open("output.txt", "w") as out:
        data = inp.readline().strip()
        out.write(solve(data))


if __name__ == "__main__":
    t_start = time.time()
    main()
    print(f"Время работы программы: {time.time() - t_start}")
    tracemalloc.start()
    main()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    print(f"Текущий объем памяти: {current / 2 ** 20} Mбайт, максимальный объем выделенной памяти: {peak / 2 ** 20} Mбайт\n")


