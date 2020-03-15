"""
链表中倒数第K个节点
输入一个链表, 输出该链表中倒数第k个结点。为了符合大多数人的习惯, 本题从1开始计数, 即链表的尾节点是倒数第一个结点。
例如一个链表有6个结点, 从头结点开始他们的值依次是1、2、3、4、5、6。这个链表的倒数第3个结点是值为4的结点。
"""
from linked_list import LinkedList


def find_kth_from_tail(data, k):
    # 由于计数是从1开始的, 所以0也当作是无效输入
    if not data or k == 0:
        return None
    ahead = data.root
    behind = data.root
    for i in range(k - 1):
        if ahead.next is not None:
            ahead = ahead.next
        else:
            return None
    while ahead.next is not None:
        ahead = ahead.next
        behind = behind.next
    return behind.value


def test_find_kth_from_tail():
    data = LinkedList()
    data.append(1)
    data.append(2)
    data.append(3)
    data.append(4)
    data.append(5)
    data.append(6)
    assert find_kth_from_tail(data, 1) == 6
    assert find_kth_from_tail(data, 2) == 5
    assert find_kth_from_tail(data, 3) == 4
    assert find_kth_from_tail(data, 4) == 3
    assert find_kth_from_tail(data, 5) == 2
    assert find_kth_from_tail(data, 6) == 1
    assert find_kth_from_tail(data, 7) is None


test_find_kth_from_tail()
