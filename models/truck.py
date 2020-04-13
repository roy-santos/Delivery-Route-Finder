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

    def print_load(self):
        print("Truck Location:", self.location)
        print("Package list:")

        for package in self.truck_load:
            print(package)

        print()
