import random

from time_memory_decorator import time_memory_decorator


def hash_table(h, m, s):
    for i in range(1, len(s) + 1):
        h[i] = (x * h[i - 1] + ord(s[i - 1])) % m


def get_hash(h, idx, l, m):
    return (h[idx + l] - x ** l * h[idx]) % m


@time_memory_decorator
def solve():
    with open("input_task4.txt") as inp:
        s = inp.readline().strip()
        q = int(inp.readline())
        req = [tuple(map(int, inp.readline().split())) for _ in range(q)]

    n = len(s)
    h1 = [0] * (n + 1)
    h2 = [0] * (n + 1)
    hash_table(h1, m1, s)
    hash_table(h2, m2, s)
    answer = []

    for a, b, l in req:
        if get_hash(h1, a, l, m1) == get_hash(h1, b, l, m1) and \
                get_hash(h2, a, l, m2) == get_hash(h2, b, l, m2):
            answer.append("YES")
        else:
            answer.append("NO")

    return answer


if __name__ == '__main__':
    m1 = 10 ** 9 + 7
    m2 = 10 ** 9 + 9
    x = random.randint(1, 10 ** 9)
    print(*solve(), sep="\n")
