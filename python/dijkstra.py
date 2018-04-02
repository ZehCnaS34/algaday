from graph import AdjacencyMatrix, breadth_first, make_edge, INF
from pprint import pprint
# from heap import MinHeap
from heapmap import HeapMap

from string import ascii_lowercase

def create_matrix():
    am = AdjacencyMatrix(6)

    make_edge(am, 0, 1, 5)
    make_edge(am, 0, 3, 9)
    make_edge(am, 0, 4, 2)

    make_edge(am, 1, 2, 2)

    make_edge(am, 2, 3, 3)

    make_edge(am, 4, 5, 3)
    
    make_edge(am, 5, 3, 2)

    return am


def dijkstra(am, source):
    node_parent = { source: None }
    node_distance = { source: 0}
    heap_map = HeapMap()
    for node in range(len(am)):
        heap_map.add(node, INF)
    
    heap_map.decrease(source, 0)


    while heap_map:
        print heap_map
        current, dist = heap_map.extract_min()
        print current, dist
        node_distance[current] = dist
        
        for child in xrange(len(am)):
            distance = am[current][child]
            if distance == INF or not heap_map.contains(child):
                continue

            total_distance = distance + node_distance[current]
            if total_distance < heap_map[child]:
                node_parent[child] = current
                heap_map.decrease(child, total_distance)

            
    return node_parent, node_distance
    
if __name__ == '__main__':
    m = create_matrix()

    np, nd = dijkstra(m, 0)

    print "path"
    for n in np:
        p = ascii_lowercase[np[n]] if np[n] is not None else None
        print(ascii_lowercase[n], p)

    print "distance"
    for n in nd:
        print(ascii_lowercase[n], nd[n])
