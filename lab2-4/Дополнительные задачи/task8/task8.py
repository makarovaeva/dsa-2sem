from time_memory_decorator import time_memory_decorator
import random


def find_longest_common_substring(s, t, x, m1, m2):
    n, m = len(s), len(t)

    # Предвычисление степеней x (максимальная длина - до min(n, m))
    max_len = min(n, m)
    pow_x1 = [1] * (max_len + 1)
    pow_x2 = [1] * (max_len + 1)
    for i in range(1, max_len + 1):
        pow_x1[i] = (pow_x1[i - 1] * x) % m1
        pow_x2[i] = (pow_x2[i - 1] * x) % m2

    # Префиксные хеши для s
    h1_s = [0] * (n + 1)
    h2_s = [0] * (n + 1)
    for i in range(1, n + 1):
        h1_s[i] = (h1_s[i - 1] * x + ord(s[i - 1])) % m1
        h2_s[i] = (h2_s[i - 1] * x + ord(s[i - 1])) % m2

    # Префиксные хеши для t
    h1_t = [0] * (m + 1)
    h2_t = [0] * (m + 1)
    for i in range(1, m + 1):
        h1_t[i] = (h1_t[i - 1] * x + ord(t[i - 1])) % m1
        h2_t[i] = (h2_t[i - 1] * x + ord(t[i - 1])) % m2

    # Функция получения хеша подстроки
    def get_hash(h, pow_x, l, r, mod):
        # l - начальная позиция (включительно), r - конечная (исключительно)
        return (h[r] - h[l] * pow_x[r - l]) % mod

    # Двоичный поиск максимальной длины
    left, right = 0, max_len
    best_i, best_j, best_len = 0, 0, 0

    while left <= right:
        k = (left + right) // 2

        if k == 0:
            # Всегда есть общая подстрока длины 0
            left = k + 1
            continue

        # Множества для хранения хешей подстрок s длины k
        hash_set1 = set()
        hash_set2 = set()
        # Также сохраняем соответствие хеш -> позиция для восстановления
        pos_map = {}

        # Добавляем все подстроки s длины k
        for i in range(n - k + 1):
            h1 = get_hash(h1_s, pow_x1, i, i + k, m1)
            h2 = get_hash(h2_s, pow_x2, i, i + k, m2)
            hash_set1.add(h1)
            hash_set2.add(h2)
            # Для первого модуля сохраняем позицию (для восстановления при совпадении)
            pos_map[(h1, h2)] = i

        found = False
        # Проверяем подстроки t длины k
        for j in range(m - k + 1):
            h1 = get_hash(h1_t, pow_x1, j, j + k, m1)
            h2 = get_hash(h2_t, pow_x2, j, j + k, m2)

            if h1 in hash_set1 and h2 in hash_set2:
                # Нашли совпадение по хешам
                i = pos_map.get((h1, h2), -1)
                if i != -1 and s[i:i + k] == t[j:j + k]:
                    best_i, best_j, best_len = i, j, k
                    found = True
                    break

        if found:
            left = k + 1
        else:
            right = k - 1

    return best_i, best_j, best_len


@time_memory_decorator
def solve():
    with open("input_task8.txt") as inp:
        lines = [line.strip() for line in inp if line.strip()]

    results = []
    for line in lines:
        if ' ' in line:
            s, t = line.split()
            i, j, l = find_longest_common_substring(s, t, x, m1, m2)
            results.append(f"{i} {j} {l}")

    return results


if __name__ == "__main__":
    m1 = 10 ** 9 + 7
    m2 = 10 ** 9 + 9
    x = random.randint(1, 10 ** 9)
    print(*solve(), sep="\n")
