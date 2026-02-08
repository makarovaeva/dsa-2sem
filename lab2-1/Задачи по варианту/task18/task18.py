import time
import tracemalloc


def main():
    with open("input.txt") as inp:
        n = int(inp.readline())
        prices = [int(inp.readline()) for _ in range(n)]
    # k1 - кол-во купонов оставшихся, k2 - кол-во использованных купонов
    result = k1 = k2 = 0
    days = []
    for i in range(n):
        if k1 == 0:
            result += prices[i]
            k1 += (prices[i] > 100)
        else:
            if prices[i] > 100 or k1 >= n - (i + 1):
                k1 -= 1
                k2 += 1
                days.append(i + 1)
            else:
                result += prices[i]
    with open("output.txt", "w") as out:
        out.write(f"{result}\n{k1} {k2}\n")
        out.write("\n".join(map(str, days)))

if __name__ == "__main__":
    t_start = time.time()
    main()
    print(f"Время работы программы: {time.time() - t_start}")
    tracemalloc.start()
    main()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    print(f"Текущий объем памяти: {current / 2 ** 20} Mбайт, максимальный объем выделенной памяти: {peak / 2 ** 20} Mбайт\n")




