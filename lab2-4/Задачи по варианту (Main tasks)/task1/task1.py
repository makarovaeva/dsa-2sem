from time_memory_decorator import time_memory_decorator


@time_memory_decorator
def solve():
    with open("input_task1.txt") as inp:
        p = inp.readline().strip()
        t = inp.readline().strip()
    answer = []
    for i in range(len(t) - len(p) + 1):
        if t[i: i + len(p)] == p:
            answer.append(i + 1)

    return len(answer), " ".join(map(str, answer))


if __name__ == '__main__':
    a, b = solve()
    print(a, b, sep="\n")
