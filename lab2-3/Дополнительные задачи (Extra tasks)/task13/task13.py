from collections import deque

from time_memory_decorator import time_memory_decorator


@time_memory_decorator
def solve():
    with open("input_task13.txt", "r") as inp:
        lines = [line.strip() for line in inp.readlines()]

    n, m = map(int, lines[0].split())
    garden = [list(line) for line in lines[1:1 + n]]

    visited = [[False] * m for _ in range(n)]
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def bfs(sx, sy):
        queue = deque()
        queue.append((sx, sy))
        visited[sx][sy] = True
        while queue:
            x, y = queue.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and garden[nx][ny] == '#':
                    visited[nx][ny] = True
                    queue.append((nx, ny))

    count = 0
    for i in range(n):
        for j in range(m):
            if garden[i][j] == '#' and not visited[i][j]:
                bfs(i, j)
                count += 1

    return count


if __name__ == "__main__":
    print(solve())