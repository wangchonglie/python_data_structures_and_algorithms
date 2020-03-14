from collections import deque

from linked_list import LinkedList


class EmptyError(Exception):
    pass


class Queue(object):
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self._item_link_list = LinkedList()

    def __len__(self):
        return len(self._item_link_list)

    def push(self, value):  # O(1)
        """ 队尾添加元素 """
        self._item_link_list.append(value)

    def pop(self):
        """队列头部删除元素"""
        if len(self) <= 0:
            raise EmptyError("队列已空!")
        self._item_link_list.popleft()


class Queue2(object):
    """
    使用 collections.deque 可以迅速实现一个队列
    """

    def __init__(self):
        self.items = deque()

    def append(self, val):
        return self.items.append(val)

    def pop(self):
        return self.items.popleft()

    def __len__(self):
        return len(self.items)

    def empty(self):
        return len(self.items) == 0

    def front(self):
        return self.items[0]
