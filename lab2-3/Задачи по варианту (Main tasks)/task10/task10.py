from collections import deque

from time_memory_decorator import time_memory_decorator


@time_memory_decorator
def solve():
    with open("input_task10.txt") as inp:
        n, m = map(int, inp.readline().split())

        # Чтение рёбер
        edges = []
        graph = [[] for _ in range(n + 1)]
        for i in range(m):
            parts = inp.readline().split()
            u, v, w = int(parts[0]), int(parts[1]), int(parts[2])
            edges.append((u, v, w))
            graph[u].append(v)

        # Чтение стартовой вершины
        s = int(inp.readline())

    # Инициализация расстояний
    INF = 10 ** 18
    dist = [INF] * (n + 1)
    dist[s] = 0

    # 1. Основная фаза Беллмана-Форда (n-1 релаксаций)
    for i in range(n - 1):
        relaxed = False
        for u, v, w in edges:
            if dist[u] < INF and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                relaxed = True
        if not relaxed:
            break

    # 2. Поиск вершин, которые находятся в отрицательных циклах или достижимы из них
    in_negative_cycle = [False] * (n + 1)

    # Находим вершины, которые можно улучшить на n-й итерации
    for u, v, w in edges:
        if dist[u] < INF and dist[u] + w < dist[v]:
            in_negative_cycle[v] = True

    # 3. BFS для поиска всех вершин, достижимых из отрицательных циклов
    queue = deque()
    for i in range(1, n + 1):
        if in_negative_cycle[i]:
            queue.append(i)

    visited_from_cycle = [False] * (n + 1)
    while queue:
        curr = queue.popleft()
        if visited_from_cycle[curr]:
            continue
        visited_from_cycle[curr] = True
        for nxt in graph[curr]:
            if not visited_from_cycle[nxt]:
                queue.append(nxt)

    # 4. Формирование вывода
    result = []
    for i in range(1, n + 1):
        if dist[i] == INF:
            result.append("*")
        elif visited_from_cycle[i]:
            result.append("-")
        else:
            result.append(dist[i])

    return result


if __name__ == "__main__":
    res = solve()
    for x in res:
        print(x)