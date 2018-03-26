from pprint import pprint
import string
from random import randrange

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

INF = Inf()


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

    def __len__(self):
        return self.size

    def __getitem__(self, key):
        return self._data[key]

    def __str__(self):
        return "%s" % self._data

    def edge(self, source, dest, weight):
        self._data[source][dest] = weight


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


def make_edge(am, s, d, w):
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
