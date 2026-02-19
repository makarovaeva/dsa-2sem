import time
import tracemalloc
from collections import deque


class AVLTree:
    def __init__(self, n, nodes):
        self.n = n
        self.tree = []
        for i in range(n):
            key, left, right = nodes[i]
            left_idx = left - 1 if left > 0 else -1
            right_idx = right - 1 if right > 0 else -1
            self.tree.append([key, left_idx, right_idx, 1])

        if n > 0:
            self.calc_heights()

    def calc_heights(self):
        """Вычисляет высоты всех узлов (постфиксный обход)"""
        if self.n == 0:
            return

        # Инициализируем все высоты как -1 (невычисленные)
        for i in range(self.n):
            self.tree[i][3] = -1

        stack = [0]

        while stack:
            v = stack[-1]

            if self.tree[v][3] == -1:
                _, left, right, _ = self.tree[v]

                if right != -1 and self.tree[right][3] == -1:
                    stack.append(right)
                if left != -1 and self.tree[left][3] == -1:
                    stack.append(left)

                if (left == -1 or self.tree[left][3] != -1) and (right == -1 or self.tree[right][3] != -1):
                    stack.pop()
                    left_h = self.tree[left][3] if left != -1 else 0
                    right_h = self.tree[right][3] if right != -1 else 0
                    self.tree[v][3] = 1 + max(left_h, right_h)
            else:
                stack.pop()

    def get_height(self, node_idx):
        return self.tree[node_idx][3] if node_idx != -1 else 0

    def update_height(self, node_idx):
        if node_idx == -1:
            return
        left_h = self.get_height(self.tree[node_idx][1])
        right_h = self.get_height(self.tree[node_idx][2])
        self.tree[node_idx][3] = 1 + max(left_h, right_h)

    def get_balance(self, node_idx):
        if node_idx == -1:
            return 0
        return self.get_height(self.tree[node_idx][2]) - self.get_height(self.tree[node_idx][1])

    def rotate_right(self, y):
        x = self.tree[y][1]
        if x == -1:
            return y

        T2 = self.tree[x][2]
        self.tree[x][2] = y
        self.tree[y][1] = T2

        self.update_height(y)
        self.update_height(x)
        return x

    def rotate_left(self, x):
        y = self.tree[x][2]
        if y == -1:
            return x

        T2 = self.tree[y][1]
        self.tree[y][1] = x
        self.tree[x][2] = T2

        self.update_height(x)
        self.update_height(y)
        return y

    def balance_node(self, node_idx):
        if node_idx == -1:
            return -1

        balance = self.get_balance(node_idx)

        # Левый перекос
        if balance < -1:
            if self.get_balance(self.tree[node_idx][1]) > 0:
                self.tree[node_idx][1] = self.rotate_left(self.tree[node_idx][1])
            return self.rotate_right(node_idx)

        # Правый перекос
        if balance > 1:
            if self.get_balance(self.tree[node_idx][2]) < 0:
                self.tree[node_idx][2] = self.rotate_right(self.tree[node_idx][2])
            return self.rotate_left(node_idx)

        return node_idx

    def insert(self, key):
        if self.n == 0:
            self.tree.append([key, -1, -1, 1])
            self.n = 1
            return

        # Поиск места вставки и сбор пути
        path = []
        current = 0

        while True:
            path.append(current)
            if key < self.tree[current][0]:
                if self.tree[current][1] == -1:
                    break
                current = self.tree[current][1]
            else:
                if self.tree[current][2] == -1:
                    break
                current = self.tree[current][2]

        parent = path[-1]

        # Создание нового узла
        new_idx = self.n
        self.tree.append([key, -1, -1, 1])
        self.n += 1

        # Присоединение к родителю
        if key < self.tree[parent][0]:
            self.tree[parent][1] = new_idx
        else:
            self.tree[parent][2] = new_idx

        # Балансировка снизу вверх
        for i in range(len(path) - 1, -1, -1):
            node = path[i]
            self.update_height(node)
            new_root = self.balance_node(node)

            if i > 0:
                parent_node = path[i - 1]
                if self.tree[parent_node][1] == node:
                    self.tree[parent_node][1] = new_root
                else:
                    self.tree[parent_node][2] = new_root

    def renumber_bfs(self):
        """Перенумеровывает узлы в порядке BFS для соблюдения условия i < Li, Ri"""
        if self.n == 0:
            return

        # Находим корень (узел, который не является ничьим ребенком)
        is_child = [False] * self.n
        for i in range(self.n):
            node = self.tree[i]
            if node[1] != -1:
                is_child[node[1]] = True
            if node[2] != -1:
                is_child[node[2]] = True

        root = -1
        for i in range(self.n):
            if not is_child[i]:
                root = i
                break

        if root == -1:
            root = 0

        # BFS обход
        queue = deque([root])
        bfs_order = []
        visited = [False] * self.n

        while queue:
            node = queue.popleft()
            if visited[node]:
                continue
            visited[node] = True
            bfs_order.append(node)

            if self.tree[node][1] != -1:
                queue.append(self.tree[node][1])
            if self.tree[node][2] != -1:
                queue.append(self.tree[node][2])

        # Создаем отображение старых индексов на новые
        old_to_new = {old: new for new, old in enumerate(bfs_order)}

        # Создаем новое дерево
        new_tree = []
        for old_idx in bfs_order:
            node = self.tree[old_idx].copy()
            new_tree.append(node)

        # Обновляем индексы детей
        for node in new_tree:
            if node[1] != -1:
                node[1] = old_to_new[node[1]]
            if node[2] != -1:
                node[2] = old_to_new[node[2]]

        self.tree = new_tree
        self.n = len(self.tree)

    def to_output_format(self):
        if self.n == 0:
            return ["0"]

        # Сначала перенумеровываем
        self.renumber_bfs()

        result = [str(self.n)]
        for i in range(self.n):
            node = self.tree[i]
            left = node[1] + 1 if node[1] != -1 else 0
            right = node[2] + 1 if node[2] != -1 else 0
            result.append(f"{node[0]} {left} {right}")
        return result


def solve():
    with open("input.txt") as inp:
        n = int(inp.readline().strip())
        nodes = [tuple(map(int, inp.readline().strip().split())) for _ in range(n)]
        x = int(inp.readline().strip())

    avl = AVLTree(n, nodes)
    avl.insert(x)
    return avl.to_output_format()


if __name__ == "__main__":
    t_start = time.time()
    result = solve()
    print(f"Время работы программы: {time.time() - t_start:.4f}")

    with open("output.txt", "w") as out:
        out.write("\n".join(result))

    tracemalloc.start()
    solve()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    print(f"Память: {current / 2 ** 20:.4f} МБ / {peak / 2 ** 20:.4f} МБ")