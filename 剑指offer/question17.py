"""
合并两个排序的链表
输入两个递增排序的链表, 合并这两个链表并使新链表中的结点仍然是按照递增排序的。
"""
from linked_list import LinkedList


def merge(link1, link2):
    if link1.next is None:
        return link2
    if link2.next is None:
        return link1
    link1 = link1.next
    link2 = link2.next
    new_link = LinkedList()
    cur_node = new_link.root
    while link1 and link2:
        if link1.value < link2.value:
            cur_node.next = link1
            link1 = link1.next
        else:
            cur_node.next = link2
            link2 = link2.next
        cur_node = cur_node.next
    if link1:
        cur_node.next = link2
    if link2:
        cur_node.next = link2
    return new_link


def rec_merge(link1, link2):
    if link1.next is None:
        return link2
    if link2.next is None:
        return link1
    link1 = link1.next
    link2 = link2.next
    new_link = LinkedList()
    # cur_node = new_link.root
    if link1.value < link2.value:
        new_link = link1
        link1.next = merge(link1.next, link2)
    else:
        new_link = link2
        link2.next = merge(link1, link2.next)
    print(new_link)
    return new_link


def test_merge():
    # 测试link1为空链表
    link1 = LinkedList()
    link2 = LinkedList()
    link2.append(1)
    assert merge(link1.root, link2.root) == link2.root

    # 测试link2为空链表
    link1 = LinkedList()
    link1.append(1)
    link2 = LinkedList()
    assert merge(link1.root, link2.root) == link1.root

    # 测试两个空链表
    link1 = LinkedList()
    link2 = LinkedList()
    assert merge(link1.root, link2.root) == link2.root

    # 测试两个完整的链表
    link1 = LinkedList()
    link2 = LinkedList()
    link1.append(1)
    link1.append(3)
    link2.append(2)
    link2.append(4)
    link2.append(4)
    link2.append(5)
    assert list(merge(link1.root, link2.root)) == [1, 2, 3, 4, 4, 5]


def test_rec_merge():
    # 测试link1为空链表
    link1 = LinkedList()
    link2 = LinkedList()
    link2.append(1)
    assert rec_merge(link1.root, link2.root) == link2.root

    # 测试link2为空链表
    link1 = LinkedList()
    link1.append(1)
    link2 = LinkedList()
    assert rec_merge(link1.root, link2.root) == link1.root

    # 测试两个空链表
    link1 = LinkedList()
    link2 = LinkedList()
    assert rec_merge(link1.root, link2.root) == link2.root

    # 测试两个完整的链表
    link1 = LinkedList()
    link2 = LinkedList()
    link1.append(1)
    link1.append(3)
    link2.append(2)
    link2.append(4)
    link2.append(4)
    link2.append(5)
    print(rec_merge(link1.root, link2.root).value)
    print(rec_merge(link1.root, link2.root).value)
    # assert list(rec_merge(link1.root, link2.root)) == [1, 2, 3, 4, 4, 5]


test_merge()
test_rec_merge()
