"""
二叉树中和为某一值的路径
输入一棵二叉树和一个整数, 打印出二叉树中结点值的和为输入整数的所有路径。
从树的根节点往下一直到叶结点所经过的结点形成一条路径。
"""
from btree import BinTree


def find_path(btree, expected_sum):
    if btree is None:
        return
    cur_sum = 0
    path = []
    find_path_helper(btree, cur_sum, path, expected_sum)


def find_path_helper(btree, cur_sum, path, expected_sum):
    cur_sum += btree.data
    path.append(btree.data)

    # 叶子结点
    if btree.left is None and btree.right is None:
        if cur_sum == expected_sum:
            print(f'{expected_sum}路径为:', end=' ')
            for elem in path:
                print(elem, end=' ')
            print()

    # 如果不是叶子结点, 则遍历它的子结点
    if btree.left is not None:
        find_path_helper(btree.left, cur_sum, path, expected_sum)
    if btree.right is not None:
        find_path_helper(btree.right, cur_sum, path, expected_sum)
    # 在返回到父结点前, 在路径上删除当前结点
    path.pop()


def test_find_path():
    btree = BinTree()
    btree.add(10)
    btree.add(5)
    btree.add(12)
    btree.add(4)
    btree.add(7)
    find_path(btree.root, 22)
    find_path(btree.root, 17)


test_find_path()
