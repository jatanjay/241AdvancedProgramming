"""
File : Graph.py
auth = Jatan Pandya
ECE 241 / C2/P2
references :bogotobogo.com/python_graph_data_structures.php and ZYBooks, Chapter : Python Graphs
"""
from vertex import Vertex


class Graph:
    """
    Graph, which holds the master list of vertices
    """

    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0

    def add_vertex(self, node):
        self.num_vertices += 1
        new_vertex = Vertex(node)
        self.vert_dict[node] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

    def __iter__(self):
        return iter(self.vert_dict.values())

    def __contains__(self, n):
        return n in self.vert_dict

    def add_edge(self, from_vertex, to_vertex, cost=0):
        """
        Basically first it sees if Leon Lai is in vert_dict - if not -- create, skips the need to explicitly create
        vertex obj (see conditions)
        same goes with Nick Ingman
        Next, add Nick Ingman as Leon Lai's neighbor with cost
        """
        if from_vertex not in self.vert_dict:
            self.add_vertex(from_vertex)
        if to_vertex not in self.vert_dict:
            self.add_vertex(to_vertex)
        self.vert_dict[from_vertex].add_neighbor(self.vert_dict[to_vertex], cost)

    def get_vertices(self):
        return self.vert_dict.keys()


class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def getSize(self):
        return len(self.items)
