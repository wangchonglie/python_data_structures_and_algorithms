class Node(object):
    __slots__ = ('value', 'prev', 'next')  # save memory

    def __init__(self, value=None, prev=None, next=None):
        self.value, self.prev, self.next = value, prev, next


class CircularDoubleLinkedList(object):
    """循环双端链表 ADT
    多了个循环其实就是把 root 的 prev 指向 tail 节点，串起来
    """

    def __init__(self, maxsize=None):
        self.maxsize = maxsize
        node = Node()
        node.next, node.prev = node, node
        self.root = node
        self.length = 0

    def __len__(self):
        return self.length

    def headnode(self):
        return self.root.next

    def tailnode(self):
        return self.root.prev

    def append(self, value):  # O(1), 你发现一般不用 for 循环的就是 O(1)，有限个步骤
        self.length += 1
        if self.maxsize is not None and self.length > self.maxsize:
            raise Exception('超过容量了!')
        tailnode = self.tailnode()
        node = Node(value)
        node.next = tailnode.next
        tailnode.next = node
        node.prev = tailnode
        self.root.prev = node

    def appendleft(self, value):
        self.length += 1
        if self.maxsize is not None and self.length > self.maxsize:
            raise Exception('超过容量了!')
        headnode = self.headnode()
        node = Node(value)
        node.next = headnode
        node.prev = headnode.prev
        headnode.prev = node
        self.root.next = node

    def remove(self, node):  # O(1)，传入node 而不是 value 我们就能实现 O(1) 删除
        if node is self.root:
            return
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
        self.length -= 1
        return node

    def iter_node(self):
        cur_node = self.root.next
        while cur_node != self.tailnode():
            yield cur_node
            cur_node = cur_node.next
        if cur_node.value is not None:
            yield cur_node

    def __iter__(self):
        for node in self.iter_node():
            yield node.value

    def iter_node_reverse(self):
        """相比单链表独有的反序遍历"""
        cur_node = self.root.prev
        while cur_node != self.headnode():
            yield cur_node
            cur_node = cur_node.prev
        if cur_node.value is not None:
            yield cur_node


def test_double_link_list():
    dll = CircularDoubleLinkedList()
    assert len(dll) == 0

    dll.append(0)
    dll.append(1)
    dll.append(2)

    assert list(dll) == [0, 1, 2]

    assert [node.value for node in dll.iter_node()] == [0, 1, 2]
    print([node.value for node in dll.iter_node_reverse()])
    assert [node.value for node in dll.iter_node_reverse()] == [2, 1, 0]

    headnode = dll.headnode()
    assert headnode.value == 0
    dll.remove(headnode)
    assert len(dll) == 2
    assert [node.value for node in dll.iter_node()] == [1, 2]

    dll.appendleft(0)
    assert [node.value for node in dll.iter_node()] == [0, 1, 2]


if __name__ == '__main__':
    test_double_link_list()
