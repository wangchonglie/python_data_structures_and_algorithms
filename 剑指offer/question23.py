"""
从上往下打印二叉树
从上往下打印出二叉树的每个节点, 同一层的结点按照从左到右的顺序打印。
"""
from collections import deque

from btree import BinTree


def print_from_top_to_bottom(subtree):
    if not subtree:
        return
    q = deque()
    q.append(subtree)

    while q:
        subtree = q.popleft()
        print(subtree.data, end=' ')
        if subtree.left:
            q.append(subtree.left)
        if subtree.right:
            q.append(subtree.right)
    print('\n---------------------------------------')


def test_print_from_top_to_bottom():
    # 空树
    btree = BinTree()
    print_from_top_to_bottom(btree.root)
    # 单结点树
    btree = BinTree()
    btree.add(8)
    print_from_top_to_bottom(btree.root)
    # 多结点树
    btree = BinTree()
    btree.add(8)
    btree.add(6)
    btree.add(10)
    btree.add(5)
    btree.add(7)
    btree.add(9)
    # btree.add(11)
    print_from_top_to_bottom(btree.root)


test_print_from_top_to_bottom()
