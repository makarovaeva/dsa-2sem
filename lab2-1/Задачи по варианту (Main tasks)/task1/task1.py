import time
import tracemalloc

def main():
    with open("input.txt") as inp:
        n, w = map(int, inp.readline().split())
        data = [tuple(map(int, inp.readline().split())) for _ in range(n)]
    unit_prices = [p / w for p, w in data]
    ind = sorted(list(range(n)), key=lambda i: unit_prices[i], reverse=True)
    sorted_data = [data[i] for i in ind]
    result = 0
    for price, weight in sorted_data:
        if w <= 0:
            break
        result += min(weight, w) * (price / weight)
        w -= weight
    with open("output.txt", "w") as out:
        out.write(f"{result:.4f}")

if __name__ == "__main__":
    t_start = time.time()
    main()
    print(f"Время работы программы: {time.time() - t_start}")
    tracemalloc.start()
    main()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    print(f"Текущий объем памяти: {current / 2 ** 20} Mбайт, максимальный объем выделенной памяти: {peak / 2 ** 20} Mбайт\n")