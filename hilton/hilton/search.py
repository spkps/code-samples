from collections import Counter
from Queue import PriorityQueue
from itertools import ifilter


def search(graph, start, completed):
    """graph is a list of edges - tuples with linked nodes
       start is a node
       completed is a function to define the end of search

       return value is a list of nodes which 
       represent the path from start while completed doesn't return True
    """
    visited = Counter()
    history = [start]
    current = start
    visited[start] += 1

    limit = len(graph)
    counter = 0

    while not completed(current) and counter < limit:
        edge = next_edge(graph, visited, current)
        visited[edge] += 1
        current = edge[1]
        visited[current] += 1
        history.append(current)
        counter += 1

    return history


def find_neighbors(graph, current):
    return ifilter(lambda node: node[0] == current, graph)


def next_edge(graph, counter, current):
    q = PriorityQueue()
    for n in find_neighbors(graph, current):
        q.put((counter[n]+counter[n[1]], n))
    return q.get()[1]
