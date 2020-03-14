from deque1 import Deque


class Stack(object):
    def __init__(self):
        self.deque = Deque()

    def push(self, value):
        return self.deque.append(value)

    def pop(self):
        return self.deque.pop()

    def __len__(self):
        return len(self.deque)

    def is_empty(self):
        return len(self) == 0


def test_stack():
    s = Stack()
    s.push(0)
    s.push(1)
    s.push(2)

    assert s.pop() == 2
    assert s.pop() == 1
    assert s.pop() == 0
    import pytest  # pip install pytest
    with pytest.raises(Exception) as excinfo:  # 我们来测试是否真的抛出了异常
        s.pop()
    assert 'empty' in str(excinfo.value)


if __name__ == '__main__':
    test_stack()
