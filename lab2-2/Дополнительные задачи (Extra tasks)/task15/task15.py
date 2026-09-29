import time
import tracemalloc

class AVLTree:
    def __init__(self, n, nodes):
        self.n = n
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
        """
        b = self.tree[a][2]  # правый ребенок
        if b == -1:
            return a

        left_of_b = self.tree[b][1]

        # Поворот
        self.tree[b][1] = a
        self.tree[a][2] = left_of_b

        # Обновляем высоты
        self.update_height(a)
        self.update_height(b)

        return b

    def small_right_rotate(self, a):
        """
        Малый правый поворот вокруг узла a
        """
        b = self.tree[a][1]  # левый ребенок
        if b == -1:
            return a

        right_of_b = self.tree[b][2]

        # Поворот
        self.tree[b][2] = a
        self.tree[a][1] = right_of_b

        # Обновляем высоты
        self.update_height(a)
        self.update_height(b)

        return b

    def big_left_rotate(self, a):
        """
        Большой левый поворот (правый-левый случай)
        """
        b = self.tree[a][2]
        if b == -1:
            return a

        c = self.tree[b][1]
        if c == -1:
            return self.small_left_rotate(a)

        left_of_c = self.tree[c][1]
        right_of_c = self.tree[c][2]

        # Поворот
        self.tree[c][1] = a
        self.tree[c][2] = b
        self.tree[a][2] = left_of_c
        self.tree[b][1] = right_of_c

        # Обновляем высоты
        self.update_height(a)
        self.update_height(b)
        self.update_height(c)

        return c

    def big_right_rotate(self, a):
        """
        Большой правый поворот (левый-правый случай)
        """
        b = self.tree[a][1]
        if b == -1:
            return a

        c = self.tree[b][2]
        if c == -1:
            return self.small_right_rotate(a)

        left_of_c = self.tree[c][1]
        right_of_c = self.tree[c][2]

        # Поворот
        self.tree[c][1] = b
        self.tree[c][2] = a
        self.tree[b][2] = left_of_c
        self.tree[a][1] = right_of_c

        # Обновляем высоты
        self.update_height(a)
        self.update_height(b)
        self.update_height(c)

        return c

    def balance_node(self, node_idx):
        """
        Балансирует узел и возвращает новый корень поддерева
        """
        if node_idx == -1:
            return -1

        balance = self.get_balance(node_idx)

        # Левый перекос (левое выше)
        if balance < -1:
            # Проверяем случай левый-правый
            if self.get_balance(self.tree[node_idx][1]) > 0:
                # Большой правый поворот
                return self.big_right_rotate(node_idx)
            # Малый правый поворот
            return self.small_right_rotate(node_idx)

        # Правый перекос (правое выше)
        if balance > 1:
            # Проверяем случай правый-левый
            if self.get_balance(self.tree[node_idx][2]) < 0:
                # Большой левый поворот
                return self.big_left_rotate(node_idx)
            # Малый левый поворот
            return self.small_left_rotate(node_idx)

        return node_idx

    def find_node(self, key):
        """
        Находит узел с заданным ключом и возвращает его индекс и путь к нему
        """
        path = []
        current_idx = 0

        while current_idx != -1:
            path.append(current_idx)
            if key < self.tree[current_idx][0]:
                current_idx = self.tree[current_idx][1]
            elif key > self.tree[current_idx][0]:
                current_idx = self.tree[current_idx][2]
            else:
                return current_idx, path

    def find_rightmost(self, start_idx):
        """
        Находит самую правую вершину в поддереве и путь к ней
        """
        path = []
        current = start_idx

        while current != -1 and self.tree[current][2] != -1:
            path.append(current)
            current = self.tree[current][2]

        if current != -1:
            path.append(current)

        return current, path

    def delete(self, key):
        """
        Удаляет вершину с заданным ключом из дерева
        """
        # Находим удаляемую вершину
        node_idx, path = self.find_node(key)

        # Случай 1: удаление корня в дереве из одной вершины
        if self.n == 1:
            self.tree = []
            self.n = 0
            return -1

        k, l, r, _ = self.tree[node_idx]
        parent_idx = -1
        if len(path) > 1:
            parent_idx = path[-2]
        if l == r:
            if self.tree[parent_idx][1] == node_idx:
                self.tree[parent_idx][1] = -1
            else:
                self.tree[parent_idx][2] = -1
            self.tree[node_idx] = None

            self.balance_up(parent_idx, path)

        elif l == -1:
            self.tree[node_idx] = self.tree[r]
            self.tree[r] = None
            self.balance_up(parent_idx, path)

        else:
            # Находим самую правую вершину в левом поддереве
            r_idx, r_path = self.find_rightmost(l)

            # Определяем родителя R
            if len(r_path) > 1:
                r_parent_idx = r_path[-2]
            else:
                r_parent_idx = -1  # R - корень левого поддерева (левый ребенок V)

            # Переносим ключ
            self.tree[node_idx][0] = self.tree[r_idx][0]

            # Удаляем вершину R
            r_left_child = self.tree[r_idx][1]  # у R нет правого ребенка

            if r_parent_idx == -1:
                # R - корень левого поддерева, значит node_idx - его родитель
                self.tree[node_idx][1] = r_left_child
            else:
                # Отсоединяем R от его родителя
                if self.tree[r_parent_idx][1] == r_idx:
                    self.tree[r_parent_idx][1] = r_left_child
                else:
                    self.tree[r_parent_idx][2] = r_left_child

            self.tree[r_idx] = None

            # Поднимаемся от родителя R
            if r_parent_idx != -1:
                # Если R не был корнем левого поддерева
                balance_start = r_parent_idx
                balance_path = path[:-1] + r_path[:-1]
            else:
                # Если R был корнем левого поддерева, начинаем с node_idx
                balance_start = node_idx
                balance_path = path[:-1]

            self.balance_up(balance_start, balance_path)


        self.rebuild_indices()


    def balance_up(self, start_idx, path):
        """
        Поднимается от start_idx к корню и балансирует узлы
        """
        if start_idx == -1:
            return -1

        current = start_idx
        # Находим позицию start_idx в пути
        try:
            pos = path.index(current)
            path_to_root = path[:pos]
        except ValueError:
            path_to_root = [current]

        # Идем от start_idx к корню
        for i in range(len(path_to_root) - 1, -1, -1):
            node = path_to_root[i]

            # Обновляем высоту
            self.update_height(node)

            # Балансируем
            new_root = self.balance_node(node)

            # Обновляем ссылку у родителя
            if i > 0:
                parent = path_to_root[i - 1]
                if self.tree[parent][1] == node:
                    self.tree[parent][1] = new_root
                else:
                    self.tree[parent][2] = new_root

    def rebuild_indices(self):
        """
        Перестраивает индексы после удаления
        """
        # Сохраняем пары (старый_индекс, узел) для всех не-None узлов
        nodes_with_old_indices = [(i, node) for i, node in enumerate(self.tree) if node is not None]

        # Если нет узлов
        if not nodes_with_old_indices:
            self.tree = []
            self.n = 0
            return

        # Словарь для отображения старых индексов на новые
        old_to_new = {}

        # Сортируем по старому индексу для предсказуемости (опционально)
        nodes_with_old_indices.sort(key=lambda x: x[0])

        # Создаем новый список узлов
        new_tree = []
        for new_idx, (old_idx, node) in enumerate(nodes_with_old_indices):
            old_to_new[old_idx] = new_idx
            # Копируем узел
            new_node = node.copy()
            new_tree.append(new_node)

        # Обновляем индексы детей
        for node in new_tree:
            if node[1] != -1 and node[1] in old_to_new:
                node[1] = old_to_new[node[1]]
            elif node[1] != -1:
                # Если индекс не найден, значит ссылка битая - ставим -1
                node[1] = -1

            if node[2] != -1 and node[2] in old_to_new:
                node[2] = old_to_new[node[2]]
            elif node[2] != -1:
                node[2] = -1

        self.tree = new_tree
        self.n = len(self.tree)

    def to_output_format(self):
        """
        Преобразует дерево в формат вывода (1-индексация)
        """

        result = [str(self.n)]
        for i, node in enumerate(self.tree):
            key = node[0]
            left = node[1]
            right = node[2]

            left_out = left + 1 if left != -1 else 0
            right_out = right + 1 if right != -1 else 0

            result.append(f"{key} {left_out} {right_out}")

        return result


def solve():
    with open("input.txt") as inp:
        n = int(inp.readline().strip())
        nodes = [list(map(int, inp.readline().strip().split())) for _ in range(n)]
        x = int(inp.readline())

    # Создаем АВЛ-дерево
    avl = AVLTree(n, nodes)

    # Удаляем вершину с ключом X
    avl.delete(x)

    # Выводим результат
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
    print(f"Текущий объем памяти: {current / 2 ** 20:.4f} Mбайт, "
          f"максимальный объем выделенной памяти: {peak / 2 ** 20:.4f} Mбайт\n")