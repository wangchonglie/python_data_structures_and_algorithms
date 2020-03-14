from heap_and_heapsort import MaxHeap


class PriorityQueue(object):
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self._maxheap = MaxHeap()

    def push(self, priority, value):
        entry = (priority, value)
        self._maxheap.add(entry)

    def pop(self, with_priority=False):
        entry = self._maxheap.extract()
        return entry if with_priority else entry[1]

    def is_empty(self):
        return len(self._maxheap) == 0


def test_priority_queue():
    size = 5
    pq = PriorityQueue(size)
    pq.push(5, 'purple')
    pq.push(0, 'white')
    pq.push(3, 'orange')
    pq.push(1, 'black')

    res = []
    while not pq.is_empty():
        res.append(pq.pop())
    assert res == ['purple', 'orange', 'black', 'white']
