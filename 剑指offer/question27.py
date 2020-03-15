"""
二叉搜索树与双向链表
输入一棵二叉搜索树, 将该二叉搜索树转换成一个排序的双向链表。
要求不能创建任何新的结点, 只能调整书中结点指针的指向。
"""
from btree import BinTree


def convert(btree):
    if not btree:
        return None
    if not btree.left and not btree.right:
        return btree

    # 将左子树构建成双链表, 返回链表头
    # btree是叶结点, left是叶子结点的值
    left = convert(btree.left)
    p = left

    # 定位至左子树的最右的一个结点
    while left and p.right:
        p = p.right

    # 如果左子树不为空, 将当前btree加到左子树链表
    if left:
        p.right = btree
        btree.left = p

    # 将右子树构造成双链表, 返回链表头
    right = convert(btree.right)
    # 如果右子树不为空, 将该链表追加到btree结点之后
    if right:
        right.left = btree
        btree.right = right

    return left or btree


def test_convert():
    btree = BinTree()
    btree.add(10)
    btree.add(6)
    btree.add(14)
    btree.add(4)
    btree.add(8)
    btree.add(12)
    btree.add(16)
    convert(btree.root)


test_convert()
