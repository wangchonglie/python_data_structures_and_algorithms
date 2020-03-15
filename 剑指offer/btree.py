from collections import deque


class Stack2(object):
    def __init__(self):
        self._items = deque()

    def push(self, value):
        return self._items.append(value)

    def pop(self):
        return self._items.pop()

    def empty(self):
        return len(self._items) == 0


class Stack(object):
    def __init__(self):
        self._items = list()

    def push(self, value):
        return self._items.append(value)

    def pop(self):
        return self._items.pop()

    def empty(self):
        return len(self._items) == 0

    def peek(self):
        if not self.empty():
            return self._items[len(self._items) - 1]


class Queue(object):
    def __init__(self):
        self._items = deque()

    def append(self, value):
        return self._items.append(value)

    def pop(self):
        return self._items.popleft()

    def empty(self):
        return len(self._items) == 0


class BinTreeNode(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class BinTree(object):
    def __init__(self, root=None):
        self.root = root

    @classmethod
    def build_from(cls, node_list):
        """
        :param node_list: {'data': 'A', 'left': None, 'right': None, 'is_root': False}
        """
        node_dict = dict()
        for node_data in node_list:
            data = node_data['data']
            node_dict[data] = BinTreeNode(data)
        for node_data in node_list:
            data = node_data['data']
            node = node_dict[data]
            if node_data['is_root']:
                root = node
            node.left = node_dict.get(node_data['left'])
            node.right = node_dict.get(node_data['right'])
        return cls(root)  # 用root 初始化这个类并返回一个对象

    def add(self, elem):
        """为树添加节点"""
        node = BinTreeNode(elem)
        # 如果树是空的，则对根节点赋值
        if self.root is None:
            self.root = node

        else:
            queue = [self.root]
            # 对已有的节点进行层次遍历
            while queue:
                # 弹出队列的第一个元素
                cur = queue.pop(0)
                if cur.left is None:
                    cur.left = node
                    return
                elif cur.right is None:
                    cur.right = node
                    return
                else:
                    # 如果左右子树都不为空，加入队列继续判断
                    queue.append(cur.left)
                    queue.append(cur.right)

    def preorder_trav(self, subtree):
        """
        先序遍历
        """
        if subtree is not None:
            print(subtree.data, end=' ')  # 递归函数里先处理根
            self.preorder_trav(subtree.left)  # 递归处理左子树
            self.preorder_trav(subtree.right)  # 递归处理右子树

    def preorder_trav_use_stack(self, subtree):
        """
        用栈的方式实现先序遍历
        """
        s = Stack()
        if subtree:
            s.push(subtree)
            while not s.empty():
                top_node = s.pop()
                print(top_node.data)
                if top_node.right:
                    s.push(top_node.right)
                if top_node.left:
                    s.push(top_node.left)

    def inorder_trav(self, subtree):
        """
        中序遍历
        """
        if subtree is not None:
            self.inorder_trav(subtree.left)
            print(subtree.data)
            self.inorder_trav(subtree.right)

    def inorder_trav_use_stack(self, subtree):
        """
        用栈的方式实现中序遍历
        1. 先判断当前节点是否还有左子节点, 有的话则将当前节点更新为其左节点;
        2. 更新到最底层的左节点将其弹出, 然后将其值更新为右节点(右节点此时为空, 所以会输出根节点, 然后将节点更新为树的右节点)
        """
        s = Stack()
        cur_node = subtree
        while cur_node or not s.empty():
            while cur_node:
                s.push(cur_node)  # 压栈
                cur_node = cur_node.left  # 切换到左节点上
            cur_node = s.pop()  # 当前栈顶已经是最底层的左节点了，取出栈顶元素，访问该节点
            print(cur_node.data)
            cur_node = cur_node.right  # 添加右节点

    def postorder_trav(self, subtree):
        """
        后序遍历
        """
        if subtree is not None:
            self.postorder_trav(subtree.left)
            self.postorder_trav(subtree.right)
            print(subtree.data)

    def postorder_trav_use_stack(self, subtree):
        """
        用栈的方式实现后序遍历
        """
        s = Stack()
        cur_node = subtree
        prev_node = None
        while cur_node or not s.empty():
            while cur_node:
                s.push(cur_node)  # 添加根节点
                cur_node = cur_node.left  # 递归添加左节点
            cur_node = s.peek()  # 获得栈顶元素
            # 在不存在右节点或者右节点已经访问过的情况下, 访问根节点
            if not cur_node.right or cur_node.right == prev_node:
                print(cur_node.data)
                prev_node = cur_node
                cur_node = None
                s.pop()
            # 右节点没有访问过就先访问右节点
            else:
                cur_node = cur_node.right

    def postorder_trav_use_two_stack(self, subtree):
        """
        双栈法实现后序遍历
        """
        s = Stack()
        result = Stack()
        if subtree:
            s.push(subtree)
            while not s.empty():
                top_node = s.pop()
                result.push(top_node)
                # print(top_node.data)
                if top_node.left:
                    s.push(top_node.left)
                if top_node.right:
                    s.push(top_node.right)
            while not result.empty():
                cur_node = result.pop()
                print(cur_node.data)

    def layer_trav(self, subtree):
        if not subtree:
            return
        cur_nodes = [subtree]  # 当前层的所有节点
        next_nodes = []  # 保存下一层的所有节点
        # while cur_nodes:  # todo: 这种应该就可以了, 待测试
        while cur_nodes or next_nodes:
            for node in cur_nodes:
                print(node.data)
                if node.left:
                    next_nodes.append(node.left)
                if node.right:
                    next_nodes.append(node.right)
            cur_nodes = next_nodes  # 移交节点到下一层
            next_nodes = []

    def layer_trav_use_queue(self, subtree):
        if not subtree:
            return
        q = Queue()
        q.append(subtree)
        while not q.empty():
            cur_node = q.pop()
            print(cur_node.data)
            if cur_node.left:
                q.append(cur_node.left)
            if cur_node.right:
                q.append(cur_node.right)


if __name__ == '__main__':
    node_list = [
        {'data': 'A', 'left': 'B', 'right': 'C', 'is_root': True},
        {'data': 'B', 'left': 'D', 'right': 'E', 'is_root': False},
        {'data': 'D', 'left': None, 'right': None, 'is_root': False},
        {'data': 'E', 'left': 'H', 'right': None, 'is_root': False},
        {'data': 'H', 'left': None, 'right': None, 'is_root': False},
        {'data': 'C', 'left': 'F', 'right': 'G', 'is_root': False},
        {'data': 'F', 'left': None, 'right': None, 'is_root': False},
        {'data': 'G', 'left': 'I', 'right': 'J', 'is_root': False},
        {'data': 'I', 'left': None, 'right': None, 'is_root': False},
        {'data': 'J', 'left': None, 'right': None, 'is_root': False},
    ]

    btree = BinTree.build_from(node_list)
    print('====先序遍历=====')
    btree.preorder_trav(btree.root)
    print('==栈方式==先序遍历=====')
    btree.preorder_trav_use_stack(btree.root)
    print('====中序遍历=====')
    btree.inorder_trav(btree.root)
    print('==栈方式==中序遍历=====')
    btree.inorder_trav_use_stack(btree.root)
    print('====后序遍历=====')
    btree.postorder_trav(btree.root)
    print('==栈方式==后序遍历=====')
    btree.postorder_trav_use_stack(btree.root)
    print('==双栈法==后序遍历=====')
    btree.postorder_trav_use_two_stack(btree.root)
    print('====层序遍历=====')
    btree.layer_trav(btree.root)
    print('====层序遍历==队列方式===')
    btree.layer_trav_use_queue(btree.root)
