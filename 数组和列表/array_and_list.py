class Array(object):
    def __init__(self, size=32):
        self.size = size
        self.items = [None] * size

    def __getitem__(self, index):
        return self.items[index]

    def __setitem__(self, index, value):
        self.items[index] = value

    def __len__(self):
        return self.size

    def clear(self, value=None):
        for i in range(self.size):
            self.items[i] = value

    def __iter__(self):
        for item in range(self.size):
            yield self.items[item]


if __name__ == '__main__':
    size = 10
    a = Array(size)
    a[0] = 1
    a[1] = 2
    a[2] = 3
    a[3] = 4

    assert a[0] == 1

    # a.clear(value=9)
    for i in a:
        print(i)