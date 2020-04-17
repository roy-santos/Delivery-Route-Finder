# Graph data structure class that utilizes adjacency lists.
import operator


# Vertex class used to represent locations on the map. Holds a list of neighboring locations.
class Vertex:
    # Initialize vertex with the name, address, and adjacent vertices.
    def __init__(self, name, address, location_zip):
        self.name = name
        self.address = address
        self.location_zip = location_zip
        self.neighbors = []

    # Function that adds adjacent vertices and the distance to that vertex as a tuple.
    def add_neighbor(self, neighbor, distance):
        if neighbor not in self.neighbors:
            self.neighbors.append((neighbor, distance))
            # Sort neighbors list by distance
            self.neighbors.sort(key=operator.itemgetter(1))


# Graph data structure class which holds vertices.
class Graph:
    # Dictionary data structure holds vertices.
    vertices = {}

    # Function that tells the program how to iterate through the graph class.
    def __iter__(self):
        return iter(self.vertices)

    # Function that adds vertices to the vertices dictionary. O(1) runtime complexity.
    def add_vertex(self, vertex):
        if type(vertex) == Vertex and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            return True
        else:
            return False

    # Function that adds weighted edges by adding a neighbor to both vertices provided. O(1) runtime complexity.
    def add_edge(self, vertex1, vertex2, distance):
        if vertex1 in self.vertices and vertex2 in self.vertices and distance != 0:
            self.vertices[vertex1].add_neighbor(vertex2, distance)
            self.vertices[vertex2].add_neighbor(vertex1, distance)
            return True
        else:
            return False

    # Function that prints all vertices in the dictionary. O(N) runtime complexity.
    def print_graph(self):
        for key in sorted(list(self.vertices.keys())):
            print(key + ' ' + str(self.vertices[key].neighbors))


