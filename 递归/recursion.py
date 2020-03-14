def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)


def print_num(n):
    for i in range(1, n + 1):
        print(i)


def print_num_recursive(n):
    if n > 0:
        print_num_recursive(n - 1)
        print(n)


def print_num_recursive_revserve(n):
    if n > 0:
        print(n)
        print_num_recursive(n - 1)


def print_num_use_stack(n):
    from stack1 import Stack
    s = Stack()
    while n > 0:
        s.push(n)
        n -= 1

    while not s.is_empty():
        print(s.pop())


def hanoi_move(n, source, dest, intermediate):
    if n >= 1:  # 递归出口, 只剩一个盘子
        hanoi_move(n - 1, source, intermediate, dest)
        print(f"Move {source} -> {dest}")  # 移动一个的时候不用递归
        hanoi_move(n - 1, intermediate, dest, source)


def hanoi_move2(n, source, dest, intermediate):
    if n == 1:
        print(f"Move {source} -> {dest}")
    else:
        hanoi_move2(n - 1, source, intermediate, dest)
        hanoi_move2(1, source, dest, intermediate)
        hanoi_move2(n - 1, intermediate, dest, source)


def flatten(rec_list):
    for i in rec_list:
        if isinstance(i, list):
            for i in flatten(i):
                yield i
        else:
            yield i


assert list(flatten([[[1], 2, 3], [1, 2, 3]])) == [1, 2, 3, 1, 2, 3]
