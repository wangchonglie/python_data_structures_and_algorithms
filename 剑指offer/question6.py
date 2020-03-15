"""
重建二叉树
输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建出如下图所示的二叉树并输出它的头结点。
"""
from btree import BinTree


def construct(preorder, inorder):
    if not preorder or not inorder:
        return False
    return construct_core(preorder, 0, len(preorder) - 1, inorder, 0, len(inorder) - 1)


def construct_core(preorder, start_preorder, end_preorder, inorder, start_inorder, end_inorder):
    """
    先根据前序遍历序列的第一个数字创建根结点，接下来在中序遍历序列中找到根结点的位置，
    这样就能确定左、右子树结点的数量。在前序遍历和中序遍历的序列中划分了左、右子树结
    点的值之后，就可以递归地去分别构建它的左右子树。
    :param preorder:
    :param start_preorder:
    :param end_preorder:
    :param inorder:
    :param start_inorder:
    :param end_inorder:
    :return:
    """
    # 前序遍历的第一个数字是根结点的值
    root_value = preorder[start_preorder]
    root = BinTree(root=root_value)
    root.left = root.right = None
    root.data = root.root
    if start_preorder == end_preorder:
        if start_inorder == end_inorder and inorder[start_inorder] == inorder[end_inorder]:
            return root
        else:
            raise Exception("错误的输入")

    # 在中序遍历中找到根结点的值
    root_inorder = start_inorder
    while root_inorder <= end_inorder and inorder[root_inorder] != root_value:
        root_inorder += 1
    # 如果两个序列不匹配
    if root_inorder == end_inorder and inorder[root_inorder] != root_value:
        raise Exception("两个序列不匹配!", root_value, inorder[root_value])
    left_length = root_inorder - start_inorder
    left_preorder_end = start_preorder + left_length
    # 构建左子树
    if left_length > 0:
        root.left = construct_core(preorder, start_preorder + 1, left_preorder_end, inorder, start_inorder,
                                   root_inorder - 1)
    # 构建右子树
    if left_length < end_preorder - start_preorder:
        # root.right = construct_core(preorder, left_preorder_end + 1, end_preorder, inorder, root_inorder + 1,
        #                             end_inorder)
        root.right = construct_core(preorder, left_preorder_end + 1, end_preorder, inorder, root_inorder + 1,
                                    end_inorder)
    return root


def test_construct():
    seq1 = [1, 2, 4, 7, 3, 5, 6, 8]
    seq2 = [4, 7, 2, 1, 5, 3, 8, 6]
    btree = construct(seq1, seq2)
    print('*', btree)
    tmp = BinTree()
    tmp.preorder_trav(btree)


test_construct()
