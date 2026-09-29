from time_memory_decorator import time_memory_decorator


@time_memory_decorator
def solve():
    with open("input_task14.txt") as inp:
        n = int(inp.readline().strip())
        d, v = map(int, inp.readline().split())
        r = int(inp.readline().strip())

        buses = []
        for i in range(r):
            parts = list(map(int, inp.readline().split()))
            buses.append(tuple(parts))  # (from, dep_time, to, arr_time)

    INF = 10**9
    # Время прибытия в каждую деревню
    time_in = [INF] * (n + 1)
    time_in[d] = 0  # стартуем из d в момент 0

    # Алгоритм Беллмана-Форда по количеству шагов (макс N-1 итераций)
    for _ in range(n - 1):
        updated = False
        for from_city, dep, to_city, arr in buses:
            if time_in[from_city] <= dep and arr < time_in[to_city]:
                time_in[to_city] = arr
                updated = True
        if not updated:
            break

    return time_in[v] if time_in[v] != INF else -1


if __name__ == "__main__":
    print(solve())