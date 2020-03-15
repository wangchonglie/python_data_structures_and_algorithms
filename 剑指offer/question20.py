"""
顺时针打印矩阵
输入一个矩阵, 按照从外向里以顺时针的顺序依次打印出每一个数字。
例如:
1   2   3   4
5   6   7   8
9   10  11  12
13  14  15  16
则依次打印出数字1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 10, 11
"""


def print_matrix_clockwisely(numbers):
    if not numbers:
        return
    rows = len(numbers)  # 行
    columns = len(numbers[0])  # 列
    start = 0
    while columns > start * 2 and rows > start * 2:
        print_matrix_incircle(numbers, columns, rows, start)
        start += 1
    print("\n---------------------------------")


def print_matrix_incircle(numbers, columns, rows, start):
    end_x = columns - 1 - start
    end_y = rows - 1 - start

    # 从左到右打印一行(必须打印的一行)
    for i in range(start, end_x + 1):
        num = numbers[start][i]
        print(num, end=' ')
    # 从上到下打印一列(终止行号大于起始行号)
    if start < end_y:
        for i in range(start + 1, end_y + 1):
            num = numbers[i][end_x]
            print(num, end=' ')
    # 从右到左打印一行(圈内至少有两行两列, 即终止行号大于起始行号, 且终止列号大于起始列号)
    if end_y > start and end_x > start:
        for i in range(end_x - 1, start - 1, -1):
            num = numbers[end_y][i]
            print(num, end=' ')
    # 从下到上打印一列(圈内至少有三行两列, 即终止行号比起始行号大2, 且终止列号大于起始列号)
    if end_y - 1 > start and end_x > start:
        for i in range(end_y - 1, start, -1):
            num = numbers[i][start]
            print(num, end=' ')


def test_print_matrix_clockwisely():
    # 测试空数组
    t = []
    print_matrix_clockwisely(t)
    # 测试数组只有一行
    t = [[1, 2, 3, 4]]
    print_matrix_clockwisely(t)

    # 测试数组只有一列
    t = [[1], [2], [3], [4]]
    print_matrix_clockwisely(t)
    # 测试数组只有一行一列
    t = [[1]]
    print_matrix_clockwisely(t)
    # 测试数组多行多列
    t = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    print_matrix_clockwisely(t)


test_print_matrix_clockwisely()
