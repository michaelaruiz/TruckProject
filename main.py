# Michaela Ruiz #001323526
import csv
import package
from distance import Distances
from hashTable import HashTable
from truck import Trucks
import datetime
from datetime import datetime


# makes the file main


def main_one():
    with open('WGUPSPackageFile1.csv', 'r') as csvfile:
        csv_file = csv.reader(csvfile, delimiter=',')  # reads the CSV package file
        list_of_packages = list(csv_file)
        # print(list_of_packages[0][0])
        packageHashTable = HashTable()  # 15 - creates a hashtable object by calling the HashTable class

        distances = Distances()
        trucks = Trucks()  # creates truck object by calling Trucks class

        # creates lists of each package attribute

        Package_IDs = []
        Addresses = []
        Cities = []
        States = []
        Zips = []
        Delivery_Deadlines = []
        Weight = []
        Notes = []
        Status = []
        Departure_time = []

        # reads the package csv and creates attributes for each package
        for row in list_of_packages:  # space time complexity is O(N)
            pid = row[0].strip()
            address = row[1]
            city = row[2]
            state = row[3]
            zipcode = row[4]
            deadline = row[5]
            weight = row[6]
            note = row[7]
            status = row[8]
            departure_time = row[9]

            # appends each value to respective lists
            Package_IDs.append(pid)
            Addresses.append(address)
            Cities.append(city)
            States.append(state)
            Zips.append(zipcode)
            Delivery_Deadlines.append(deadline)
            Weight.append(weight)
            Notes.append(note)
            Status.append(status)
            Departure_time.append(departure_time)

            p = package.Package(pid, address, city, state, zipcode, deadline,
                                weight, note)  # creates the package object using the package class

            packageHashTable.get(pid)  # look up the package by the id
            packageHashTable.insert(pid, p)  # inserts the packages into the hashtable

        # gets the package object using the ids using the hashtable and creates package objects for each
        p1 = packageHashTable.get('1')
        p5 = packageHashTable.get('5')
        p7 = packageHashTable.get('7')
        p8 = packageHashTable.get('8')
        p10 = packageHashTable.get('10')
        p11 = packageHashTable.get('11')
        p12 = packageHashTable.get('12')
        p13 = packageHashTable.get('13')
        p14 = packageHashTable.get('14')
        p15 = packageHashTable.get('15')
        p16 = packageHashTable.get('16')
        p19 = packageHashTable.get('19')
        p20 = packageHashTable.get('20')
        p29 = packageHashTable.get('29')
        p30 = packageHashTable.get('30')
        p34 = packageHashTable.get('34')
        p37 = packageHashTable.get('37')
        p3 = packageHashTable.get('3')
        p6 = packageHashTable.get('6')
        p18 = packageHashTable.get('18')
        p25 = packageHashTable.get('25')
        p26 = packageHashTable.get('26')
        p31 = packageHashTable.get('31')
        p36 = packageHashTable.get('36')
        p38 = packageHashTable.get('38')
        p40 = packageHashTable.get('40')
        p2 = packageHashTable.get('2')
        p4 = packageHashTable.get('4')
        p9 = packageHashTable.get('9')
        p17 = packageHashTable.get('17')
        p21 = packageHashTable.get('21')
        p22 = packageHashTable.get('22')
        p23 = packageHashTable.get('23')
        p24 = packageHashTable.get('24')
        p27 = packageHashTable.get('27')
        p28 = packageHashTable.get('28')
        p32 = packageHashTable.get('32')
        p33 = packageHashTable.get('33')
        p35 = packageHashTable.get('35')
        p39 = packageHashTable.get('39')
        # p37.status = 'At Hub'
        # print(p37)
        firstTruckTripPackages = [p1, p7, p8, p10, p11, p12, p13, p14, p15, p16, p19, p20, p29, p30, p34, p37]
        # print(p1.pid)
        # puts the packages into the first truck
        # print(packageHashTable.update_status('1', 'At HUB'))

        firstTruckTripPAddresses = []
        for item in firstTruckTripPackages:
            firstTruckTripPackageA = item.address
            firstTruckTripPAddresses.append(firstTruckTripPackageA)
            # creates a list of addresses of each package in the first truck
            # space time complexity of O(N)

        secondTruckTripPackages = [p3, p6, p18, p25, p26, p31, p36, p38, p40]
        # puts the package object into the second truck

        secondTruckTripPAddresses = []
        for item in secondTruckTripPackages:
            secondTruckTripPackageA = item.address
            secondTruckTripPAddresses.append(secondTruckTripPackageA)
            # creates a list of addresses of each package in the second truck
            # space time complexity of O(N)

        thirdTruckTripPackages = [p2, p4, p5, p9, p17, p21, p22, p23, p24, p27, p28, p32, p33, p35, p39]
        # puts the package object into the third truck

        thirdTruckTripPAddresses = []
        for item in thirdTruckTripPackages:
            firstTruckSecondTripPackageA = item.address
            thirdTruckTripPAddresses.append(firstTruckSecondTripPackageA)
            # creates a list of addresses of each package in the second truck
            # space time complexity of O(N)

        first_location = 'HUB'

        # creates list of addresses from the optimized list of addresses from truck 1
        first_truck_delivery = trucks.shortest_distance_calculation_truck1_addresses(
            firstTruckTripPAddresses, firstTruckTripPackages, first_location)

        # creates list of addresses from the optimized list of addresses from truck 2
        second_truck_delivery = trucks.shortest_distance_calculation_truck2_addresses(
            secondTruckTripPAddresses, secondTruckTripPackages, first_location)

        # creates list of addresses from the optimized list of addresses from truck 3
        third_truck_delivery = trucks.shortest_distance_calculation_truck3_addresses(
            thirdTruckTripPAddresses, thirdTruckTripPackages, first_location)

    # lines 166-168 update each package departure time
    trucks.update_package_departure_from_hub_time_first_truck(firstTruckTripPackages)
    trucks.update_package_departure_from_hub_time_second_truck(secondTruckTripPackages)
    trucks.update_package_departure_from_hub_time_third_truck(thirdTruckTripPackages)

    # lines 167-169 update each package delivery time to the time they are delivered
    trucks.update_package_delivery_time_first_truck(first_truck_delivery, firstTruckTripPackages, 'HUB')
    trucks.update_package_delivery_time_second_truck(second_truck_delivery, secondTruckTripPackages, 'HUB')
    trucks.update_package_delivery_time_third_truck(third_truck_delivery, thirdTruckTripPackages, 'HUB')

    # for item in firstTruckTripPackages:
    #     print(item.pid)
    #     print(item.departure_time)
    #     print(item.delivery_time)
    # print('\n')
    #
    #
    # for item2 in secondTruckTripPackages:
    #     print(item2.pid)
    #     print(item2.departure_time)
    #     print(item2.delivery_time)
    # print('\n')
    #
    # for item3 in thirdTruckTripPackages:
    #     print(item3.pid)
    #     print(item3.departure_time)
    #     print(item3.delivery_time)
    # print('\n')

    print('Hello, welcome to the portal of the Western Governors University Parcel Service!')
    print('Below is the total miles traveled in by each truck delivery:')
    first_truck_miles = trucks.calculate_total_distance_traveled_per_truck(first_truck_delivery, 'HUB')
    print('First truck miles: ', first_truck_miles)
    second_truck_miles = trucks.calculate_total_distance_traveled_per_truck(second_truck_delivery, 'HUB')
    print('Second truck miles: ', second_truck_miles)
    third_truck_miles = trucks.calculate_total_distance_traveled_per_truck(third_truck_delivery, 'HUB')
    print('Third truck miles: ', third_truck_miles)
    print('Total miles: ', first_truck_miles + second_truck_miles + third_truck_miles)


    first_input = input("Please enter 'get' or 'status' to get started. 'Get' will return package information and "
                        "'status' will return status information for a certain time: ")
    # space time complexity O(N^2)
    while first_input is not 'exit':
        if first_input == 'get':
            p = input("Please enter package ID: ")
            for package_id_input in firstTruckTripPackages:  # gets package information from each package in truck 1
                if package_id_input.pid == p:
                    departure_time = package_id_input.departure_time
                    delivery_time = package_id_input.delivery_time
                    user_input_time = input("please enter a time in the 'HH:MM:SS' format: ")
                    convert_user_input_time = datetime.strptime(user_input_time, '%H:%M:%S')
                    if departure_time >= convert_user_input_time:  # checks if package is at hub and then sets
                        # value in hashtable
                        package_id_input.status = 'At HUB'
                        print('Package ID: ', package_id_input.pid, 'Address: ', package_id_input.address, 'City: ',
                              package_id_input.city, 'State: ', package_id_input.state, 'Zipcode: ',
                              package_id_input.zip_code,
                              'Deadline: ', package_id_input.deadline, 'Weight: ', package_id_input.weight, 'Notes: ',
                              package_id_input.note, 'Status: ', package_id_input.status, 'Departure Time: ',
                              package_id_input.departure_time, 'Delivery Time: ', package_id_input.delivery_time)
                    elif departure_time <= convert_user_input_time:  # checks if package is in transit
                        # then sets in hashtable
                        if convert_user_input_time < delivery_time:
                            package_id_input.status = 'In transit'
                            print('Package ID: ', package_id_input.pid, 'Address: ', package_id_input.address, 'City: ',
                                  package_id_input.city, 'State: ', package_id_input.state, 'Zipcode: ',
                                  package_id_input.zip_code,
                                  'Deadline: ', package_id_input.deadline, 'Weight: ', package_id_input.weight,
                                  'Notes: ',
                                  package_id_input.note, 'Status: ', package_id_input.status, 'Departure Time: ',
                                  package_id_input.departure_time, 'Delivery Time: ', package_id_input.delivery_time)
                        else:  # checks if package is delivered and then sets value in hashtable
                            package_id_input.status = 'Delivered'
                            print('Package ID: ', package_id_input.pid, 'Address: ', package_id_input.address, 'City: ',
                                  package_id_input.city, 'State: ', package_id_input.state, 'Zipcode: ',
                                  package_id_input.zip_code,
                                  'Deadline: ', package_id_input.deadline, 'Weight: ', package_id_input.weight,
                                  'Notes: ',
                                  package_id_input.note, 'Status: ', package_id_input.status, 'Departure Time: ',
                                  package_id_input.departure_time, 'Delivery Time: ', package_id_input.delivery_time)
            for package_id_input in secondTruckTripPackages:  # gets package information from each package in truck 2
                if package_id_input.pid == p:
                    departure_time = package_id_input.departure_time
                    delivery_time = package_id_input.delivery_time
                    user_input_time = input("please enter a time in the 'HH:MM:SS' format: ")
                    convert_user_input_time = datetime.strptime(user_input_time, '%H:%M:%S')
                    if departure_time >= convert_user_input_time:
                        package_id_input.status = 'At HUB'
                        print('Package ID: ', package_id_input.pid, 'Address: ', package_id_input.address, 'City: ',
                              package_id_input.city, 'State: ', package_id_input.state, 'Zipcode: ',
                              package_id_input.zip_code,
                              'Deadline: ', package_id_input.deadline, 'Weight: ', package_id_input.weight, 'Notes: ',
                              package_id_input.note, 'Status: ', package_id_input.status, 'Departure Time: ',
                              package_id_input.departure_time, 'Delivery Time: ', package_id_input.delivery_time)
                    elif departure_time <= convert_user_input_time:
                        if convert_user_input_time < delivery_time:
                            package_id_input.status = 'In transit'
                            print('Package ID: ', package_id_input.pid, 'Address: ', package_id_input.address, 'City: ',
                                  package_id_input.city, 'State: ', package_id_input.state, 'Zipcode: ',
                                  package_id_input.zip_code,
                                  'Deadline: ', package_id_input.deadline, 'Weight: ', package_id_input.weight,
                                  'Notes: ',
                                  package_id_input.note, 'Status: ', package_id_input.status, 'Departure Time: ',
                                  package_id_input.departure_time, 'Delivery Time: ', package_id_input.delivery_time)
                        else:
                            package_id_input.status = 'Delivered'
                            print('Package ID: ', package_id_input.pid, 'Address: ', package_id_input.address, 'City: ',
                                  package_id_input.city, 'State: ', package_id_input.state, 'Zipcode: ',
                                  package_id_input.zip_code,
                                  'Deadline: ', package_id_input.deadline, 'Weight: ', package_id_input.weight,
                                  'Notes: ',
                                  package_id_input.note, 'Status: ', package_id_input.status, 'Departure Time: ',
                                  package_id_input.departure_time, 'Delivery Time: ', package_id_input.delivery_time)
            for package_id_input in thirdTruckTripPackages:  # gets package information from each package in truck 3
                if package_id_input.pid == p:
                    departure_time = package_id_input.departure_time
                    delivery_time = package_id_input.delivery_time
                    user_input_time = input("please enter a time in the 'HH:MM:SS' format: ")
                    convert_user_input_time = datetime.strptime(user_input_time, '%H:%M:%S')
                    if departure_time >= convert_user_input_time:  # checks if package is at the hub
                        package_id_input.status = 'At HUB'
                        print('Package ID: ', package_id_input.pid, 'Address: ', package_id_input.address, 'City: ',
                              package_id_input.city, 'State: ', package_id_input.state, 'Zipcode: ',
                              package_id_input.zip_code,
                              'Deadline: ', package_id_input.deadline, 'Weight: ', package_id_input.weight, 'Notes: ',
                              package_id_input.note, 'Status: ', package_id_input.status, 'Departure Time: ',
                              package_id_input.departure_time, 'Delivery Time: ', package_id_input.delivery_time)
                    elif departure_time <= convert_user_input_time:  # checks if package is in transit or delivered
                        if convert_user_input_time < delivery_time:
                            package_id_input.status = 'In transit'
                            print('Package ID: ', package_id_input.pid, 'Address: ', package_id_input.address, 'City: ',
                                  package_id_input.city, 'State: ', package_id_input.state, 'Zipcode: ',
                                  package_id_input.zip_code,
                                  'Deadline: ', package_id_input.deadline, 'Weight: ', package_id_input.weight,
                                  'Notes: ',
                                  package_id_input.note, 'Status: ', package_id_input.status, 'Departure Time: ',
                                  package_id_input.departure_time, 'Delivery Time: ', package_id_input.delivery_time)
                        else:
                            package_id_input.status = 'Delivered'
                            print('Package ID: ', package_id_input.pid, 'Address: ', package_id_input.address, 'City: ',
                                  package_id_input.city, 'State: ', package_id_input.state, 'Zipcode: ',
                                  package_id_input.zip_code,
                                  'Deadline: ', package_id_input.deadline, 'Weight: ', package_id_input.weight,
                                  'Notes: ',
                                  package_id_input.note, 'Status: ', package_id_input.status, 'Departure Time: ',
                                  package_id_input.departure_time, 'Delivery Time: ', package_id_input.delivery_time)
        # checks the status of each package in all three trucks
        elif first_input == 'status':
            user_input_input_time = input("Please enter starting time in 'HH:MM:SS' format: ")
            convert_user_input_time = datetime.strptime(user_input_input_time,
                                                        '%H:%M:%S')  # converts time inputted to datetime
            for p in firstTruckTripPackages:  # checks status of the first truck
                departure_time = p.departure_time
                delivery_time = p.delivery_time
                if departure_time >= convert_user_input_time:  # checks if package is at the HUB
                    p.status = 'At HUB'
                    print('Package ID: ', p.pid, 'Status: ', p.status)
                elif delivery_time <= convert_user_input_time:  # checks if package has been delivered
                    p.status = 'Delivered'
                    print('Package ID: ', p.pid, 'Status: ', p.status)
                elif departure_time <= convert_user_input_time < delivery_time:  # checks if package is in transit
                    p.status = 'In transit'
                    print('Package ID: ', p.pid, 'Status: ', p.status)
            for p in secondTruckTripPackages:  # checks status of the second truck
                departure_time = p.departure_time
                delivery_time = p.delivery_time
                if departure_time >= convert_user_input_time:  # checks if package is at the hub
                    p.status = 'At HUB'
                    print('Package ID: ', p.pid, 'Status: ', p.status)
                elif delivery_time <= convert_user_input_time:  # checks if package has been delivered
                    p.status = 'Delivered'
                    print('Package ID: ', p.pid, 'Status: ', p.status)
                elif departure_time <= convert_user_input_time < delivery_time:  # checks if package is in transit
                    p.status = 'In transit'
                    print('Package ID: ', p.pid, 'Status: ', p.status)
            for p in thirdTruckTripPackages:  # checks status of third truck
                departure_time = p.departure_time
                delivery_time = p.delivery_time
                if departure_time >= convert_user_input_time:  # checks if package is at the hub
                    p.status = 'At HUB'
                    print('Package ID: ', p.pid, 'Status: ', p.status)
                elif delivery_time <= convert_user_input_time:  # checks if package has been delivered
                    p.status = 'Delivered'
                    print('Package ID: ', p.pid, 'Status: ', p.status)
                elif departure_time <= convert_user_input_time < delivery_time:  # checks if package is in transit
                    p.status = 'In transit'
                    print('Package ID: ', p.pid, 'Status: ', p.status)
        elif first_input == 'exit':
            exit()


# makes the main.py file the  main
if __name__ == "__main__":
    main_one()
