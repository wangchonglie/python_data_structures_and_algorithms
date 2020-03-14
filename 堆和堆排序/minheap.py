class Array(object):

    def __init__(self, size=32):
        self._size = size
        self._items = [None] * size

    def __getitem__(self, index):
        return self._items[index]

    def __setitem__(self, index, value):
        self._items[index] = value

    def __len__(self):
        return self._size

    def clear(self, value=None):
        for i in range(len(self._items)):
            self._items[i] = value

    def __iter__(self):
        for item in self._items:
            yield item


class MinHeap(object):
    def __init__(self, maxsize=None):
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
            if self._elements[ndx] < self._elements[parent]:  # 如果插入的值小于parent, 一直交换
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
        min_value = ndx
        # 找出最小值
        if (left < self._count and
                self._elements[left] <= self._elements[min_value] and
                self._elements[left] <= self._elements[right]):
            min_value = left
        elif right < self._count and self._elements[right] <= self._elements[min_value]:
            min_value = right
        if min_value != ndx:
            self._elements[ndx], self._elements[min_value] = self._elements[min_value], self._elements[ndx]
            self._siftdown(min_value)

    def top(self):
        return self._elements[0]


def test_maxheap():
    n = 5
    h = MinHeap(n)
    for i in range(n):
        h.add(i)
    for i in range(n):
        assert i == h.extract()


def heapsort_reverse(array):
    length = len(array)
    minheap = MinHeap(length)
    for i in array:
        minheap.add(i)
    res = []
    for i in range(length):
        res.append(minheap.extract())
    return res


def test_heapsort_reverse():
    import random
    l = list(range(10))
    random.shuffle(l)
    assert heapsort_reverse(l) == sorted(l, reverse=False)


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


def test_top_k(k=10):
    import random
    print()
    nums = list(range(1000))
    random.shuffle(nums)
    minheap = MinHeap(k)
    for i in range(1000):
        if i < k:
            minheap.add(nums[i])
            continue
        if nums[i] >= minheap.top():
            minheap.extract()
            minheap.add(nums[i])
    for idx in range(k):
        print(minheap.extract())
