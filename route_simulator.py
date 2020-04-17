from datetime import datetime, date, time, timedelta

from models.truck import Truck
from utilities.data_loader import hash_loader, graph_loader


# Function that sets up and runs the package delivery simulation.
def run_simulation(set_time):

    # Initialize hash table and graph with data from CSV files
    hashtable = hash_loader('utilities/WGUPS_Package_File.csv', 40)
    graph = graph_loader('utilities/WGUPS_Distance_Table.csv')

    # Constant values used in the simulation. Start time is 8:00AM and average truck speed of 18mph.
    start_time = datetime.combine(date.today(), time(8))
    AVG_SPEED_MPH = 18

    # Load 2 trucks with packages.
    truck1 = Truck('truck 1')
    truck1.load_truck(hashtable)
    truck2 = Truck('truck 2')
    truck2.load_truck(hashtable)

    # Truck1 and Truck2 leave the hub at 8:00AM to start deliveries.
    truck1.run_route(graph, set_time)
    truck2.run_route(graph, set_time)

    # Checks to see if truck1 finished it's route by the specified set_time. If not, no need to run rest of the code.
    # Else, truck1 gets loaded with the remaining packages and performs the rest of the deliveries.
    if len(truck1.truck_load) != 0:
        # The truck that traveled the most will determine the end_time for the simulation
        if truck1.distance_traveled > truck2.distance_traveled:
            end_time = start_time + timedelta(
                minutes=(truck1.distance_traveled / AVG_SPEED_MPH) * 60)
            return end_time, hashtable
        else:
            end_time = start_time + timedelta(
                minutes=(truck2.distance_traveled / AVG_SPEED_MPH) * 60)
            return end_time, hashtable
    else:
        truck1.load_truck(hashtable)
        truck1.run_route(graph, set_time)

    # Calculate total distance travelled by both trucks.
    total_distance = int(truck1.distance_traveled + truck2.distance_traveled)
    print('Total distance travelled: ' + str(total_distance))

    # Conditional statement that only runs if all packages were delivered. Prints the time of the last delivery.
    if len(truck1.truck_load) == 0 and truck1.location == "Western Governors University (HUB)":
        print("Deliveries completed at " + str(truck1.time))

    # Truck1 will go out for deliveries twice. Distance it traveled will be used to determine simulation end time.
    end_time = start_time + timedelta(
        minutes=(truck1.distance_traveled / AVG_SPEED_MPH) * 60)

    # Conditional that returns the greater value out of time set by user and time at the end of the simulation.
    if end_time > set_time:
        return end_time, hashtable
    else:
        return set_time, hashtable

