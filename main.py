# Roy Santos, StudentID: 001186453

import csv
from models.package import *
from data_structures.hash import *


# Create a hash table to store packages. Amount of packages to deliver is known to be 40.
package_hash_table = HashTable(40)

# Fill hash table with package data from CSV file
with open('WGUPS_Package_File.csv', encoding='utf-8=sig') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        package = Package(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
        package_hash_table.insert(package)

for index in range(0,41):
    print(package_hash_table.search(index))

print(package_hash_table.search(0))



