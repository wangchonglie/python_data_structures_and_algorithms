"""
反转链表
定义一个函数, 输入一个链表的头结点, 反转该链表并输出反转后链表的头结点。
"""
from linked_list import LinkedList


def reverse_link(link):
    reversed_head = None
    cur_node = link.root
    prev = None
    while cur_node is not None:
        p_next = cur_node.next
        if p_next is None:
            reversed_head = cur_node
        cur_node.next = prev
        prev = cur_node
        cur_node = p_next
    print(reversed_head.value)
    return reversed_head.value


def test_reverse_link():
    # 输入的是一个空指针
    link = LinkedList()
    assert reverse_link(link) is None

    # 输入的链表只有一个结点
    link = LinkedList()
    link.append(1)
    assert reverse_link(link) == 1

    # 输入的链表有多个结点
    link = LinkedList()
    link.append(1)
    link.append(2)
    link.append(3)
    link.append(4)
    link.append(5)
    link.append(6)
    assert reverse_link(link) == 6


test_reverse_link()
