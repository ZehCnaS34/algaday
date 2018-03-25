from graph import AdjacencyMatrix, breadth_first_search
# from heap import MinHeap

def create_matrix():
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


def dijkstra(am, source, dest):
    l = len(am)
    paths = {}

    q = [source]


