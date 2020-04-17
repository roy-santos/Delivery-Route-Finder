# Package class to hold information about each package
from enum import Enum


# Enumeration class for package statuses
class PackageStatus(Enum):
    STATUS_1 = "ACCEPTED AT WGUPS FACILITY"
    STATUS_2 = "IN TRANSIT"
    STATUS_3 = "DELIVERED"


class Package:
    # Package information is read from the CSV and used as input for creating packages.
    def __init__(self, package_id=-1, package_address='', package_city='', package_state='', package_zip='',
                 delivery_deadline='', mass_in_kilos='', special_notes='', delivery_status=PackageStatus.STATUS_1.value,
                 delivery_time=''):
        self.package_id = int(package_id)
        self.package_address = package_address
        self.package_city = package_city
        self.package_state = package_state
        self.package_zip = package_zip
        self.delivery_deadline = delivery_deadline
        self.mass_in_kilos = mass_in_kilos
        self.special_notes = special_notes
        self.delivery_status = delivery_status
        self.delivery_time = delivery_time

    # Function that defines how the package class is hashed.
    def __hash__(self):
        return self.package_id

    # Function that defines how packages are determined to be equal.
    def __eq__(self, other):
        return self.package_id == other

    # Function that overrides an object's default print implementation.
    def __str__(self):
        return "Package ID: %s; Address: %s, %s, %s, %s; Deadline: %s; Mass: %s; Special Notes: %s; Delivery Status: " \
               "%s, %s" % (
                   self.package_id, self.package_address, self.package_city, self.package_state, self.package_zip,
                   self.delivery_deadline, self.mass_in_kilos, self.special_notes, self.delivery_status,
                   self.delivery_time)
