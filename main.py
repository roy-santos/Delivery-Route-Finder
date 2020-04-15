# Roy Santos, StudentID: 001186453
from datetime import datetime

import route_simulator
from models.truck import Truck
from utilities.data_loader import hash_loader, graph_loader

# Initialize hash table and graph with data from CSV files
hash_table = hash_loader('WGUPS_Package_File.csv', 40)
adjacency_list_graph = graph_loader('WGUPS_Distance_Table.csv')

# Load trucks with packages
truck1 = Truck()
truck1.load_truck(hash_table)
print()
truck2 = Truck()
truck2.load_truck(hash_table)
print()


# ALGO TESTING - DELETE LATER
#truck1.run_route(adjacency_list_graph)
#truck1.load_truck(hash_table)
#truck1.run_route(adjacency_list_graph)  #--- Does not work
truck2.run_route(adjacency_list_graph)
print(truck1.location, truck2.location)
print(truck1.distance_traveled, truck2.distance_traveled)
hash_table.print_table()


# User interface.
def user_int_prompt():
    try:
        return int(input("Select from the following:\n"
                         "1 - Look up Package ID\n"
                         "2 - Print All Packages\n"
                         "3 - Set start time\n"
                         "4 - End program\n\n"
                         "Enter Command: "))
    except ValueError:
        pass


time_set = datetime.strptime('8:00AM', '%I:%M%p').time()

while True:
    print()
    print('Current simulation time:',time_set)
    user_int = user_int_prompt()
    print()
    if user_int == 1:
        package_id = int(input('Enter package ID: '))
        print(hash_table.search(package_id))
        print()
    elif user_int == 2:
        hash_table.print_table()
        print()
    elif user_int == 3:
        time_set = datetime.strptime(input('Enter start time (HH:MM): '), '%H:%M').time()
        print()
    elif user_int == 4:
        print('Goodbye!')
        break
    else:
        print('Invalid command!')
        print()
