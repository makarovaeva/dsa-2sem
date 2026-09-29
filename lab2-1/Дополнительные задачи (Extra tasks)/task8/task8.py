import time
import tracemalloc

def main():
    with open("input.txt") as inp:
        n = int(inp.readline())
        data = [tuple(map(int, inp.readline().split())) for _ in range(n)]
    # сортируем по времени окончания
    data.sort(key=lambda x: x[1])
    count = last_end = 0
    for start, end in data:
        if start >= last_end:
            count += 1
            last_end = end

    with open("output.txt", "w") as out:
        out.write(str(count))

if __name__ == "__main__":
    t_start = time.time()
    main()
    print(f"Время работы программы: {time.time() - t_start}")
    tracemalloc.start()
    main()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    print(f"Текущий объем памяти: {current / 2 ** 20} Mбайт, максимальный объем выделенной памяти: {peak / 2 ** 20} Mбайт\n")
