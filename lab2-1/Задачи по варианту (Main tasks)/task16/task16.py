import time
import tracemalloc


def solve(n, data):
    INF = 10 ** 18
    N = 1 << n

    dp = [[INF] * n for _ in range(N)]
    parent = [[-1] * n for _ in range(N)]

    # база
    for i in range(n):
        dp[1 << i][i] = 0
    # DP по маскам
    for mask in range(N):
        for v in range(n):
            if not (mask & (1 << v)):
                continue

            prev_mask = mask ^ (1 << v)
            if prev_mask == 0:
                continue

            for u in range(n):
                if prev_mask & (1 << u):
                    cost = dp[prev_mask][u] + data[u][v]
                    if cost < dp[mask][v]:
                        dp[mask][v] = cost
                        parent[mask][v] = u

    full_mask = N - 1

    # лучший конец
    ans = INF
    last = 0
    for i in range(n):
        if dp[full_mask][i] < ans:
            ans = dp[full_mask][i]
            last = i

    # восстановление пути
    path = []
    mask = full_mask
    cur = last
    while cur != -1:
        path.append(cur)
        prev = parent[mask][cur]
        mask ^= (1 << cur)
        cur = prev

    path.reverse()
    return path, ans

def main():
    with open("input.txt", "r") as inp:
        n = int(inp.readline())
        data = [list(map(int, inp.readline().split())) for _ in range(n)]
    path, ans = solve(n, data)
    with open("output.txt", "w") as out:
        out.write(str(ans) + "\n")
        out.write(" ".join(str(x + 1) for x in path))

if __name__ == "__main__":
    t_start = time.time()
    main()
    print(f"Время работы программы: {time.time() - t_start}")
    tracemalloc.start()
    main()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    print(f"Текущий объем памяти: {current / 2 ** 20} Mбайт, максимальный объем выделенной памяти: {peak / 2 ** 20} Mбайт\n")
