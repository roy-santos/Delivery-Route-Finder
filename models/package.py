# Package class


class Package:

    def __init__(self, package_id=-1, package_address='', package_city='', package_state='', package_zip='',
                 delivery_deadline='', mass_in_kilos='', special_notes='', delivery_status='', delivery_time=''):
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

    def __hash__(self):
        return hash(self.package_id)

    def __eq__(self, other):
        return self.package_id == other

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s" % (self.package_id, self.package_address, self.package_city, self.package_state, self.package_zip, self.mass_in_kilos, self.special_notes, self.delivery_status, self. delivery_time)


