"""
二叉树的镜像
请完成一个函数, 输入一个二叉树, 该函数输出它的镜像。
"""
from btree import BinTree
from btree import Stack


def mirror_recursively(btree):
    if btree is None:
        return
    if btree.left is None and btree.right is None:
        return

    # 交换左右结点
    btree.left, btree.right = btree.right, btree.left

    if btree.left:
        mirror_recursively(btree.left)
    if btree.right:
        mirror_recursively(btree.right)


def mirror_use_stack(btree):
    if btree:
        s = Stack()
        s.push(btree)
        while not s.empty():
            top_node = s.pop()

            # 这两个判断交换顺序也没关系, 因为不是打印当前值
            if top_node.right:
                s.push(top_node.right)
            if top_node.left:
                s.push(top_node.left)

            if top_node.left or top_node.right:
                top_node.left, top_node.right = top_node.right, top_node.left


def test_mirror_recursively():
    # 空结点树
    tree = BinTree()
    print(mirror_recursively(tree.root))
    # 一个结点的树
    tree = BinTree()
    tree.add('A')
    mirror_recursively(tree.root)
    tree.preorder_trav(tree.root)
    # 多结点树
    tree = BinTree()
    tree.add('A')
    tree.add('B')
    tree.add('C')
    tree.add('D')
    tree.add('E')
    tree.add('F')
    tree.add('G')
    print("-------------------镜像前-------------------")
    tree.preorder_trav(tree.root)
    mirror_recursively(tree.root)
    print("-------------------镜像后-------------------")
    tree.preorder_trav(tree.root)


def test_mirror_use_stack():
    # 空结点树
    tree = BinTree()
    print(mirror_use_stack(tree.root))
    # 一个结点的树
    tree = BinTree()
    tree.add('A')
    mirror_use_stack(tree.root)
    tree.preorder_trav(tree.root)
    # 多结点树
    tree = BinTree()
    tree.add('A')
    tree.add('B')
    tree.add('C')
    tree.add('D')
    tree.add('E')
    tree.add('F')
    tree.add('G')
    print("-------------------镜像前-------------------")
    tree.preorder_trav(tree.root)
    mirror_use_stack(tree.root)
    print("-------------------镜像后-------------------")
    tree.preorder_trav(tree.root)


test_mirror_recursively()
print('----------------------------分割线----------------------------')
test_mirror_use_stack()
