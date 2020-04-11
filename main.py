# Roy Santos, StudentID: 001186453

import csv
from models.package import *
from data_structures.hash import *
from data_structures.graph import *


# Create a hash table to store packages. Amount of packages to deliver is known to be 40.
package_hash_table = HashTable(40)

# Fill hash table with package data from CSV file
with open('WGUPS_Package_File.csv', encoding='utf-8=sig') as package_csv_file:
    csv_reader = csv.reader(package_csv_file, delimiter=',')
    for row in csv_reader:
        package = Package(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
        package_hash_table.insert(package)

for index in range(0,41):
    print(package_hash_table.search(index))


print()
# Create graph structure to hold locations(vertices) and distances (edges)
adjacency_list = Graph()

with open('WGUPS_Distance_Table.csv', encoding='utf-8=sig') as distance_csv_file:
    csv_reader = csv.reader(distance_csv_file, delimiter=',')

    # Add all vertices to the graph
    for count, row in enumerate(csv_reader, 0):
        if count > 0:
            adjacency_list.add_vertex(Vertex(row[0], row[1]))

with open('WGUPS_Distance_Table.csv', encoding='utf-8=sig') as distance_csv_file:
    csv_reader = csv.reader(distance_csv_file, delimiter=',')

    location = []
    # Add all edges to the graph
    for count, row in enumerate(csv_reader, 0):
        column = 2
        if count == 0:
            while column < len(row):
                location.append(row[column])
                column += 1
        else:
            while column < len(row) and row[column] != '0':
                adjacency_list.add_edge(row[0], location[column - 2], float(row[column]))
                column += 1
        column += 1

adjacency_list.print_graph()

