# Michaela Ruiz #001323526
import truck


# package class and attributes

class Package:

    def __init__(self, pid, address, city, state, zip_code, deadline, weight, note):
        self.pid = pid
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.deadline = deadline
        self.weight = weight
        self.note = note
        self.status = 'N/A'
        self.delivery_time = 'N/A'
        self.departure_time = 'N/A'


