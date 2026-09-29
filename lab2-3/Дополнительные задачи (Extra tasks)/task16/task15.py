from collections import deque

from time_memory_decorator import time_memory_decorator


@time_memory_decorator
def solve():
    with open("input_task15.txt", "r") as inp:
        lines = [line.strip() for line in inp.readlines()]

    idx = 0
    n, m = map(int, lines[idx].split())
    idx += 1

    garden = []
    for _ in range(n):
        garden.append(list(lines[idx]))
        idx += 1

    qx, qy, l = map(int, lines[idx].split())
    idx += 1
    qx -= 1
    qy -= 1

    musketeers = []
    for _ in range(4):
        x, y, p = map(int, lines[idx].split())
        idx += 1
        musketeers.append((x - 1, y - 1, p))

    # BFS от королевы до всех клеток (чтобы не запускать 4 BFS)
    dist = [[-1] * m for _ in range(n)]
    if garden[qx][qy] == '0':  # королева стоит на проходимой клетке
        dist[qx][qy] = 0
        queue = deque()
        queue.append((qx, qy))

        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while queue:
            x, y = queue.popleft()
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and garden[nx][ny] == '0' and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1
                    queue.append((nx, ny))

    # Считаем подвески
    total = 0
    for x, y, p in musketeers:
        if 0 <= dist[x][y] <= l:
            total += p

    return total


if __name__ == "__main__":
    print(solve())