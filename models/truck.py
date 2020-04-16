# Truck class
import datetime

from models.package import PackageStatus


class Truck:

    def __init__(self, truck_name):
        self.name = truck_name
        self.AVG_SPEED_MPH = 18
        self.CARGO_CAPACITY = 16
        self.truck_load = []
        self.distance_traveled = 0
        self.location = "Western Governors University (HUB)"
        self.time = datetime.datetime.combine(datetime.date.today(), datetime.time(8))

    def __iter__(self):
        return iter(self.truck_load)

    # Trucks are loaded by first sorting the hashtable by address then loading the first 16 available packages into
    # the truck. Runtime complexity is O(NlogN) due to python's sort function.
    def load_truck(self, hashtable):

        for package in hashtable:
            if self.CARGO_CAPACITY > 0 and package.delivery_status == PackageStatus.STATUS_1.value and package.package_id in [
                13, 14, 15, 19, 16, 20]:
                self.truck_load.append(package)
                package.delivery_status = PackageStatus.STATUS_2.value
                self.CARGO_CAPACITY -= 1

        hashtable.array.sort(key=lambda x: x.package_address)

        for package in hashtable:
            if self.CARGO_CAPACITY > 0 and package.delivery_status == PackageStatus.STATUS_1.value and package.special_notes == "":
                self.truck_load.append(package)
                package.delivery_status = PackageStatus.STATUS_2.value
                self.CARGO_CAPACITY -= 1
            elif self.CARGO_CAPACITY > 0 and package.delivery_status == PackageStatus.STATUS_1.value and self.name in package.special_notes:
                self.truck_load.append(package)
                package.delivery_status = PackageStatus.STATUS_2.value
                self.CARGO_CAPACITY -= 1
            elif self.CARGO_CAPACITY > 0 and package.delivery_status == PackageStatus.STATUS_1.value and (
                    'Delayed' in package.special_notes or 'Wrong' in package.special_notes):
                if self.time > datetime.datetime.combine(datetime.date.today(), datetime.time(9, 5)):
                    self.truck_load.append(package)
                    package.delivery_status = PackageStatus.STATUS_2.value
                    self.CARGO_CAPACITY -= 1

    # Delivery route that follows the nearest neighbor algorithm for the shortest path. Runtime complexity O(N^2)
    def run_route(self, graph, time):
        next_location = None
        # Loop until all packages in truck load have 'Delivered' status
        while sum(package.delivery_status == PackageStatus.STATUS_2.value for package in
                  self.truck_load) > 0 and self.time < time:
            # Find closest location to current location
            min_distance = 100
            # Loops through locations to find closest one to current location
            for location in graph.vertices[self.location].neighbors:
                if location[1] < min_distance:
                    # Loops through packages to find one that matches the closest location
                    for package in self.truck_load:
                        if package.package_address == graph.vertices[
                                location[0]].address and package.delivery_status == PackageStatus.STATUS_2.value:
                            min_distance = location[1]
                            next_location = location
                            if self.location != next_location[0]:
                                self.location = next_location[0]
                                self.distance_traveled += next_location[1]
                                self.time = self.time + datetime.timedelta(
                                    minutes=(next_location[1] / self.AVG_SPEED_MPH) * 60)
                            package.delivery_status = PackageStatus.STATUS_3.value + ' by ' + self.name + ' at ' + str(
                                self.time)
        if sum(PackageStatus.STATUS_3.value in package.delivery_status for package in self.truck_load) == len(
                self.truck_load):
            self.truck_load = []
            self.CARGO_CAPACITY += 16
            self.location = graph.vertices['Western Governors University (HUB)'].name
            distance_back_to_hub = \
                [item for item in graph.vertices[next_location[0]].neighbors if item[0] == self.location][0][1]
            self.distance_traveled += distance_back_to_hub
        return self.time

    def print_load(self):
        print(self.name)
        print("Truck Location:", self.location)
        print("Package list:")

        for package in self.truck_load:
            print(package)

        print()
