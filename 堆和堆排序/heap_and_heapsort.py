class MaxHeap(object):
    def __init__(self, maxsize=10):
        self.maxsize = maxsize
        self._elements = [None] * maxsize
        self._count = 0

    def __len__(self):
        return self._count

    def add(self, value):
        if self._count >= self.maxsize:
            raise Exception('full')
        self._elements[self._count] = value  # 插入到最后一位
        self._siftup(self._count)  # 维持堆的特性
        self._count += 1

    def _siftup(self, ndx):
        """
        从下往上维持堆的特性
        """
        if ndx > 0:
            parent = int((ndx - 1) / 2)
            if self._elements[ndx] > self._elements[parent]:  # 如果插入的值大于parent, 一直交换
                self._elements[ndx], self._elements[parent] = self._elements[parent], self._elements[ndx]
                self._siftup(parent)  # 递归维持堆的特性

    def extract(self):
        if self._count <= 0:
            raise Exception('Empty')
        value = self._elements[0]
        self._count -= 1
        self._elements[0] = self._elements[self._count]  # 最右下的节点放到root位置后siftDown
        self._siftdown(0)  # 维持堆的特性
        return value

    def _siftdown(self, ndx):
        """
        从上往下维持堆的特性
        """
        left = 2 * ndx + 1
        right = 2 * ndx + 2
        # 找出最大值
        if left < self._count and self._elements[left] >= self._elements[ndx]:
            largest = left
        else:
            largest = ndx
        if right < self._count and self._elements[right] >= self._elements[largest]:
            largest = right
        if largest != ndx:
            self._elements[ndx], self._elements[largest] = self._elements[largest], self._elements[ndx]
            self._siftdown(largest)


def test_maxheap():
    import random
    n = 5
    h = MaxHeap(n)
    for i in range(n):
        h.add(i)
    for i in reversed(range(n)):
        assert i == h.extract()


def heapsort_reverse(array):
    length = len(array)
    maxheap = MaxHeap(length)
    for i in array:
        maxheap.add(i)
    res = []
    for i in range(length):
        res.append(maxheap.extract())
    return res


def test_heapsort_reverse():
    import random
    l = list(range(10))
    random.shuffle(l)
    assert heapsort_reverse(l) == sorted(l, reverse=True)


def heapsort_use_heapq(iterable):
    from heapq import heappush, heappop
    items = []
    for value in iterable:
        heappush(items, value)
    return [heappop(items) for i in range(len(items))]


def test_heapsort_use_heapq():
    import random
    l = list(range(10))
    random.shuffle(l)
    assert heapsort_use_heapq(l) == sorted(l)


test_maxheap()
test_heapsort_reverse()
test_heapsort_use_heapq()
