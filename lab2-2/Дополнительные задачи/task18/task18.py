import random
import time
import tracemalloc

class Node:
    __slots__ = ('ch', 'prior', 'sz', 'char')

    def __init__(self, char, prior):
        self.ch = [-1, -1]
        self.prior = prior
        self.sz = 1
        self.char = char


class ImplicitTreap:
    def __init__(self, s):
        self.nodes = []
        self.root = -1

        # Оптимизация 1: Быстрое построение дерева через стек (O(n))
        if s:
            # Генерируем все приоритеты заранее
            priors = [random.randint(1, 2 ** 30) for _ in range(len(s))]

            # Строим дерево за O(n) с помощью стека (как Cartesian tree)
            stack = []
            for i, char in enumerate(s):
                node_idx = self._new_node(char, priors[i])
                last = -1

                while stack and priors[stack[-1]] < priors[i]:
                    last = stack.pop()

                if stack:
                    self.nodes[stack[-1]].ch[1] = node_idx

                if last != -1:
                    self.nodes[node_idx].ch[0] = last

                stack.append(node_idx)

                # Обновляем размеры (можно отложить)

            # Обновляем размеры для всех узлов
            self._update_all_sizes()

            # Корень - первый элемент в стеке
            self.root = stack[0] if stack else -1

    def _new_node(self, char, prior):
        idx = len(self.nodes)
        self.nodes.append(Node(char, prior))
        return idx

    def _size(self, t):
        return self.nodes[t].sz if t != -1 else 0

    def _update(self, t):
        if t != -1:
            node = self.nodes[t]
            node.sz = 1 + self._size(node.ch[0]) + self._size(node.ch[1])

    def _update_all_sizes(self):
        """Обновляет размеры всех узлов через постфиксный обход"""
        if self.root == -1:
            return

        stack = [(self.root, False)]
        while stack:
            node_idx, visited = stack.pop()
            node = self.nodes[node_idx]

            if visited:
                node.sz = 1 + self._size(node.ch[0]) + self._size(node.ch[1])
            else:
                stack.append((node_idx, True))
                if node.ch[1] != -1:
                    stack.append((node.ch[1], False))
                if node.ch[0] != -1:
                    stack.append((node.ch[0], False))

    def split(self, t, key):
        """Разделяет дерево - итеративная версия для скорости"""
        if t == -1:
            return -1, -1

        # Оптимизация 2: Используем локальные переменные для быстрого доступа
        nodes = self.nodes
        size_func = self._size

        # Путь для обратного обновления
        path_left = []
        path_right = []

        current = t
        while current != -1:
            node = nodes[current]
            cur_key = size_func(node.ch[0])

            if key <= cur_key:
                # Идем влево
                path_right.append(current)
                current = node.ch[0]
            else:
                # Идем вправо
                key -= cur_key + 1
                path_left.append(current)
                current = node.ch[1]

        # Формируем левое дерево
        left_root = -1
        for node_idx in reversed(path_left):
            node = nodes[node_idx]
            node.ch[1] = left_root
            self._update(node_idx)
            left_root = node_idx

        # Формируем правое дерево
        right_root = -1
        for node_idx in reversed(path_right):
            node = nodes[node_idx]
            node.ch[0] = right_root
            self._update(node_idx)
            right_root = node_idx

        return left_root, right_root

    def merge(self, left, right):
        """Сливает два дерева - итеративная версия"""
        if left == -1:
            return right
        if right == -1:
            return left

        nodes = self.nodes

        # Путь для обратного обновления
        path = []

        # Спускаемся, сравнивая приоритеты
        l, r = left, right
        while l != -1 and r != -1:
            if nodes[l].prior > nodes[r].prior:
                path.append((l, True))  # True означает, что идем по правому ребенку
                l = nodes[l].ch[1]
            else:
                path.append((r, False))  # False означает, что идем по левому ребенку
                r = nodes[r].ch[0]

        # Соединяем оставшиеся части
        if l != -1:
            remainder = l
        else:
            remainder = r

        # Поднимаемся обратно и обновляем ссылки
        for node_idx, is_right in reversed(path):
            if is_right:
                nodes[node_idx].ch[1] = remainder
                self._update(node_idx)
                remainder = node_idx
            else:
                nodes[node_idx].ch[0] = remainder
                self._update(node_idx)
                remainder = node_idx

        return remainder

    def inorder(self, t, result):
        """Итеративный симметричный обход (быстрее рекурсии)"""
        stack = []
        current = t

        while stack or current != -1:
            while current != -1:
                stack.append(current)
                current = self.nodes[current].ch[0]

            current = stack.pop()
            result.append(self.nodes[current].char)
            current = self.nodes[current].ch[1]

    def process_query(self, i, j, k):
        """
        Вырезает подстроку с i по j и вставляет после k символов
        """
        # Оптимизация 3: Избегаем лишних split при k = 0 или k = размер - длина
        length = j - i + 1
        total_size = self._size(self.root)

        # Разделяем дерево на три части
        left, temp = self.split(self.root, i)
        middle, right = self.split(temp, length)

        # Объединяем left и right
        self.root = self.merge(left, right)

        # Оптимизация 4: Если k == total_size - length, можно вставить в конец
        if k == self._size(self.root):
            self.root = self.merge(self.root, middle)
        else:
            left2, right2 = self.split(self.root, k)
            self.root = self.merge(self.merge(left2, middle), right2)


def solve():
    treap = ImplicitTreap(s)

    for i, j, k in queries:
        treap.process_query(i, j, k)

    result = []
    treap.inorder(treap.root, result)
    return ''.join(result)


if __name__ == "__main__":
    with open("input.txt") as inp:
        s = inp.readline()
        n = int(inp.readline())
        queries = [tuple(map(int, inp.readline().split())) for _ in range(n)]
    t_start = time.time()
    result = solve()
    print(f"Время работы программы: {time.time() - t_start}")
    with open("output.txt", "w") as out:
        out.write(result)
    tracemalloc.start()
    solve()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    print(f"Текущий объем памяти: {current / 2 ** 20} Mбайт, максимальный объем выделенной памяти: {peak / 2 ** 20} Mбайт\n")
