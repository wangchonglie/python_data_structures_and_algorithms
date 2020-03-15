"""
二叉搜索树的后序遍历序列
输入一个整数数组, 判断该数组是不是某二叉搜索树的后序遍历的结果。
如果是则返回true, 否则返回false。假设输入的数组的任意两个数字都互不相同。
例如在下面的一颗二叉搜索树中，输入数组{5,7,6,9,11,10,8}，则返回true，
因为这个整数序列是下图二叉搜索树的后序遍历结果。如果输入的数组是{7,4,6,5}，
由于没有哪棵二叉搜索树的后序遍历的结果是这个序列，因此返回false。
"""


# import sys
# sys.setrecursionlimit(10000000)

def verufy_sequence_of_bst(seq):
    """
    Step1.通过取出序列最后一个元素得到二叉搜索树的根节点；
    Step2.在二叉搜索树中左子树的结点小于根结点，因此可以遍历一次得到左子树；
    Step3.在二叉搜索树中右子树的结点大于根结点，因此可以继续遍历后序元素得到右子树；
    Step4.重复以上步骤递归判断左右子树是不是二叉搜索树，如果都是，则返回true，如果不是，则返回false;
    """
    # print("seq", seq)
    if not seq:
        return False
    length = len(seq)
    root = seq[-1]
    # 在二叉搜索树中左子树的结点小于根结点
    left = 0
    for i in range(length - 1):
        if seq[i] > root:
            break
        left += 1

    # 在二叉搜索树中右子树的结点大于根结点
    for i in range(left, length - 1):
        if seq[i] < root:
            return False
    # 判断左子树是不是二叉搜索树
    left_is_bst = True
    if left > 0:
        left_is_bst = verufy_sequence_of_bst(seq[:left])
    # 判断右子树是不是二叉搜索树
    right_is_bst = True
    if left < length - 1 and left_is_bst:
        right_is_bst = verufy_sequence_of_bst(seq[left:-1])
    return left_is_bst and right_is_bst


def test_verufy_sequence_of_bst():
    seq = [5, 7, 6, 9, 11, 10, 8]
    assert verufy_sequence_of_bst(seq) is True
    seq = [7, 4, 6, 5]
    assert verufy_sequence_of_bst(seq) is False
    seq = [4, 8, 6, 12, 16, 14, 10]
    assert verufy_sequence_of_bst(seq) is True
    seq = [4, 6, 7, 5]
    assert verufy_sequence_of_bst(seq) is True
    seq = [1, 2, 3, 4, 5]
    assert verufy_sequence_of_bst(seq) is True
    # 树中只有一个结点
    seq = [5]
    assert verufy_sequence_of_bst(seq) is True
    seq = [4, 6, 12, 8, 16, 14, 10]
    assert verufy_sequence_of_bst(seq) is False
    seq = []
    assert verufy_sequence_of_bst(seq) is False


test_verufy_sequence_of_bst()
