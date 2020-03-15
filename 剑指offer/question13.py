"""
给定单向链表的头指针和一个结点指针, 定义一个函数在O(1)时间删除该结点。
"""


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
        return node

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

    def remove(self, node):
        if self.length == 0:
            raise Exception("Empty")
        cur_node = self.root.next
        # 要删除的节点不是尾节点
        if node.next is not None:
            # tmp_node = Node()
            tmp_node = node.next
            node.value = tmp_node.value
            node.next = tmp_node.next
            self.length -= 1
            del tmp_node
            return True
        # 链表只有一个结点, 删除头结点(也是尾节点)
        elif cur_node == node:
            self.root.next = None
            self.length = 0
            self.tailnode = None
            return True
        # 链表中有多个结点, 删除尾节点
        else:
            while cur_node.next != node:
                cur_node = cur_node.next
            cur_node.next = None
            self.length -= 1
            return True


def test_linked_list_remove():
    ll = LinkedList()
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.append(6)
    node = ll.append(7)
    ll.remove(node)
    print(list(ll))

test_linked_list_remove()
