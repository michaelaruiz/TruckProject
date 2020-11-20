# Michaela Ruiz #001323526
from datetime import datetime
import datetime
from distance import Distances

distances = Distances()  # creates distance object from Distances class
first_truck_delivery = []  # creates list of addresses in order in the optimized first truck
first_truck_delivery_packages = []  # creates list of packages in order traveled in optimized first truck
second_truck_delivery = []  # creates list of addresses in order in the optimized second truck
second_truck_delivery_packages = []  # creates list of packages in order traveled in optimized second truck
third_truck_delivery = []  # creates list of addresses in order in the optimized third truck
third_truck_delivery_packages = []  # creates list of packages in order traveled in optimized third truck

first_truck_dep = ['8:00:00']  # time first truck leaves the hub
second_truck_dep = ['9:15:00']  # time second truck leaves the hub
third_truck_dep = ['10:45:00']  # time third truck leaves the hub



class Trucks:

    # space time complexity O(N^2)
    # finds the shortest distance from the the current address to another in the same truck
    # returns the list in order of addresses traveled
    def shortest_distance_calculation_truck1_addresses(self, truck_distances, truck_packages, current_location):
        smallest_value = 60.0
        newest_address = 'address'
        for i in truck_distances:
            if distances.lookupDistancesByAddresses(current_location, i) <= smallest_value:
                smallest_value = distances.lookupDistancesByAddresses(current_location, i)
                newest_address = i
        for i in truck_distances:
            if i in truck_distances:
                if distances.lookupDistancesByAddresses(current_location, i) == smallest_value:
                    first_truck_delivery.append(i)
                    for item in truck_packages:
                        if i == item.address:
                            first_truck_delivery_packages.append(item)
                    ap = truck_distances.index(i)
                    truck_distances.pop(ap)
                    current_location = newest_address
                    self.shortest_distance_calculation_truck1_addresses(truck_distances, truck_packages,
                                                                        current_location)

        return first_truck_delivery

    # space time complexity O(N^2)
    # returns list in order of packages traveled in truck 1 using the function that returns addresses in order
    # finds the shortest distance from the the current address to another in the same truck
    def shortest_distance_calculation_truck1_packages(self, truck_distances, truck_packages, current_location):
        smallest_value = 60.0
        newest_address = 'address'
        for i in truck_distances:
            if distances.lookupDistancesByAddresses(current_location, i) <= smallest_value:
                smallest_value = distances.lookupDistancesByAddresses(current_location, i)
                newest_address = i
        for i in truck_distances:
            if i in truck_distances:
                if distances.lookupDistancesByAddresses(current_location, i) == smallest_value:
                    first_truck_delivery.append(i)
                    for item in truck_packages:
                        if i == item.address:
                            first_truck_delivery_packages.append(item)
                    ap = truck_distances.index(i)
                    truck_distances.pop(ap)
                    current_location = newest_address
                    self.shortest_distance_calculation_truck1_packages(truck_distances, truck_packages,
                                                                       current_location)
        return first_truck_delivery_packages

    # space time complexity O(N^2)
    # finds the shortest distance from the the current address to another in the same package
    def shortest_distance_calculation_truck2_addresses(self, truck_distances, packages, current_location):
        smallest_value = 60.0
        newest_address = 'address'
        for i in truck_distances:
            if distances.lookupDistancesByAddresses(current_location, i) <= smallest_value:
                smallest_value = distances.lookupDistancesByAddresses(current_location, i)
                newest_address = i
        for i in truck_distances:
            if distances.lookupDistancesByAddresses(current_location, i) == smallest_value:
                second_truck_delivery.append(i)
                for item in packages:
                    if i == item.address:
                        second_truck_delivery_packages.append(item)
                ap = truck_distances.index(i)
                truck_distances.pop(ap)
                current_location = newest_address
                self.shortest_distance_calculation_truck2_addresses(truck_distances, packages, current_location)
        return second_truck_delivery

    # space time complexity O(N^2)
    # returns list in order of packages traveled in truck 2 using the function that returns addresses in order
    def shortest_distance_calculation_truck2_packages(self, truck_distances, packages, current_location):
        smallest_value = 60.0
        newest_address = 'address'
        for i in truck_distances:
            if distances.lookupDistancesByAddresses(current_location, i) <= smallest_value:
                smallest_value = distances.lookupDistancesByAddresses(current_location, i)
                newest_address = i
        for i in truck_distances:
            if distances.lookupDistancesByAddresses(current_location, i) == smallest_value:
                second_truck_delivery.append(i)
                for item in packages:
                    if i == item.address:
                        second_truck_delivery_packages.append(item)
                ap = truck_distances.index(i)
                truck_distances.pop(ap)
                current_location = newest_address
                self.shortest_distance_calculation_truck2_packages(truck_distances, packages, current_location)
        return second_truck_delivery_packages

    # space time complexity O(N^2)
    # finds the shortest distance from the the current address to another in the same package
    def shortest_distance_calculation_truck3_addresses(self, truck_distances, packages, current_location):
        smallest_value = 60.0
        newest_address = 'address'
        for i in truck_distances:
            if distances.lookupDistancesByAddresses(current_location, i) <= smallest_value:
                smallest_value = distances.lookupDistancesByAddresses(current_location, i)
                newest_address = i
        for i in truck_distances:
            if distances.lookupDistancesByAddresses(current_location, i) == smallest_value:
                third_truck_delivery.append(i)
                for item in packages:
                    if i == item.address:
                        third_truck_delivery_packages.append(item)
                ap = truck_distances.index(i)
                truck_distances.pop(ap)
                current_location = newest_address
                self.shortest_distance_calculation_truck3_addresses(truck_distances, packages, current_location)
        return third_truck_delivery

    # space time complexity O(N^2)
    # returns list in order of packages traveled in truck 3 using the function that returns addresses in order

    def shortest_distance_calculation_truck3_packages(self, truck_distances, packages, current_location):
        smallest_value = 60.0
        newest_address = 'address'
        for i in truck_distances:
            if distances.lookupDistancesByAddresses(current_location, i) <= smallest_value:
                smallest_value = distances.lookupDistancesByAddresses(current_location, i)
                newest_address = i
        for i in truck_distances:
            if distances.lookupDistancesByAddresses(current_location, i) == smallest_value:
                third_truck_delivery.append(i)
                for item in packages:
                    if i == item.address:
                        third_truck_delivery_packages.append(item)
                ap = truck_distances.index(i)
                truck_distances.pop(ap)
                current_location = newest_address
                self.shortest_distance_calculation_truck3_packages(truck_distances, packages, current_location)
        return third_truck_delivery_packages

    # space time complexity O(N)
    # calculates total distance traveled in a truck trip
    def calculate_total_distance_traveled_per_truck(self, truck_delivery, current_location):
        distance_sum = 0.0
        for i in truck_delivery:
            distance1 = distances.lookupDistancesByAddresses(current_location, i)
            current_location = i
            distance_sum += distance1
        return distance_sum

    # space time complexity O(N)
    # finds the amount each package traveled before getting to its destination
    def find_package_distance_from_start(self, truck_delivery, packages_in_truck, current_location, package_number):
        distance_sum = 0.0
        if package_number not in packages_in_truck:
            print('error, package not in truck; truck leaves at')
        else:
            index = truck_delivery.index(package_number.address)
            for i in truck_delivery[0:index + 1]:
                distance1 = distances.lookupDistancesByAddresses(current_location, i)
                current_location = i
                distance_sum += distance1
        return distance_sum

    # times
    # space time complexity O(N)
    # calculates the time that the truck gets to the distance inputted
    def time_of_first_truck_at_distance(self, distance):
        time_object = datetime.datetime.strptime(first_truck_dep[0], '%H:%M:%S')
        time = distance / 18
        hour_min = '{0:02.0f}:{1:02.0f}'.format(*divmod(time * 60, 60))
        hour_min_sec = hour_min + ':00'
        first_truck_dep.append(hour_min_sec)
        total = datetime.timedelta()
        for i in first_truck_dep:
            (h, m, s) = i.split(':')
            d = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
            total = d
        return total + time_object

    # space time complexity O(N)

    def update_package_departure_from_hub_time_first_truck(self, packages_in_truck):
        time_object = datetime.datetime.strptime(first_truck_dep[0], '%H:%M:%S')
        for p in packages_in_truck:
            departure_time = time_object
            p.departure_time = departure_time
        return departure_time

    # space time complexity O(N)
    def update_package_delivery_time_first_truck(self, truck_delivery, packages_in_truck, current_location):
        for p in packages_in_truck:
            delivery_time = self.time_of_first_truck_at_distance(
                self.find_package_distance_from_start(truck_delivery, packages_in_truck, current_location, p))
            p.delivery_time = delivery_time
        return delivery_time

    # space time complexity O(N)
    # calculates the time that the truck gets to the distance inputted
    def time_of_second_truck_at_distance(self, distance):
        time_object = datetime.datetime.strptime(second_truck_dep[0], '%H:%M:%S')
        time = distance / 18
        hour_min = '{0:02.0f}:{1:02.0f}'.format(*divmod(time * 60, 60))
        hour_min_sec = hour_min + ':00'
        second_truck_dep.append(hour_min_sec)
        total = datetime.timedelta()
        for i in second_truck_dep:
            (h, m, s) = i.split(':')
            d = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
            total = d
        return total + time_object

    # space time complexity O(N)
    def update_package_delivery_time_second_truck(self, truck_delivery, packages_in_truck, current_location):
        for p in packages_in_truck:
            delivery_time = self.time_of_second_truck_at_distance(
                self.find_package_distance_from_start(truck_delivery, packages_in_truck, current_location, p))
            p.delivery_time = delivery_time
        return delivery_time

    # space time complexity O(N)
    def update_package_departure_from_hub_time_second_truck(self, packages_in_truck):
        time_object = datetime.datetime.strptime(second_truck_dep[0], '%H:%M:%S')
        for p in packages_in_truck:
            departure_time = time_object
            p.departure_time = departure_time
        return departure_time

    # space time complexity O(N)
    # calculates the time that the truck gets to the distance inputted
    def time_of_third_truck_at_distance(self, distance):
        time_object = datetime.datetime.strptime(third_truck_dep[0], '%H:%M:%S')
        time = distance / 18
        hour_min = '{0:02.0f}:{1:02.0f}'.format(*divmod(time * 60, 60))
        hour_min_sec = hour_min + ':00'
        third_truck_dep.append(hour_min_sec)
        total = datetime.timedelta()
        for i in third_truck_dep:
            (h, m, s) = i.split(':')
            d = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
            total = d
        return total + time_object

    # space time complexity O(N)
    def update_package_delivery_time_third_truck(self, truck_delivery, packages_in_truck, current_location):
        for p in packages_in_truck:
            delivery_time = self.time_of_third_truck_at_distance(
                self.find_package_distance_from_start(truck_delivery, packages_in_truck, current_location, p))
            p.delivery_time = delivery_time
        return delivery_time

    # space time complexity O(N)
    def update_package_departure_from_hub_time_third_truck(self, packages_in_truck):
        time_object = datetime.datetime.strptime(third_truck_dep[0], '%H:%M:%S')
        for p in packages_in_truck:
            departure_time = time_object
            p.departure_time = departure_time
        return departure_time
