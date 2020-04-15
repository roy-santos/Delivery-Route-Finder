# Truck class
from models.package import PackageStatus


class Truck:

    def __init__(self):
        self.AVG_SPEED_MPH = 18
        self.cargo_capacity = 16
        self.truck_load = []
        self.distance_traveled = 0
        self.location = "Western Governors University (HUB)"

    def __iter__(self):
        return iter(self.truck_load)

    # Trucks are loaded by first sorting the hashtable by address then loading the first 16 available packages into
    # the truck. Runtime complexity is O(NlogN) due to python's sort function.
    def load_truck(self, hashtable):

        hashtable.array.sort(key=lambda x: x.package_address)

        for package in hashtable:
            if self.cargo_capacity > 0 and package.delivery_status == PackageStatus.STATUS_1.value:
                self.truck_load.append(package)
                package.delivery_status = PackageStatus.STATUS_2.value
                self.cargo_capacity -= 1

    # Delivery route that follows the nearest neighbor algorithm for the shortest path. Runtime complexity O(N^2)
    def run_route(self, graph):
        next_location = None
        # Loop until truck load is empty
        while sum(package.delivery_status == PackageStatus.STATUS_2.value for package in self.truck_load) > 0:
        # while len(self.truck_load) > 0:
            # Find closest location to current location
            min_distance = 100
            # Loops through locations to find closest one to current location
            for location in graph.vertices[self.location].neighbors:
                if location[1] < min_distance:
                    # Loops through packages to find one that matches the closest location
                    for package in self.truck_load:
                        x = package.package_address
                        y = graph.vertices[location[0]].address
                        if package.package_address == graph.vertices[location[0]].address and package.delivery_status != PackageStatus.STATUS_3.value:
                            print('Delivered at:', package.package_address)
                            min_distance = location[1]
                            next_location = location
                            package.delivery_status = PackageStatus.STATUS_3.value
                            if self.location != next_location[0]:
                                self.location = next_location[0]
                                self.distance_traveled += next_location[1]
        self.truck_load = []
        self.cargo_capacity += 16
        self.location = graph.vertices['Western Governors University (HUB)'].name
        distance_back_to_hub = [item for item in graph.vertices[next_location[0]].neighbors if item[0] == self.location][0][1]
        self.distance_traveled += distance_back_to_hub

    def print_load(self):
        print("Truck Location:", self.location)
        print("Package list:")

        for package in self.truck_load:
            print(package)

        print()
