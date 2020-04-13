#  Data loader python file used to separate data loading code from main functionality.
import csv

from data_structures.graph import Graph, Vertex
from data_structures.hash import HashTable
from models.package import Package


# Function that returns a hash table to store package information.
def hash_loader(filename, table_size=40):

    # Create hash table
    table = HashTable(table_size)

    # Fill hash table with package data from CSV file
    with open(filename, encoding='utf-8=sig') as package_csv_file:
        csv_reader = csv.reader(package_csv_file, delimiter=',')
        for row in csv_reader:
            package = Package(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
            table.insert(package)

    return table


# Function that returns a graph data structure for holding locations (vertices) and distances (edges) to adjacent
# locations.
def graph_loader(filename):

    # Create graph
    graph = Graph()

    # Add all vertices to the graph. O(N) runtime complexity
    with open(filename, encoding='utf-8=sig') as distance_csv_file:
        csv_reader = csv.reader(distance_csv_file, delimiter=',')

        for count, row in enumerate(csv_reader, 0):
            if count > 0:
                graph.add_vertex(Vertex(row[0], row[1], row[2]))

    # Add all edges to the graph. O(N) runtime complexity
    with open(filename, encoding='utf-8=sig') as distance_csv_file:
        csv_reader = csv.reader(distance_csv_file, delimiter=',')

        location = []
        for count, row in enumerate(csv_reader, 0):
            column = 2
            if count == 0:
                while column < len(row):
                    location.append(row[column])
                    column += 1
            else:
                while column < len(row) and row[column] != '0':
                    graph.add_edge(row[0], location[column - 2], float(row[column]))
                    column += 1
            column += 1
    return graph
