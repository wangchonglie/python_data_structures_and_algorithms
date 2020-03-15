"""
输入一个整数数组, 实现一个函数来调整该数组中数字的顺序, 使得所有奇数位于数组的前半部分, 所有偶数位于数组的后半部分。
"""


def reorder(data):
    if not data:
        return
    beg = 0
    end = len(data) - 1
    while beg < end:
        # 向后移动beg指针, 直到它指向偶数
        while beg < end and not is_even(data[beg]):
            beg += 1
        # 向前移动beg指针, 直到它指向奇数
        while beg < end and is_even(data[end]):
            end -= 1
        if beg < end:
            data[beg], data[end] = data[end], data[beg]
    return data


def is_even(num):

    return num & 1 == 0

# print(is_even(2))
print(reorder([1, 2, 3, 4, 5]))
