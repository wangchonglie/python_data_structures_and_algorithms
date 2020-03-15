"""
包含min函数的栈
定义栈的数据结构, 请在该类型中实现一个能够得到栈的最小元素的min函数。
在该栈中, 调用min、push及pop的时间复杂度都是O(1)。
"""


class Stack(object):
    def __init__(self):
        self.__elements = []  # 数据栈，存放栈的所有元素
        self.__helper = []  # 辅助栈，存放栈的最小元素

    def pop(self):
        value = self.__elements.pop()
        self.__helper.pop()
        return value

    def push(self, item):
        if len(self.__elements) == 0 or item < self.__helper[-1]:
            self.__helper.append(item)
        else:
            self.__helper.append(self.__helper[-1])
        self.__elements.append(item)

    def min_value(self):
        if len(self.__helper) > 0 and len(self.__elements) > 0:
            return self.__helper[-1]
        else:
            raise Exception("空栈")

    def __len__(self):
        return len(self.__elements)


def test_min():
    s = Stack()
    # 新压入栈的数字比之前的最小值大
    s.push(1)
    s.push(2)
    assert s.min_value() == 1
    # 新压入栈的数字比之前的最小值小
    s.push(-1)
    assert s.min_value() == -1
    # 弹出栈的数字不是最小的元素
    s.push(5)
    s.pop()
    assert s.min_value() == -1
    # 弹出栈的数字是最小的元素
    s.pop()
    assert s.min_value() == 1
    s.pop()
    s.pop()
    # 空栈
    print(s.min_value())


test_min()
