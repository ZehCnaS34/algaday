from pprint import pprint
from random import randrange


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

    def edge(self, source, dest, weight):
        self._data[source][dest] = weight


def breadth_first_search(graph, start):
    size = graph.size
    graph = graph
    queue = [(start, 0)]
    visited = [False for _ in xrange(graph.size)]
    while len(queue) > 0:
        current, w = queue.pop(0)
        visited[current] = True

        for child in xrange(size):
            weight = graph._data[current][child]
            if weight != INF and not visited[child]:
                queue.append((child, weight))

        yield current, w


if __name__ == '__main__':
    am = AdjacencyMatrix(5)

    pprint(am._data)
    am.edge(0, 3, 4)

    for node in breadth_first_search(am, 0):
        pass
