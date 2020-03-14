from double_linked_list import CircularDoubleLinkedList


class Deque(object):

    def __init__(self):
        self.deque = CircularDoubleLinkedList()

    def append(self, value):
        self.deque.append(value)

    def appendleft(self, value):
        self.deque.appendleft(value)

    def pop(self):
        if len(self.deque) == 0:
            raise Exception('empty')
        tailnode = self.deque.tailnode()
        self.deque.remove(tailnode)
        return tailnode.value

    def popleft(self):
        if len(self.deque) == 0:
            raise Exception('empty')
        headnode = self.deque.headnode()
        self.deque.remove(headnode)
        return headnode.value

    def __len__(self):
        return len(self.deque)
