"""
Min Heap
"""
import math

class HeapMap:
    def __init__(self):
        self.size = 0
        self.data = [None for _ in range(5)]
        self._map = {}
        self._ensure_space()

    def __str__(self):
        return "%s:%s" % (self.size, self.data)

    def _ensure_space(self):
        if self.size >= len(self.data):
            self.data += [None for _ in range(self.size)]

    def parentI(self, x):
        return (x-1) // 2

    def hasParent(self, x):
        return self.parentI(x) > -1

    def parent(self, x):
        return self.data[self.parentI(x)]

    def leftI(self, x):
        return 2 * x + 1

    def left_child(self, x):
        return self.data[self.leftI(x)]

    def has_left_child(self, cursor):
        try:
            # print(self.data[self.leftI(cursor)] is not None)
            return self.data[self.leftI(cursor)] is not None
        except Exception, a:
            return False

    def rightI(self, x):
        return 2 * x + 2

    def right_child(self, x):
        return self.data[self.rightI(x)]

    def add(self, key, value):
        self.size += 1
        self._ensure_space()
        self.data[self.size-1] = (key, value)
        return self.up()

    def contains(self, key):
        return key in self._map

    def extract_min(self):
        assert self.size != 0
        item = self.data[0]
        self.data[0] = self.data[self.cursor]
        self.data[self.cursor] = None
        self.size -= 1
        self.down()
        return item


    def swap(self, x, y):
        self.data[x], self.data[y] = self.data[y], self.data[x]
        self.map[self.data[x][0]] = x
        self.map[self.data[y][0]] = y

    def up(self):
        cursor = self.cursor
        while self.hasParent(cursor) and self.data[cursor] < self.parent(cursor):
            self.swap(self.parentI(cursor), cursor)
            cursor = self.parentI(cursor)

    def down(self):
        cursor = 0

        while self.has_left_child(cursor):
            smaller_child = self.leftI(cursor)
            if self.data[self.rightI(cursor)] and self.right_child(cursor) < self.data[smaller_child]:
                smaller_child = self.rightI(cursor)

            if self.data[cursor] < self.data[smaller_child]:
                break
            else:
                self.swap(smaller_child, cursor)
                cursor = smaller_child

    def contains(self):
        pass

    def decrease(self):
        pass


if __name__ == '__main__':
    hm = HeapMap()
