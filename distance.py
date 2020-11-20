# Michaela Ruiz #001323526
import csv

first_truck_delivery = []
first_truck_delivery_packages = []
second_truck_delivery = []
second_truck_delivery_packages = []
third_truck_delivery = []
third_truck_delivery_packages = []


class Distances:

    # constructor
    def __init__(self):
        self.distanceData = self.import_distance_to_list()
        # creates distanceData object which is the distance table csv read
        # creates dictionary of address keys and value is column or row value in the distance table
        self.distance_dict = {'HUB': 0, '1060 Dalton Ave S': 1, '1330 2100 S': 2, '1488 4800 S': 3,
                              '177 W Price Ave': 4,
                              '195 W Oakland Ave': 5, '2010 W 500 S': 6, '2300 Parkway Blvd': 7, '233 Canyon Rd': 8,
                              '2530 S 500 E': 9, '2600 Taylorsville Blvd': 10, '2835 Main St': 11, '300 State St': 12,
                              '3060 Lester St': 13, '3148 S 1100 W': 14, '3365 S 900 W': 15,
                              '3575 W Valley Central Station bus Loop': 16,
                              '3595 Main St': 17, '380 W 2880 S': 18, '410 S State St': 19, '4300 S 1300 E': 20,
                              '4580 S 2300 E': 21,
                              '5025 State St': 22, '5100 South 2700 West': 23, '5383 South 900 East #104': 24,
                              '600 E 900 South': 25,
                              '6351 South 900 East': 26
                              }
        self.max_addressId = 26  # there are only 26 rows

    # space time complexity O(N)
    # imports and reads data distance file
    def import_distance_to_list(self):
        distances_list = []
        with open('DistanceData.csv', 'r') as csv_file:
            readCSV = csv.reader(csv_file, delimiter=',')  # reads the csv file
            for row in readCSV:
                row1 = [float(i) for i in row if i]  # converts the distances in the table floats instead of strings
                distances_list.append(row1)  # creates distance lists of distances in the csv file
                # print(row1)
        return distances_list  # return distance list

    # space time complexity O(1)
    # finds the distance between two addresses by address Name
    def lookupDistancesByAddresses(self, address1, address2):
        addressId1 = self.distance_dict[address1]
        addressId2 = self.distance_dict[address2]
        rowId = max(addressId1, addressId2)
        columnId = min(addressId1, addressId2)
        distance = self.distanceData[rowId][columnId]
        return distance

    # space time complexity O(1)
    # finds the distance between two addresses by address ID(or row/column number)
    def lookupDistancesByAddressIds(self, addressId1, addressId2):
        rowId = max(addressId1, addressId2)
        columnId = min(addressId1, addressId2)
        distance = self.distanceData[rowId][columnId]
        return distance

    # space time complexity O(N)
    # finds closest address to address1 from the same truck
    def find_closest_address(self, address1, truckPackages):
        closest_address_distance = 300000
        closest_address = None
        for address2 in self.distance_dict.keys():
            if address1 == address2:
                continue
            if address2 in truckPackages:
                if self.lookupDistancesByAddresses(address1, address2) < closest_address_distance:
                    closest_address_distance = self.lookupDistancesByAddresses(address1, address2)
                    closest_address = address2
        # return closest_address, closest_address_distances
        return closest_address, closest_address_distance

