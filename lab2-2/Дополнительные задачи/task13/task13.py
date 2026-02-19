import time
import tracemalloc
from collections import deque


class AVLTree:
    def __init__(self):
        # Преобразуем входные данные в список узлов [key, left, right, height]
        self.tree = []
        for i in range(n):
            key, left, right = nodes[i]
            # Приводим индексы к 0-based (-1 если нет ребенка)
            left_idx = left - 1 if left > 0 else -1
            right_idx = right - 1 if right > 0 else -1
            self.tree.append([key, left_idx, right_idx, -1])  # временная высота

        # Вычисляем реальные высоты
        self.calc_heights()

    def calc_heights(self):
        """Вычисляет высоты всех узлов (постфиксный обход)"""

        stack = [0]  # корень

        while stack:
            v = stack[-1]

            if self.get_height(v) == -1:
                _, left, right, _ = self.tree[v]

                # Добавляем детей в стек
                if right != -1 and self.get_height(right) == -1:
                    stack.append(right)
                if left != -1 and self.get_height(left) == -1:
                    stack.append(left)

                # Если дети обработаны или их нет
                if (left == -1 or self.get_height(left) != -1) and (right == -1 or self.get_height(right) != -1):
                    stack.pop()

                    # Вычисляем высоту
                    left_h = self.get_height(left) if left != -1 else -1
                    right_h = self.get_height(right) if right != -1 else -1
                    self.tree[v][3] = 1 + max(left_h, right_h)
            else:
                stack.pop()

    def get_height(self, node_idx):
        """Возвращает высоту узла"""
        return self.tree[node_idx][3] if node_idx != -1 else 0

    def update_height(self, node_idx):
        """Обновляет высоту узла"""
        if node_idx == -1:
            return
        left_h = self.get_height(self.tree[node_idx][1])
        right_h = self.get_height(self.tree[node_idx][2])
        self.tree[node_idx][3] = 1 + max(left_h, right_h)

    def get_balance(self, node_idx):
        """Возвращает баланс узла (правое - левое)"""
        if node_idx == -1:
            return 0
        left_h = self.get_height(self.tree[node_idx][1])
        right_h = self.get_height(self.tree[node_idx][2])
        return right_h - left_h

    def small_left_rotate(self, a):
        """
        Малый левый поворот вокруг узла a
        a - индекс узла, вокруг которого делаем поворот
        возвращает новый корень поддерева
        """
        # Получаем правого ребенка узла a
        b = self.tree[a][2]  # b - правый ребенок

        if b == -1:
            return a  # нет правого ребенка, поворот невозможен

        # Сохраняем левое поддерево узла b
        left_of_b = self.tree[b][1]

        # Делаем поворот
        self.tree[b][1] = a  # левым ребенком b становится a
        self.tree[a][2] = left_of_b  # правым ребенком a становится бывшее левое поддерево b

        # Обновляем высоты
        self.update_height(a)
        self.update_height(b)

        return b  # b становится новым корнем

    def big_left_rotate(self, a):
        """
        Большой левый поворот вокруг узла a (правый-левый случай)
        a - индекс узла, вокруг которого делаем поворот
        возвращает новый корень поддерева
        """
        # Получаем правого ребенка узла a
        b = self.tree[a][2]  # b - правый ребенок

        if b == -1:
            return a  # нет правого ребенка, поворот невозможен

        # Получаем левого ребенка узла b (узел c)
        c = self.tree[b][1]  # c - левый ребенок b

        if c == -1:
            # Если нет c, то это малый левый поворот
            return self.small_left_rotate(a)

        # Сохраняем поддеревья узла c
        left_of_c = self.tree[c][1]  # левое поддерево c
        right_of_c = self.tree[c][2]  # правое поддерево c

        # Выполняем большой левый поворот
        # 1. c становится новым корнем
        self.tree[c][1] = a  # левым ребенком c становится a
        self.tree[c][2] = b  # правым ребенком c становится b

        # 2. Обновляем связи a и b
        self.tree[a][2] = left_of_c  # правым ребенком a становится левое поддерево c
        self.tree[b][1] = right_of_c  # левым ребенком b становится правое поддерево c

        # Обновляем высоты
        self.update_height(a)
        self.update_height(b)
        self.update_height(c)

        return c  # c становится новым корнем

    def to_output_format(self, root):
        """
        Преобразует дерево в формат вывода (1-индексация)
        с обязательным условием: номер вершины меньше номера ее детей
        """

        # Нумеруем узлы в порядке обхода в ширину (BFS)
        # Это гарантирует, что родитель будет иметь меньший номер, чем дети
        new_indices = [-1] * n
        bfs_order = []
        queue = deque([root])
        idx = 0

        while queue:
            node = queue.popleft()
            new_indices[node] = idx
            bfs_order.append(node)
            idx += 1

            if self.tree[node][1] != -1:
                queue.append(self.tree[node][1])
            if self.tree[node][2] != -1:
                queue.append(self.tree[node][2])

        # Формируем вывод в порядке BFS
        result = [str(n)]
        for node in bfs_order:
            key = self.tree[node][0]
            left = self.tree[node][1]
            right = self.tree[node][2]

            # Преобразуем индексы детей в новые (1-based)
            left_out = new_indices[left] + 1 if left != -1 else 0
            right_out = new_indices[right] + 1 if right != -1 else 0

            result.append(f"{key} {left_out} {right_out}")

        return result


def solve():
    # Создаем АВЛ-дерево
    avl = AVLTree()

    # Получаем индекс правого ребенка корня
    right_child = avl.tree[0][2]

    # Проверяем баланс правого ребенка для выбора типа поворота
    if right_child != -1 and avl.get_balance(right_child) == -1:
        new_root = avl.big_left_rotate(0)
    else:
        new_root = avl.small_left_rotate(0)

    return avl.to_output_format(new_root)


if __name__ == "__main__":
    with open("input.txt") as inp:
        n = int(inp.readline())
        nodes = [list(map(int, inp.readline().split())) for _ in range(n)]
    t_start = time.time()
    result = solve()
    print(f"Время работы программы: {time.time() - t_start:.4f}")
    with open("output.txt", "w") as out:
        out.write("\n".join(result))
    tracemalloc.start()
    solve()
    current, peak = tracemalloc.get_traced_memory()
    print(f"Текущий объем памяти: {current / 2 ** 20:.4f} Mбайт, максимальный объем выделенной памяти: {peak / 2 ** 20:.4f} Mбайт\n")
    tracemalloc.stop()