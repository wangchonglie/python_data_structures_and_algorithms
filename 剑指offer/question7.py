"""
用两个栈实现一个队列
"""


class Stack():

    def __init__(self, maxsize=32):
        self.elements = []
        self.maxsize = maxsize

    def __len__(self):
        return len(self.elements)

    def push(self, item):
        self.elements.append(item)

    def pop(self):
        return self.elements.pop()

    def is_empty(self):
        return len(self) == 0


class Queue():

    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def delete_head(self):
        if not self.stack2.is_empty():
            return self.stack2.pop()
        else:
            while not self.stack1.is_empty():
                value = self.stack1.pop()
                self.stack2.push(value)
            return self.stack2.pop()

    def append_tail(self, item):
        self.stack1.push(item)

    def is_empty(self):
        if self.stack1.is_empty() and self.stack2.is_empty():
            return True
        else:
            return False

    def __len__(self):
        return len(self.stack1) + len(self.stack2)

"""
用两个队列实现一个栈
在push的时候，往非空的那个队列添加（刚刚初始化的时候，两个队列都为空，随便往哪个队列push都行 上图步骤1和步骤3
在pop的时候，如果队列1不为空，就把队列1中q1.size()-1个元素poll出来，添加到队列2中（上图步骤2中元素1和2），再把队列中那个最后的元素poll出来（步骤2中元素3）
这两个队列中始终有一个是空的。另一个非空。push添加元素到非空队列中，pop把非空队列中前面的元素都转移到另一个队列中，只剩最后一个元素，再把最后一个元素pop出来。这样这一个队列是空的，另一个队列又非空了。
"""


class Stack2():

    def __init__(self):
        self.queue1 = Queue()
        self.queue2 = Queue()

    def push(self, item):
        if not self.queue1.is_empty():
            self.queue1.append_tail(item)
        else:
            self.queue2.append_tail(item)

    def pop(self):
        if not self.is_empty():
            if self.queue1.is_empty():
                while len(self.queue2) > 1:
                    self.queue1.append_tail(self.queue2.delete_head())
                return self.queue2.delete_head()
            else:
                while len(self.queue1) > 1:
                    tmp = self.queue1.delete_head()
                    self.queue2.append_tail(tmp)
                return self.queue1.delete_head()

    def is_empty(self):
        return self.queue1.is_empty() and self.queue2.is_empty()


def test_stack():
    s = Stack2()
    s.push(0)
    s.push(1)
    s.push(2)
    s.push(3)
    print(s.pop())
    print('分割线')
    s.push(2)
    # print(s.pop())
    # print(s.pop())
    # print(s.pop())
    # print(s.pop())
    assert s.pop() == 2
    assert s.pop() == 2
    assert s.pop() == 1
    assert s.pop() == 0

test_stack()


def test_queue():
    q = Queue()
    q.append_tail(0)
    q.append_tail(1)
    q.append_tail(2)

    assert q.delete_head() == 0
    assert q.delete_head() == 1
    assert q.delete_head() == 2

test_queue()
