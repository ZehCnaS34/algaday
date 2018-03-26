"""
Min Heap
"""
import math
import string


class HeapMap:
    def __init__(self):
        self.size = 0
        self._data = [None for _ in range(5)]
        self._map = {}
        self._ensure_space()

    def __getitem__(self, key):
        return self._data[self._map[key]]

    def __nonzero__(self):
        return self.size != 0

    def __str__(self):
        return "%s" % (
            [
                (string.ascii_lowercase[i], v) for i, v in self._data[:self.size]
            ]
        )

    def __repr__(self):
        return "%s" % (self._data)

    def _ensure_space(self):
        if self.size >= len(self._data):
            self._data += [None for _ in range(self.size)]

    def parentI(self, x):
        return (x-1) // 2

    def hasParent(self, x):
        return self.parentI(x) > -1

    def parent(self, x):
        return self._data[self.parentI(x)]

    def leftI(self, x):
        return 2 * x + 1

    def left_child(self, x):
        return self._data[self.leftI(x)]

    def has_left_child(self, cursor):
        try:
            # print(self.data[self.leftI(cursor)] is not None)
            return self._data[self.leftI(cursor)] is not None
        except Exception, _:
            return False

    def rightI(self, x):
        return 2 * x + 2

    def right_child(self, x):
        return self._data[self.rightI(x)]

    def add(self, key, value):
        self._map[key] = self.size
        self.size += 1
        self._ensure_space()
        self._data[self.size-1] = (key, value)
        return self.up()

    def contains(self, key):
        return key in self._map

    def extract_min(self):
        assert self.size != 0
        item = self._data[0]
        del self._map[item[0]]
        self._data[0] = self._data[self.size - 1]
        self._data[self.size - 1] = None
        self.size -= 1
        self.down()
        return item

    def swap(self, x, y):
        self._data[x], self._data[y] = self._data[y], self._data[x]
        self._map[self._data[x][0]] = x
        self._map[self._data[y][0]] = y

    def up(self, cursor=None):
        if cursor is None:
            cursor = self.size - 1

        while self.hasParent(cursor) and self._data[cursor][1] < self.parent(cursor)[1]:
            self.swap(self.parentI(cursor), cursor)
            cursor = self.parentI(cursor)

    def down(self):
        cursor = 0

        while self.has_left_child(cursor):
            smaller_child = self.leftI(cursor)
            if self._data[self.rightI(cursor)] and self.right_child(cursor)[1] < self._data[smaller_child][1]:
                smaller_child = self.rightI(cursor)

            if self._data[cursor][1] < self._data[smaller_child][1]:
                break
            else:
                self.swap(smaller_child, cursor)
                cursor = smaller_child

    def decrease(self, key, value):
        cursor = self._map[key]

        if value < self._data[cursor][1]:
            self._data[cursor] = (key, value)
            self.up(cursor)


if __name__ == '__main__':
    from random import randrange
    hm = HeapMap()

    kvs = [(l, randrange(100)) for l in range(10)]

    for k, v in kvs:
        hm.add(k, v)

    print hm
