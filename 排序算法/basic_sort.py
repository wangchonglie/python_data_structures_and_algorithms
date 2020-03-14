import random


def bubble_sort(seq):
    n = len(seq)
    for i in range(n - 1):
        flag = True
        print(seq)
        for j in range(n - 1 - i):
            if seq[j] > seq[j + 1]:
                seq[j], seq[j + 1] = seq[j + 1], seq[j]
                flag = False
        if flag:
            break


def test_bubble_sort():
    seq = list(range(10))
    random.shuffle(seq)
    print("seq", seq)
    bubble_sort(seq)
    assert seq == sorted(seq)


def select_sort(seq):
    n = len(seq)
    for i in range(n - 1):
        min_value = seq[i]
        for j in range(i + 1, n):
            if seq[j] < min_value:
                min_value = seq[j]
        seq[i] = min_value


def test_select_sort():
    seq = list(range(10))
    random.shuffle(seq)
    print("seq", seq)
    select_sort(seq)
    assert seq == sorted(seq)


def insertion_sort(seq):
    n = len(seq)
    for i in range(1, n):
        value = seq[i]
        pos = i
        while pos > 0 and value < seq[pos - 1]:
            seq[pos] = seq[pos - 1]
            pos -= 1
        seq[pos] = value


def insertion_sort2(alist):
    # 从第二个位置，即下标为1的元素开始向前插入
    for i in range(1, len(alist)):
        # 从第i个元素开始向前比较，如果小于前一个元素，交换位置
        for j in range(i, 0, -1):
            if alist[j] < alist[j - 1]:
                alist[j], alist[j - 1] = alist[j - 1], alist[j]


def test_insertion_sort():
    seq = list(range(10))
    random.shuffle(seq)
    insertion_sort2(seq)
    assert seq == sorted(seq)


# test_bubble_sort()
# test_select_sort()
test_insertion_sort()
