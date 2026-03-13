from time_memory_decorator import time_memory_decorator


@time_memory_decorator
def solve():
    with open('input.txt', 'r') as inp:
        n, m = map(int, inp.readline().split())

        # Создаём список смежности
        graph = [[] for _ in range(n + 1)]

        for i in range(m):
            a, b = map(int, inp.readline().split())
            graph[a].append(b)
            graph[b].append(a)

        u, v = map(int, inp.readline().split())

    # BFS для поиска пути от u к v
    visited = [False] * (n + 1)
    queue = [u]
    visited[u] = True

    while queue:
        current = queue.pop(0)

        if current == v:
            return 1

        for neighbor in graph[current]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)

    return 0


if __name__ == "__main__":
    print(solve())
