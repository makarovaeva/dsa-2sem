from time_memory_decorator import time_memory_decorator


@time_memory_decorator
def solve():
    with open("input_task6.txt") as inp:
        s = inp.readline().strip()

    n = len(s)
    z = [0] * n

    # Алгоритм построения Z-функции за O(n)
    l, r = 0, 0  # границы самого правого отрезка совпадения
    for i in range(1, n):
        if i <= r:
            # Используем ранее вычисленные значения
            z[i] = min(r - i + 1, z[i - l])

        # Наивное расширение, пока символы совпадают
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1

        # Обновляем границы самого правого отрезка
        if i + z[i] - 1 > r:
            l, r = i, i + z[i] - 1

    # Формируем вывод для индексов от 1 до n-1
    result = " ".join(map(str, z[1:]))

    return result


if __name__ == "__main__":
    print(solve())