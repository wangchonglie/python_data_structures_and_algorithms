from hashtable import HashTable


class DictADT(HashTable):

    def _iter_slot(self):
        for slot in self._table:
            if slot not in (HashTable.EMPTY, HashTable.UNUSED):
                yield slot

    def __setitem__(self, key, value):
        self.add(key, value)

    def __getitem__(self, key, default=None):
        return self.get(key, default)

    def items(self):
        for slot in self._iter_slot():
            yield (slot.key, slot.value)

    def keys(self):
        for slot in self._iter_slot():
            yield slot.key

    def values(self):
        for slot in self._iter_slot():
            yield slot.value


def test_dict_adt():
    import random
    d = DictADT()

    d['a'] = 1
    assert d['a'] == 1
    d.remove('a')

    l = list(range(30))
    random.shuffle(l)
    for i in l:
        d.add(i, i)

    for i in range(30):
        assert d.get(i) == i

    assert sorted(list(d.keys())) == sorted(l)


test_dict_adt()
