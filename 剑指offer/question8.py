"""
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个非减排序的数组的一个旋转，输出旋转数组的最小元素。
例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。
"""


def min_number(numbers):
    length = len(numbers)
    if length <= 0:
        raise Exception("Wrong numbers!")
    idx1 = 0
    idx2 = length - 1
    idx_mid = idx1
    while numbers[idx1] >= numbers[idx2]:
        if idx2 - idx1 == 1:
            idx_mid = idx2
            break
        idx_mid = int((idx1 + idx2) / 2)
        # 如果下标idx1, idx2和idx_mid指向的三个数字相等, 则只能顺序查找
        if numbers[idx1] == numbers[idx2] == numbers[idx_mid]:
            return in_order_min(numbers, idx1, idx2)
        if numbers[idx_mid] >= numbers[idx1]:
            idx1 = idx_mid
        elif numbers[idx_mid] <= numbers[idx2]:
            idx2 = idx_mid
    return numbers[idx_mid]


def in_order_min(numbers, index1, index2):
    res = numbers[index1]
    for i in range(index1 + 1, index2 + 1):
        if res > numbers[i]:
            res = numbers[i]
    return res


def test_min_number():
    seq = [3, 4, 5, 1, 2]
    assert min_number(seq) == 1
    seq = [1, 0, 1, 1, 1]
    assert min_number(seq) == 0
    seq = [1, 1, 1, 0, 1]
    assert min_number(seq) == 0


test_min_number()
