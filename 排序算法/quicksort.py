def quicksort(seq):
    if len(seq) <= 1:
        return seq
    else:
        pivot_index = 0  # 默认第0个元素为主元
        left_half = [elem for elem in seq[pivot_index + 1:] if elem <= seq[pivot_index]]
        right_half = [elem for elem in seq[pivot_index + 1:] if elem > seq[pivot_index]]
        return quicksort(left_half) + [seq[pivot_index]] + quicksort(right_half)


def test_quick_sort():
    import random
    seq = list(range(10))
    random.shuffle(seq)
    print(seq)
    new_seq = quicksort(seq)
    print(new_seq)
    assert new_seq == list(range(10))


# test_quick_sort()

def partition(seq, beg, end):
    """
    将序列分隔为两部分, 并返回主元位置
    """
    pivot_index = beg
    pivot = seq[pivot_index]
    left = beg + 1
    right = end - 1
    while True:
        while left <= right and seq[right] >= pivot:
            right -= 1
        while left <= right and seq[left] < pivot:
            left += 1
        if left > right:
            break
        else:
            seq[left], seq[right] = seq[right], seq[left]
    seq[pivot_index], seq[right] = seq[right], seq[pivot_index]
    return right


def test_partition():
    l = [4, 1, 2, 8]
    assert partition(l, 0, len(l)) == 2
    l = [1, 2, 3, 4]
    assert partition(l, 0, len(l)) == 0
    l = [4, 3, 2, 1]
    assert partition(l, 0, len(l)) == 3
    l = [1]
    assert partition(l, 0, len(l)) == 0
    l = [2, 1]
    assert partition(l, 0, len(l)) == 1
    l = [6, 1, 2, 5, 4, 3, 9, 7, 10, 8]
    assert partition(l, 0, len(l)) == 5


# test_partition()


def quicksort_inplace(seq, beg, end):
    if beg < end:
        pivot_index = partition(seq, beg, end)
        quicksort_inplace(seq, beg, pivot_index)
        quicksort_inplace(seq, pivot_index + 1, end)


def test_quicksort_inplace():
    import random
    seq = list(range(10))
    random.shuffle(seq)
    seq = [6, 6, 1, 2, 7, 9, 3, 4, 5, 10, 8]
    sorted_seq = sorted(seq)
    quicksort_inplace(seq, 0, len(seq))
    assert seq == sorted_seq


# test_quicksort_inplace()
print(quicksort_inplace([3, 5, 2, 7, 6, 4, 9], 0, 7))
