import time
import tracemalloc

def in_order(root):
    key, left, right = root
    if left != -1:
        in_order(tree[left])
    in_order_result.append(key)
    if right != -1:
        in_order(tree[right])

def pre_order(root):
    key, left, right = root
    pre_order_result.append(key)
    if left != -1:
        pre_order(tree[left])
    if right != -1:
        pre_order(tree[right])

def post_order(root):
    key, left, right = root
    if left != -1:
        post_order(tree[left])
    if right != -1:
        post_order(tree[right])
    post_order_result.append(key)

def main(root):
    in_order(root)
    pre_order(root)
    post_order(root)

if __name__ == "__main__":
    with open("input.txt") as inp:
        n = int(inp.readline())
        tree = [tuple(map(int, inp.readline().split())) for _ in range(n)]
    in_order_result = []
    pre_order_result = []
    post_order_result = []
    t_start = time.time()
    main(tree[0])
    print(f"Время работы программы: {time.time() - t_start}")
    with open("output.txt", "w") as out:
        out.write(" ".join(map(str, in_order_result)) + "\n")
        out.write(" ".join(map(str, pre_order_result)) + "\n")
        out.write(" ".join(map(str, post_order_result)) + "\n")
    tracemalloc.start()
    main(tree[0])
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    print(f"Текущий объем памяти: {current / 2 ** 20} Mбайт, максимальный объем выделенной памяти: {peak / 2 ** 20} Mбайт\n")
