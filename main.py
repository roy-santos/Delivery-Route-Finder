# Roy Santos, StudentID: 001186453
import route_simulator
from models.truck import Truck
from utilities.data_loader import hash_loader, graph_loader

# Initialize hash table and graph with data from CSV files
hash_table = hash_loader('WGUPS_Package_File.csv', 40)
adjacency_list_graph = graph_loader('WGUPS_Distance_Table.csv')


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


truck1 = Truck()
truck1.load_truck(hash_table)
truck1.print_load()
print()
truck2 = Truck()
truck2.load_truck(hash_table)
truck2.print_load()

# route_simulator.run_simulation(adjacency_list_graph)

# User interface.
while True:
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
        time_set = input('Enter start time (HH:MM): ')
        print()
    elif user_int == 4:
        print('Goodbye!')
        break
    else:
        print('Invalid command!')
        print()
