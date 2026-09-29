from time_memory_decorator import time_memory_decorator


@time_memory_decorator
def solve():
    # Чтение входных данных
    with open("input_task2.txt") as inp:
        message = inp.readline().rstrip('\n')

    # Удаление пробелов
    s = ''.join(message.split())
    n = len(s)

    # Если длина меньше 3, то способов нет
    if n < 3:
        return 0

    # Подсчёт количества способов
    # Идея: перебираем центральный индекс j, для каждого j считаем,
    # сколько одинаковых символов слева и справа можно выбрать в пару.

    # Предподсчёт: сколько раз каждая буква встречается справа от текущей позиции
    right_count = [0] * 26
    for ch in s:
        right_count[ord(ch) - ord('a')] += 1

    left_count = [0] * 26
    total_ways = 0

    for j in range(n):
        # Текущий символ s[j] удаляем из правого подсчёта (он станет центром)
        ch_idx = ord(s[j]) - ord('a')
        right_count[ch_idx] -= 1

        # Для фиксированного центрального j:
        # Способы = сумма по всем буквам (left_count[c] * right_count[c])
        # Это количество пар (i, k) с одинаковыми символами до и после j
        for c in range(26):
            total_ways += left_count[c] * right_count[c]

        # Добавляем текущий символ в левый подсчёт для следующих итераций
        left_count[ch_idx] += 1

    return total_ways


if __name__ == "__main__":
    print(solve())