import time
import tracemalloc


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None


class BST:
    def __init__(self):
        self.root = None

    def search(self, key):
        """Поиск узла по ключу"""
        current = self.root
        while current is not None:
            if current.key == key:
                return current
            elif key < current.key:
                current = current.left
            else:
                current = current.right
        return None

    def insert(self, key):
        """Вставка ключа в дерево"""
        # Проверяем, существует ли уже такой ключ
        if self.search(key) is not None:
            return

        new_node = Node(key)

        if self.root is None:
            self.root = new_node
            return

        current = self.root
        parent = None

        while current is not None:
            parent = current
            if key < current.key:
                current = current.left
            else:
                current = current.right

        new_node.parent = parent
        if key < parent.key:
            parent.left = new_node
        else:
            parent.right = new_node

    def minimum(self, node):
        """Поиск минимального элемента в поддереве"""
        if node is None:
            return None
        current = node
        while current.left is not None:
            current = current.left
        return current

    def next(self, x):
        """Поиск следующего элемента (строго большего x)"""
        current = self.root
        successor = None

        while current is not None:
            if current.key > x:
                successor = current
                current = current.left
            else:
                current = current.right

        return successor

    def prev(self, x):
        """Поиск предыдущего элемента (строго меньшего x)"""
        current = self.root
        predecessor = None

        while current is not None:
            if current.key < x:
                predecessor = current
                current = current.right
            else:
                current = current.left

        return predecessor

    def transplant(self, u, v):
        """Замена поддерева u на поддерево v"""
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v

        if v is not None:
            v.parent = u.parent

    def delete(self, key):
        """Удаление ключа из дерева"""
        node = self.search(key)
        if node is None:
            return

        # Случай 1: нет левого ребенка
        if node.left is None:
            self.transplant(node, node.right)
        # Случай 2: нет правого ребенка
        elif node.right is None:
            self.transplant(node, node.left)
        # Случай 3: есть оба ребенка
        else:
            # Находим минимальный элемент в правом поддереве
            y = self.minimum(node.right)

            # Если y не является прямым правым ребенком node
            if y.parent != node:
                self.transplant(y, y.right)
                y.right = node.right
                y.right.parent = y

            self.transplant(node, y)
            y.left = node.left
            y.left.parent = y

        # Очищаем ссылки удаляемого узла
        node.left = None
        node.right = None
        node.parent = None

    def exists(self, key):
        """Проверка существования ключа"""
        return self.search(key) is not None

def main():
    bst = BST()
    for com, x in data:
        x = int(x)
        if com == "insert" and not bst.exists(x):
            bst.insert(x)
        elif com == "delete" and bst.exists(x):
            bst.delete(x)
        elif com == "exists":
            print("true" if bst.exists(x) else "false")
        elif com == "next":
            k = bst.next(x)
            print(k.key if k is not None else "none")
        else:
            k = bst.prev(x)
            print(k.key if k is not None else "none")


if __name__ == "__main__":
    with open("input.txt") as inp:
        data = []
        for line in inp.readlines():
            data.append(line.strip().split())
    t_start = time.time()
    tracemalloc.start()
    main()
    print(f"Время работы программы: {time.time() - t_start:.4f}")
    current, peak = tracemalloc.get_traced_memory()
    print(f"Текущий объем памяти: {current / 2 ** 20:.4f} Mбайт, "
    f"максимальный объем выделенной памяти: {peak / 2 ** 20:.4f} Mбайт\n")
    tracemalloc.stop()
