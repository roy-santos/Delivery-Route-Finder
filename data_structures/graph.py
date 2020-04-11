# Adjacency list graph representation


# Vertex class to represent locations and their adjacent locations
import operator


class Vertex:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.neighbors = []

    def add_neighbor(self, neighbor, distance):
        if neighbor not in self.neighbors:
            self.neighbors.append((neighbor, distance))
            self.neighbors.sort(key=operator.itemgetter(1))


class Graph:
    vertices = {}

    def add_vertex(self, vertex):
        if type(vertex) == Vertex and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            return True
        else:
            return False

    def add_edge(self, vertex1, vertex2, distance):
        if vertex1 in self.vertices and vertex2 in self.vertices:
            self.vertices[vertex1].add_neighbor(vertex2, distance)
            self.vertices[vertex2].add_neighbor(vertex1, distance)
            return True
        else:
            return False

    def print_graph(self):
        for key in sorted(list(self.vertices.keys())):
            print(key + ' ' + str(self.vertices[key].neighbors))
