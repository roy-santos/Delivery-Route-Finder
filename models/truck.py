# Truck class
import datetime

from models.package import PackageStatus


class Truck:
    # Init truck objects with these attributes.
    def __init__(self, truck_name):
        self.name = truck_name
        self.AVG_SPEED_MPH = 18
        self.CARGO_CAPACITY = 16
        self.truck_load = []
        self.distance_traveled = 0
        self.location = "Western Governors University (HUB)"
        self.time = datetime.datetime.combine(datetime.date.today(), datetime.time(8))

    # Function that defines how to iterate over truck objects. Iterates over the truck_load
    def __iter__(self):
        return iter(self.truck_load)

    # Trucks are loaded by first sorting the hashtable by address then loading the first 16 available packages into
    # the truck. Packages with certain delivery constraints are prioritized to load first to ensure that they are in
    # the same truck. Runtime complexity is O(NlogN) due to python's sort function.
    def load_truck(self, hashtable):
        # For loop that finds packages that must be delivered in the same truck.
        for package in hashtable:
            if self.CARGO_CAPACITY > 0 and package.delivery_status == PackageStatus.STATUS_1.value and package.package_id in [
                13, 14, 15, 19, 16, 20]:
                self.truck_load.append(package)
                package.delivery_status = PackageStatus.STATUS_2.value
                self.CARGO_CAPACITY -= 1
        # Sort array by address so that packages that go to the same location are added to the same truck.
        hashtable.array.sort(key=lambda x: x.package_address)
        # For loop that adds the packages until the capacity of the truck is 0.
        for package in hashtable:
            if self.CARGO_CAPACITY > 0 and package.delivery_status == PackageStatus.STATUS_1.value and (
                    'Delayed' in package.special_notes or 'Wrong' in package.special_notes):
                if self.time > datetime.datetime.combine(datetime.date.today(), datetime.time(9, 5)):
                    self.truck_load.append(package)
                    package.delivery_status = PackageStatus.STATUS_2.value
                    self.CARGO_CAPACITY -= 1
            elif self.CARGO_CAPACITY > 0 and package.delivery_status == PackageStatus.STATUS_1.value and package.special_notes == "":
                self.truck_load.append(package)
                package.delivery_status = PackageStatus.STATUS_2.value
                self.CARGO_CAPACITY -= 1
            elif self.CARGO_CAPACITY > 0 and package.delivery_status == PackageStatus.STATUS_1.value and self.name in package.special_notes:
                self.truck_load.append(package)
                package.delivery_status = PackageStatus.STATUS_2.value
                self.CARGO_CAPACITY -= 1

    # Delivery route algorithm that follows the nearest neighbor algorithm for shortest path. Runtime complexity O(N^2).
    def run_route(self, graph, time):
        next_location = None
        # Loop until all packages in truck load have 'Delivered' status. Since the loop has a max number of
        # iterations (16), the runtime complexity is O(1).
        while sum(package.delivery_status == PackageStatus.STATUS_2.value for package in
                  self.truck_load) > 0 and self.time < time:
            # Find closest location to current location
            min_distance = 100
            # Prioritize packages ID 25 which has was delayed and has a deadline of 10:30AM.
            for package in self.truck_load:
                if package.package_id == 25:
                    for location in graph.vertices[self.location].neighbors:
                        if package.package_address == graph.vertices[location[0]].address and package.delivery_status ==\
                                PackageStatus.STATUS_2.value:
                            min_distance = location[1]
                            next_location = location
                            # Conditional statement that handles situations where multiple packages for the same
                            # location.
                            if self.location != next_location[0]:
                                self.location = next_location[0]
                                self.distance_traveled += next_location[1]
                                self.time = self.time + datetime.timedelta(
                                    minutes=(next_location[1] / self.AVG_SPEED_MPH) * 60)
                            package.delivery_status = PackageStatus.STATUS_3.value + ' by ' + self.name + ' at ' + str(
                                self.time)
            # Prioritize packages ID 6 which has was delayed and has a deadline of 10:30AM.
            for package in self.truck_load:
                if package.package_id == 6:
                    for location in graph.vertices[self.location].neighbors:
                        if package.package_address == graph.vertices[location[0]].address and package.delivery_status ==\
                                PackageStatus.STATUS_2.value:
                            min_distance = location[1]
                            next_location = location
                            # Conditional statement that handles situations where multiple packages for the same
                            # location.
                            if self.location != next_location[0]:
                                self.location = next_location[0]
                                self.distance_traveled += next_location[1]
                                self.time = self.time + datetime.timedelta(
                                    minutes=(next_location[1] / self.AVG_SPEED_MPH) * 60)
                            package.delivery_status = PackageStatus.STATUS_3.value + ' by ' + self.name + ' at ' + str(
                                self.time)
            # Handles the rest of the packages. Loops through locations to find closest one to current location.
            # Runtime complexity of O(N)
            for location in graph.vertices[self.location].neighbors:
                if location[1] < min_distance:
                    # Loops through packages to find one that matches the closest location. Runtime complexity of O(N)
                    for package in self.truck_load:
                        # Conditional statement that corrects the address of package ID 9 at 10:20AM
                        if self.time > datetime.datetime.combine(datetime.date.today(), datetime.time(10, 20)):
                            if package.package_id == 9:
                                package.package_address = '410 S State St'
                                package.package_zip = '84111'
                        # nearest neighbor to the current location.
                        if package.package_address == graph.vertices[
                             location[0]].address and package.delivery_status == PackageStatus.STATUS_2.value:
                            min_distance = location[1]
                            next_location = location
                            # Conditional statement that handles situations where multiple packages for the same
                            # location.
                            if self.location != next_location[0]:
                                self.location = next_location[0]
                                self.distance_traveled += next_location[1]
                                self.time = self.time + datetime.timedelta(
                                    minutes=(next_location[1] / self.AVG_SPEED_MPH) * 60)
                            package.delivery_status = PackageStatus.STATUS_3.value + ' by ' + self.name + ' at ' + str(
                                self.time)
        # Conditional statement that determines whether all of the packages are delivered. Sets the capacity back to
        # 16 and empties the truck load list.
        if sum(PackageStatus.STATUS_3.value in package.delivery_status for package in self.truck_load) == len(
                self.truck_load):
            self.truck_load = []
            self.CARGO_CAPACITY += 16
            self.location = graph.vertices['Western Governors University (HUB)'].name
            distance_back_to_hub = \
                [item for item in graph.vertices[next_location[0]].neighbors if item[0] == self.location][0][1]
            self.distance_traveled += distance_back_to_hub
        return self.time

    # Function for printing out packages currently in the truck. Runtime complexity of O(N).
    def print_load(self):
        print(self.name)
        print("Truck Location:", self.location)
        print("Package list:")

        for package in self.truck_load:
            print(package)

        print()
