# Roy Santos, StudentID: 001186453
from datetime import datetime, date, time

import route_simulator
from utilities.data_loader import hash_loader, graph_loader

# Initialize hash table and graph with data from CSV files
hash_table = hash_loader('WGUPS_Package_File.csv', 40)
adjacency_list_graph = graph_loader('WGUPS_Distance_Table.csv')

# Initialize start time for the day
set_time = datetime.combine(date.today(), time(8))


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


while True:
    print()
    print('Current simulation time:', set_time)
    user_int = user_int_prompt()
    print()
    if user_int == 1:
        package_id = int(input('Enter package ID: '))
        print(route_simulator.run_simulation(set_time)[1].search(package_id))
        print()
    elif user_int == 2:
        route_simulator.run_simulation(set_time)[1].print_table()
        print()
    elif user_int == 3:
        time_prompt = input('Enter start time (HH:MM): ')
        hours, minutes = map(int, time_prompt.split(':'))
        user_time = datetime.combine(date.today(), time(hours, minutes))
        set_time = route_simulator.run_simulation(user_time)[0]
    elif user_int == 4:
        print('Goodbye!')
        break
    else:
        print('Invalid command!')
        print()
