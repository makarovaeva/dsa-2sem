import math

from time_memory_decorator import time_memory_decorator


@time_memory_decorator
def solve():
    with open("input_task18.txt", "r") as inp:
        n = int(inp.readline().strip())
        points = [tuple(map(int, inp.readline().split())) for _ in range(n)]

    # Создаём все возможные рёбра
    edges = [(math.dist(points[i], points[j]), i, j) for i in range(n) for j in range(i + 1, n)]

    # Сортируем рёбра по длине
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

    total_length = 0.0
    edges_used = 0

    for dist, u, v in edges:
        if union(u, v):
            total_length += dist
            edges_used += 1
            if edges_used == n - 1:
                break

    return f"{total_length:.9f}"


if __name__ == "__main__":
    print(solve())
