from pprint import pprint
import string
from random import randrange
import math

xrange = range

class Inf(int):
    def __str__(self):
        return 'Inf'

    def __repr__(self):
        return 'I'

    def __lt__(self, other):
        return False

    def __gt__(self, other):
        return True

    def __eq__(self, other):
        return type(self) == type(other)

    def __ne__(self, other):
        return type(self) != type(other)

INF = float('inf')


def dist(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def square_matrix(n, value):
    return [
        [
            value for _ in xrange(n)
        ] for _ in xrange(n)
    ]


class AdjacencyMatrix:
    def __init__(self, node_count):
        self.size = node_count
        self._data = square_matrix(node_count, INF)
        self._nodes = []

    def __len__(self):
        return self.size

    def __getitem__(self, key):
        return self._data[key]

    def __call__(self, key):
        return self._nodes[key]

    def __str__(self):
        return "%s" % self._data

    def edge(self, source, dest, weight=None):
        if weight is None:
            n1 = self._nodes[source]
            n2 = self._nodes[dest]
            weight = dist(n1, n2)

        self._data[source][dest] = weight

    def node(self, node):
        """insert nodes in order. a=0, b=2, ..."""
        self._nodes.append(node)



def breadth_first(graph, start):
    size = graph.size
    graph = graph
    queue = [(None, start, 0)]
    visited = [False for _ in xrange(graph.size)]
    visited[start] = True
    while len(queue) > 0:
        prev, current, w = queue.pop(0)

        for child in xrange(size):
            weight = graph._data[current][child]
            if weight != INF and not visited[child]:
                visited[child] = True
                queue.append((current, child, weight))

        yield prev, current, w


def make_edge(am, s, d, w=None):
    am.edge(d, s, w)
    am.edge(s, d, w)


if __name__ == '__main__':
    am = AdjacencyMatrix(10)


    make_edge(am, 0, 1, 1)
    make_edge(am, 1, 2, 2)
    make_edge(am, 2, 3, 1)
    make_edge(am, 2, 6, 2)
    make_edge(am, 2, 5, 5)
    make_edge(am, 3, 5, 3)
    make_edge(am, 3, 4, 3)
    make_edge(am, 3, 7, 7)
    make_edge(am, 6, 7, 1)
    make_edge(am, 6, 9, 0)
    make_edge(am, 7, 9, 1)
    make_edge(am, 9, 8, 1)

    pprint(am._data)

    for node in breadth_first(am, 0):
        print(node)
