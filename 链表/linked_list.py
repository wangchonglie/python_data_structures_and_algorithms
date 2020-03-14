class Node(object):
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class LinkedList(object):
    """ 链接表 ADT
    [root] -> [node0] -> [node1] -> [node2]
    """

    def __init__(self, maxsize=None):
        """
        :param maxsize: int or None, 如果是 None，无限扩充
        """
        self.maxsize = maxsize
        self.root = Node()
        self.tailnode = None
        self.length = 0

    def __len__(self):
        return self.length

    def append(self, value):
        if self.maxsize is not None and self.length > self.maxsize:
            raise Exception('链表已超过最大容量!')
        node = Node(value)
        tailnode = self.tailnode
        if tailnode is None:  # 说明此链表还没有append过
            self.root.next = node
        else:
            tailnode.next = node
        self.tailnode = node
        self.length += 1

    def appendleft(self, value):
        if self.length == 0:
            self.append(value)
        else:
            self.length += 1
            if self.maxsize is not None and self.length > self.maxsize:
                raise Exception('链表已超过最大容量!')
            node = Node(value)
            node.next = self.root.next
            self.root.next = node

    def __iter__(self):
        for node in self.iter_node():
            yield node.value

    def iter_node(self):
        """遍历 从 head 节点到 tail 节点"""
        cur_node = self.root.next
        while cur_node is not None:
            # print('111', cur_node.value)
            yield cur_node
            cur_node = cur_node.next
        if cur_node is not None:
            # print('222', cur_node.value)
            yield cur_node

    def remove(self, value):  # O(n)
        """ 删除包含值的一个节点，将其前一个节点的 next 指向被查询节点的下一个即可
        :param value:
        """
        cur_node = self.root.next
        if cur_node.value == value:
            self.root.next = cur_node.next
            self.length -= 1
            return 1
        while cur_node is not None:
            if cur_node.next and cur_node.next.value == value:
                cur_node.next = cur_node.next.next
                self.length -= 1
                return 1
            cur_node = cur_node.next
        return -1

    def find(self, value):  # O(n)
        """ 查找一个节点，返回序号，从 0 开始
        :param value:
        """
        cur_node = self.root.next
        num = 0
        while cur_node is not None:
            if cur_node.next is not None and cur_node.next.value == value:
                num += 1
                return num
            cur_node = cur_node.next
            num += 1
        return -1

    def popleft(self):  # O(1)
        """ 删除第一个链表节点
        """
        if self.length <= 1:
            self.root.next = None
            self.length -= 1
            self.tailnode = None
            return None
        cur_node = self.root.next
        self.root.next = cur_node.next
        self.length -= 1
        return cur_node.value

    def clear(self):
        self.root.next = None
        self.length = 0
        self.tailnode = None

    # def reverse(self):
    #     """将单链表储存为数组，然后按照数组的索引逆序进行反转。"""
    #     values = []
    #     for value in self.iter_node():
    #         values.append(value.value)
    #     self.root.next = None
    #     self.length = 0
    #     for i in range(len(values) - 1, -1, -1):
    #         self.append(values[i])

    # def reverse(self):
    #     """使用前节点, 当前节点, 下一节点, 逐个将节点反转。"""
    #     cur_node = self.root.next
    #     prev_node = None
    #     while cur_node is not None:
    #         next_node = cur_node.next
    #         cur_node.next = prev_node
    #
    #         if next_node is None:
    #             # 此时已经到达尾节点
    #             self.root.next = cur_node
    #         # 前面已经反转完成, 此时更新新的节点信息
    #         prev_node = cur_node
    #         cur_node = next_node

    def reverse(self):
        """从第一个节点之后, 将后续的所有节点都添加到链表的第二个节点位置, 直至最后将头节点添加到尾节点处"""
        cur_node = self.root.next
        self.tailnode = cur_node
        cur_node = cur_node.next
        while cur_node.next is not None:
            next_node = cur_node.next
            cur_node.next = next_node.next
            next_node.next = self.tailnode.next
            self.tailnode.next = next_node
        res = []
        for j in self.iter_node():
            res.append(j.value)
        print("最终的res:", res)
        cur_node.next = self.root  # 围绕成环
        self.root = cur_node.next.next  # 将单链表更新为从节点的第二个开始
        cur_node.next = Node(self.tailnode.value)   # 断掉环



def test_linked_list():
    ll = LinkedList()

    ll.append(0)
    ll.append(1)
    ll.append(2)
    ll.append(3)
    assert len(ll) == 4
    assert ll.find(2) == 2
    assert ll.find(-1) == -1

    assert ll.remove(0) == 1
    assert ll.remove(10) == -1
    assert ll.remove(2) == 1
    assert len(ll) == 2
    assert list(ll) == [1, 3]
    assert ll.find(0) == -1

    ll.appendleft(0)
    assert list(ll) == [0, 1, 3]
    assert len(ll) == 3

    headvalue = ll.popleft()
    assert headvalue == 0
    assert len(ll) == 2
    assert list(ll) == [1, 3]

    assert ll.popleft() == 1
    assert list(ll) == [3]
    ll.popleft()
    assert len(ll) == 0
    assert ll.tailnode is None

    ll.clear()
    assert len(ll) == 0
    assert list(ll) == []


def test_linked_list_remove():
    ll = LinkedList()
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.append(6)
    ll.append(7)
    ll.remove(7)
    print(list(ll))


def test_linked_list_reverse():
    ll = LinkedList()
    n = 10
    for i in range(n):
        ll.append(i)
    ll.reverse()
    # for i in ll:
    #     print(i)
    print(list(ll))
    print(list(reversed(range(n))))
    assert list(ll) == list(reversed(range(n)))


def test_linked_list_append():
    ll = LinkedList()
    ll.appendleft(1)
    ll.append(2)
    assert list(ll) == [1, 2]


if __name__ == '__main__':
    # test_linked_list()
    # test_linked_list_remove()
    # test_linked_list_append()
    test_linked_list_reverse()
