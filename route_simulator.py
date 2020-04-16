from datetime import datetime, date, time, timedelta

from models.truck import Truck
from utilities.data_loader import hash_loader, graph_loader


def run_simulation(set_time):

    # Initialize hash table and graph with data from CSV files
    hashtable = hash_loader('WGUPS_Package_File.csv', 40)
    graph = graph_loader('WGUPS_Distance_Table.csv')

    start_time = datetime.combine(date.today(), time(8))
    AVG_SPEED_MPH = 18

    # Load trucks with packages
    truck1 = Truck('truck 1')
    truck1.load_truck(hashtable)
    truck2 = Truck('truck 2')
    truck2.load_truck(hashtable)

    # ALGO TESTING - DELETE LATER
    simulation_time = truck1.run_route(graph, set_time)
    truck2.run_route(graph, set_time)

    truck1.load_truck(hashtable)
    truck1.run_route(graph, set_time)

    total_distance = int(truck1.distance_traveled + truck2.distance_traveled)

    print()
    print(truck1.distance_traveled)
    print(truck2.distance_traveled)
    print('Total distance travelled: ' + str(total_distance))

    end_time = start_time + timedelta(
        minutes=((truck1.distance_traveled + truck2.distance_traveled) / AVG_SPEED_MPH) * 60)

    if end_time > set_time:
        return end_time, hashtable
    else:
        return set_time, hashtable

