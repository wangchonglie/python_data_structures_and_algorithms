def merge_sort(seq):
    if len(seq) <= 1:
        return seq
    else:
        # 分解
        mid = len(seq) // 2
        left_elem = merge_sort(seq[:mid])
        right_elem = merge_sort(seq[mid:])
        # 合并
        new_seq = merge_list(left_elem, right_elem)
        return new_seq


def merge_list(list_a, list_b):
    lenth_a = len(list_a)
    lenth_b = len(list_b)
    a = b = 0  # 双指针
    res = []
    while a < lenth_a and b < lenth_b:
        if list_a[a] < list_b[b]:
            res.append(list_a[a])
            a += 1
        else:
            res.append(list_b[b])
            b += 1
    if a < lenth_a:
        res.extend(list_a[a:])
    else:
        res.extend(list_b[b:])
    return res


def test_merge_sort():
    import random
    seq = list(range(10))
    random.shuffle(seq)
    print(seq)
    new_seq = merge_sort(seq)
    assert new_seq == list(range(10))


test_merge_sort()
