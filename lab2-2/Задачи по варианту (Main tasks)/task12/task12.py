import time
import tracemalloc


def main():
    # Читаем дерево
    tree = []
    for k, l, r in data:
        tree.append((k, l - 1 if l > 0 else -1, r - 1 if r > 0 else -1))

    # Массивы для высот и результатов
    height = [-1] * n
    result = [0] * n

    # Итеративный постфиксный обход
    stack = [0]  # корень

    while stack:
        v = stack[-1]

        if height[v] == -1:
            _, l, r = tree[v]

            # Добавляем детей в стек (сначала правого для порядка)
            if r != -1 and height[r] == -1:
                stack.append(r)
            if l != -1 and height[l] == -1:
                stack.append(l)

            # Если нет детей или они уже обработаны
            if (l == -1 or height[l] != -1) and (r == -1 or height[r] != -1):
                stack.pop()

                # Вычисляем высоты детей
                h_left = height[l] if l != -1 else -1
                h_right = height[r] if r != -1 else -1

                # Высота текущей вершины
                height[v] = 1 + max(h_left, h_right)

                # Баланс (правое - левое)
                result[v] = h_right - h_left
        else:
            stack.pop()

    return result


if __name__ == "__main__":
    with open("input.txt") as inp:
        n = int(inp.readline().strip())
        data = [list(map(int, inp.readline().strip().split())) for _ in range(n)]
    t_start = time.time()
    with open("output.txt", "w") as out:
        out.write("\n".join(map(str, main())))
    print(f"Время работы программы: {time.time() - t_start}")
    tracemalloc.start()
    main()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    print(f"Текущий объем памяти: {current / 2 ** 20} Mбайт, максимальный объем выделенной памяти: {peak / 2 ** 20} Mбайт\n")
