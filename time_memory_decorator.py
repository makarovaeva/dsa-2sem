import time
import tracemalloc


def time_memory_decorator(func):
    def wrapper():
        t_start = time.time()
        res = func()
        print(f"Время работы программы: {time.time() - t_start:.2f}")
        tracemalloc.start()
        func()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        print(f"Текущий объем памяти: {current / 2 ** 20:.2f} Mбайт, "
              f"максимальный объем выделенной памяти: {peak / 2 ** 20:.2f} Mбайт\n")
        return res

    return wrapper
