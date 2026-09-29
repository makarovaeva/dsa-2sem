from collections import deque

from time_memory_decorator import time_memory_decorator


@time_memory_decorator
def solve():
    with open("input_task17.txt", "r") as inp:
        lines = inp.readlines()

    n, m = map(int, lines[0].split())

    # weight[u][v] = 0, если можно ехать по направлению u->v без нарушений
    # weight[u][v] = 1, если только в обратную сторону
    inf = 10 ** 9
    weight = [[inf] * n for _ in range(n)]
    for i in range(n):
        weight[i][i] = 0

    # Для каждой пары храним, есть ли прямая дорога
    direct = [[False] * n for _ in range(n)]

    for i in range(1, m + 1):
        u, v = map(int, lines[i].split())
        u -= 1
        v -= 1
        direct[u][v] = True

    # Заполняем веса
    for u in range(n):
        for v in range(n):
            if u == v:
                continue
            if direct[u][v] and direct[v][u]:
                weight[u][v] = 0
                weight[v][u] = 0
            elif direct[u][v]:
                weight[u][v] = 0
                weight[v][u] = 1
            elif direct[v][u]:
                weight[u][v] = 1
                weight[v][u] = 0

    # BFS / 0-1 BFS из каждой вершины
    max_dist = 0

    for start in range(n):
        dist = [inf] * n
        dist[start] = 0
        dq = deque()
        dq.append(start)

        while dq:
            u = dq.popleft()
            for v in range(n):
                if weight[u][v] != inf:
                    new_dist = dist[u] + weight[u][v]
                    if new_dist < dist[v]:
                        dist[v] = new_dist
                        if weight[u][v] == 0:
                            dq.appendleft(v)
                        else:
                            dq.append(v)

        # Проверяем, что все вершины достижимы
        for v in range(n):
            if dist[v] != inf and dist[v] > max_dist:
                max_dist = dist[v]

    return max_dist


if __name__ == "__main__":
    print(solve())
