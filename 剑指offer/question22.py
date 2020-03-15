"""
栈的压入、弹出序列
输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否可能为该栈的弹出顺序。
假设压入栈的所有数字均不相等。例如序列1,2,3,4,5是某栈的压入顺序，序列4,5,3,2,1是该压栈序列对应的一个弹出序列，
但4,3,5,1,2就不可能是该压栈序列的弹出序列。
"""


def is_pop_order(list1, list2):
    if not list1 or not list2:
        return False
    helper = []  # 辅助栈
    while list1:
        # 将压栈序列依次存入辅助栈中
        helper.append(list1.pop(0))
        # 每轮判断出栈序列的的栈顶元素是否与辅助栈的出栈元素相等
        # 相等则同时将辅助栈和出栈序列出栈(出栈序列的栈顶元素在list2[0]位置)
        while True:
            if list2 and helper[-1] == list2[0]:
                helper.pop()
                list2.pop(0)
            else:
                break
    # 当压栈序列依次存入辅助栈后, 如果经过处理后, 辅助栈为空, 则为真, 否则为假
    return False if helper else True


def test_is_pop_order():
    t1 = [1, 2, 3, 4, 5]
    t2 = [4, 5, 3, 2, 1]
    assert is_pop_order(t1, t2) is True
    t1 = [1, 2, 3, 4, 5]
    t2 = [4, 3, 5, 1, 2]
    assert is_pop_order(t1, t2) is False
    # 输入两个空序列
    t1 = []
    t2 = []
    assert is_pop_order(t1, t2) is False
    t1 = [1]
    t2 = [1]
    assert is_pop_order(t1, t2) is True
    t1 = [1]
    t2 = [2]
    assert is_pop_order(t1, t2) is False


test_is_pop_order()
