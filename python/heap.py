"""
Min Heap
"""
import math

class MinHeap:
    def __init__(self):
        self.size = 0
        self.cursor = -1
        self.data = [None for _ in range(5)]
        self._resize()

    def __str__(self):
        return "%s:%s" % (self.size, self.data)
    
    def _resize(self):
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

    def insert(self, value):
        self.cursor += 1
        self.size += 1
        self._resize()
        self.data[self.cursor] = value
        self.up()

    def poll(self):
        assert self.size != 0
        item = self.data[0]
        self.data[0] = self.data[self.cursor]
        self.data[self.cursor] = None
        self.size -= 1
        self.cursor -= 1
        self.down()
        return item
        

    def swap(self, x, y):
        self.data[x], self.data[y] = self.data[y], self.data[x]

    def up(self):
        cursor = self.cursor
        while self.hasParent(cursor) and self.data[cursor] < self.parent(cursor):
            self.data[self.parentI(cursor)], self.data[cursor] = (
                self.data[cursor],
                self.data[self.parentI(cursor)]
            )
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

def heap_sort(arr):
    output = []
    h = MinHeap()
    for e in arr:
        h.insert(e)
    
    while h.size > 0:
        output.append(h.poll())

    return output

if __name__ == '__main__':
    import random
    i = [random.randrange(0, 100) for _ in range(20)]
    o = heap_sort(i)
    print(i)
    print(o)