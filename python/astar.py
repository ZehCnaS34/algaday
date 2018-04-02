
import graph
from graph import AdjacencyMatrix, breadth_first, make_edge, INF
from pprint import pprint
# from heap import MinHeap
from heapmap import HeapMap

from string import ascii_lowercase


def create_matrix():
    am = AdjacencyMatrix(10)

    am.node((3, 2))
    am.node((9, 2))
    am.node((5, 4))
    am.node((8, 4))
    am.node((8, 6))
    am.node((4, 8))
    am.node((10, 10))
    am.node((7, 11))
    am.node((10, 12))
    am.node((4, 13))

    make_edge(am, 0, 1)
    make_edge(am, 0, 2)
    make_edge(am, 1, 3)
    make_edge(am, 2, 3)
    make_edge(am, 2, 4)
    make_edge(am, 3, 4)
    make_edge(am, 3, 5)
    make_edge(am, 4, 5)
    make_edge(am, 4, 6)
    make_edge(am, 4, 7)
    make_edge(am, 5, 7)
    make_edge(am, 5, 9)
    make_edge(am, 6, 8)
    make_edge(am, 7, 8)
    make_edge(am, 7, 9)

    return am


def astar(am, source, dest):
    node_parent = {source: None}
    # first, distance from parent
    # second, distance from dest.
    node_distance = {source: 0}
    heap_map = HeapMap()

    for node in range(len(am)):
        heap_map.add(node, INF)

    heap_map.decrease(source, 0)

    while heap_map:
        current, _ = heap_map.extract_min()
        node_distance[current] = node_distance[current]

        for child in xrange(len(am)):
            distance = am[current][child]

            if distance == INF or not heap_map.contains(child):
                continue

            total_distance = distance + node_distance[current]
            heuristic_distance = total_distance + graph.dist(am(child), am(dest))
            if heap_map[child][1] > heuristic_distance:
                node_parent[child] = current
                node_distance[child] = total_distance
                heap_map.decrease(child, heuristic_distance)
                print heap_map

    return node_parent, node_distance


if __name__ == '__main__':
    m = create_matrix()

    np, nd = astar(m, 0, 9)

    print "path"
    for n in np:
        p = ascii_lowercase[np[n]] if np[n] is not None else None
        print(ascii_lowercase[n], p)

    print "distance"
    for n in nd:
        print(ascii_lowercase[n], nd[n])
