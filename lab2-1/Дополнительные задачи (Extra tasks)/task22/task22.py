import time
import tracemalloc


def solve(M, N):
    if M * N > 30:
        return 0

    # Транспонируем для минимальной ширины
    if M < N:
        M, N = N, M

    total_masks = 1 << N

    # Предвычисляем допустимые переходы между масками
    transitions = [[] for _ in range(total_masks)]
    for mask1 in range(total_masks):
        for mask2 in range(total_masks):
            valid = True
            # Проверяем все квадраты 2x2
            for col in range(N - 1):
                # Берем биты из двух строк
                b11 = (mask1 >> col) & 1
                b12 = (mask1 >> (col + 1)) & 1
                b21 = (mask2 >> col) & 1
                b22 = (mask2 >> (col + 1)) & 1
                if b11 == b12 == b21 == b22:
                    valid = False
                    break
            if valid:
                transitions[mask1].append(mask2)

    dp = [1] * total_masks  # первая строка
    for _ in range(1, M):
        new_dp = [0] * total_masks
        for prev_mask in range(total_masks):
            if dp[prev_mask] == 0:
                continue
            for curr_mask in transitions[prev_mask]:
                new_dp[curr_mask] += dp[prev_mask]
        dp = new_dp

    return sum(dp)

def main():
    with open("input.txt") as inp:
        m, n = map(int, inp.readline().split())
    result = solve(m, n)
    with open("output.txt", "w") as out:
        out.write(str(result))

if __name__ == "__main__":
    t_start = time.time()
    main()
    print(f"Время работы программы: {time.time() - t_start}")
    tracemalloc.start()
    main()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    print(f"Текущий объем памяти: {current / 2 ** 20} Mбайт, максимальный объем выделенной памяти: {peak / 2 ** 20} Mбайт\n")
