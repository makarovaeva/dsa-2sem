import time
import tracemalloc

def largest_number(digits):
    answer = ""
    while digits:
        max_digit = digits[0]
        for digit in digits:
            if digit + max_digit >= max_digit + digit:
                max_digit = digit
        answer += max_digit
        digits.remove(max_digit)
    return answer

def main():
    with open("input.txt") as inp, open("output.txt", "w") as out:
        n = int(inp.readline())
        data = inp.readline().split()
        out.write(largest_number(data))

if __name__ == "__main__":
    t_start = time.time()
    main()
    print(f"Время работы программы: {time.time() - t_start}")
    tracemalloc.start()
    main()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    print(f"Текущий объем памяти: {current / 2 ** 20} Mбайт, максимальный объем выделенной памяти: {peak / 2 ** 20} Mбайт\n")