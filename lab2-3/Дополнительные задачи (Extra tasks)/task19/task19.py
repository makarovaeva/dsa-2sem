import math

from time_memory_decorator import time_memory_decorator


@time_memory_decorator
def solve():
    with open("input_task19.txt", "r") as inp:
        n = int(inp.readline().strip())
        points = [tuple(map(int, inp.readline().split())) for _ in range(n)]
        k = int(inp.readline().strip())

    # Создаём все рёбра
    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            dx = points[i][0] - points[j][0]
            dy = points[i][1] - points[j][1]
            dist = math.sqrt(dx * dx + dy * dy)
            edges.append((dist, i, j))

    # Сортируем рёбра по расстоянию
    edges.sort(key=lambda x: x[0])

    # DSU
    parent = list(range(n))
    rank = [0] * n

    def find(v):
        while parent[v] != v:
            parent[v] = parent[parent[v]]
            v = parent[v]
        return v

    def union(v1, v2):
        r1, r2 = find(v1), find(v2)
        if r1 == r2:
            return False
        if rank[r1] < rank[r2]:
            parent[r1] = r2
        elif rank[r1] > rank[r2]:
            parent[r2] = r1
        else:
            parent[r2] = r1
            rank[r1] += 1
        return True

    # Строим MST
    mst_edges = []
    for dist, u, v in edges:
        if union(u, v):
            mst_edges.append(dist)
        if len(mst_edges) == n - 1:
            break

    # Сортируем рёбра MST по убыванию
    mst_edges.sort(reverse=True)

    # Ответ — (k-1)-е по величине ребро в MST
    # Если k == n, то ответ — минимальное ребро в MST (последнее)
    if k == n:
        answer = mst_edges[-1]
    elif k == 1:
        answer = mst_edges[0]  # Максимальное ребро, но для 1 кластера d = ∞? Нет, условие не выполняется.
    else:
        answer = mst_edges[k - 2]  # Индекс k-2, т.к. mst_edges[0] — самое длинное, mst_edges[1] — второе

    return f"{answer:.12f}"


if __name__ == "__main__":
    print(solve())
