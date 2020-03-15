"""
面试题3:
在一个二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
"""
test = [
    [1, 2, 8, 9],
    [2, 4, 9, 12],
    [4, 7, 10, 13],
    [6, 8, 11, 15]
]


def check_exist(l, num):
    if not l:
        return False
    row = [i for i in range(len(l))]	# 行数
    col = [i for i in range(len(l[0]))]	# 列数
    while row and col:
        if l[row[0]][col[-1]] == num:
            return True
        # 如果右上角的数大于目标数, 则这一列就排除
        elif l[row[0]][col[-1]] > num:
            col = col[:-1]
        # 如果右上角的数小于目标数, 则这一行就排除
        else:
            row = row[1:]
    return False

print(check_exist(test, 15))
