"""
树的子结构
输入两颗二叉树A和B, 判断B是不是A的子结构。
"""
from btree import BinTree


def has_subtree(btree1, btree2):
    res = False
    if btree1 is not None and btree2 is not None:
        if btree1.data == btree2.data:
            res = helper(btree1, btree2)
        if not res:
            res = has_subtree(btree1.left, btree2)
        if not res:
            res = has_subtree(btree1.right, btree2)
    return res


def helper(btree1, btree2):
    if btree2 is None:
        return True
    if btree1 is None:
        return False
    if btree1.data != btree2.data:
        return False

    return helper(btree1.left, btree2.left) and helper(btree1.right, btree2.right)


def test_has_subtree():
    node_list = [
        {'data': 'A', 'left': 'B', 'right': 'C', 'is_root': True},
        {'data': 'B', 'left': 'D', 'right': 'E', 'is_root': False},
        {'data': 'D', 'left': None, 'right': None, 'is_root': False},
        {'data': 'E', 'left': 'H', 'right': None, 'is_root': False},
        {'data': 'H', 'left': None, 'right': None, 'is_root': False},
        {'data': 'C', 'left': 'F', 'right': 'G', 'is_root': False},
        {'data': 'F', 'left': None, 'right': None, 'is_root': False},
        {'data': 'G', 'left': 'I', 'right': 'J', 'is_root': False},
        {'data': 'I', 'left': None, 'right': None, 'is_root': False},
        {'data': 'J', 'left': None, 'right': None, 'is_root': False},
    ]

    btree1 = BinTree.build_from(node_list)
    node_list2 = [
        {'data': 'A', 'left': 'B', 'right': 'D', 'is_root': True},
        {'data': 'B', 'left': None, 'right': None, 'is_root': False},
        {'data': 'D', 'left': None, 'right': None, 'is_root': False},
    ]

    btree2 = BinTree.build_from(node_list2)
    print(has_subtree(btree1.root, btree2.root))


test_has_subtree()
