import time
import tracemalloc


def solve(d):
    n = len(d)
    if n == 1:
        return "A"

    # Извлекаем размерности
    p = [d[0][0]]
    for rows, cols in d:
        p.append(cols)

    inf = 10 ** 18
    dp = [[0] * n for _ in range(n)]
    bracket = [[-1] * n for _ in range(n)]

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = inf

            for k in range(i, j):
                cost = dp[i][k] + dp[k + 1][j] + p[i] * p[k + 1] * p[j + 1]
                if cost < dp[i][j]:
                    dp[i][j] = cost
                    bracket[i][j] = k

    def build_parts(i, j):
        if i == j:
            return f"A"

        k = bracket[i][j]
        left = build_parts(i, k)
        right = build_parts(k + 1, j)

        # Добавляем скобки только если нужно
        if i != k or k + 1 != j:
            if i != k:
                left = f"({left})"
            if k + 1 != j:
                right = f"({right})"

        return f"{left}{right}"

    result = build_parts(0, n - 1)
    if n > 1:
        result = f"({result})"

    return result

def main():
    with open("input.txt") as inp:
        n = int(inp.readline())
        data = [list(map(int, inp.readline().split())) for _ in range(n)]
    result = solve(data)
    with open("output.txt", "w") as out:
        out.write(result)

if __name__ == "__main__":
    t_start = time.time()
    main()
    print(f"Время работы программы: {time.time() - t_start}")
    tracemalloc.start()
    main()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    print(f"Текущий объем памяти: {current / 2 ** 20} Mбайт, максимальный объем выделенной памяти: {peak / 2 ** 20} Mбайт\n")
