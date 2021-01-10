# Daniel Wetzel #000975667

import datetime

'''
sets inital capacity for HashTable
'''
from operator import index

INITIAL_CAPACITY = 50

'''
imports the csv module to use csv files
'''

import csv


class Node:
    def __init__(self, pkg_id, address, deadline, city, zipcode, weight, status):
        self.key = pkg_id
        self.value = [address, deadline, city, zipcode, weight, status]
        self.next = None


'''
creates a Hash Table for packages and their data
'''


class HashTable:
    def __init__(self):
        self.capacity = INITIAL_CAPACITY
        self.size = 0
        self.buckets = [None] * self.capacity

    def hash(self, key):
        hashsum = 0
        for idx, c in enumerate( key ):
            hashsum += (idx + len( key )) ** ord( c )
            hashsum = hashsum % self.capacity
        return hashsum

    '''
    insert function
    '''

    def insert(self, pkg_id, address, deadline, city, zipcode, weight, status):
        self.size += 1
        index = self.hash( pkg_id )
        node = self.buckets[index]
        if node is None:
            self.buckets[index] = Node( pkg_id, address, deadline, city, zipcode, weight, status )
            return
        prev = node
        while node is not None:
            prev = node
            node = node.next
        prev.next = Node( pkg_id, address, deadline, city, zipcode, weight, status )

    '''
    search function
    '''

    def search(self, key):
        index = self.hash( key )
        node = self.buckets[index]
        while node is not None and node.key != key:
            node = node.next
        if node is None:
            return None
        else:
            return node.value

    '''
    remove function
    '''

    def remove(self, key):
        index = self.hash( key )
        node = self.buckets[index]
        prev = None

        while node is not None and node.key != key:
            prev = node
            node = node.next
        if node is None:
            return None
        else:
            self.size -= 1
            result = node.value
            if prev is None:
                node = None
            else:
                prev.next = prev.next.next
            return result

distSum = 0

'''
creates a new HashTable
'''

packageFile = HashTable()

'''
creates an empty dictionary
'''

d = {}

'''
converts the WGUPS_Package_File.csv csv into a python list
'''

with open( 'WGUPS_Package_File.csv' ) as csv_file:
    csv_reader = csv.reader( csv_file )
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            line_count += 1
            packageFile.insert( row[0].__str__(), row[1].__str__(), row[5].__str__(), row[2].__str__(), row[4].__str__(),
                                row[6].__str__(), 'At Hub' )
            d[row[0]] = [row[1], row[5], row[2], row[4], row[6]]
    #print( f'Processed {line_count} lines.' )

''' - searches for package 40
print( packageFile.search( '40' ) )
'''


'''
creates an empty dictionary
'''

dist = {}

'''
converts the WGUPS_Distance_Table.csv into a python list
'''

with open( 'WGUPS_Distance_Table.csv' ) as csv_file:
    csv_reader = csv.reader( csv_file )
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            line_count += 1
            dist[row[0]] = [row[2:29]]
    print( f'Processed {line_count} lines.' )

'''
print( 'dist:', dist )
'''

'''
newList used to format distance data into an ordered list
'''

newlist = []

'''
populates newlist
'''

for key in dist:
    #print( '\nAddress for', key, 'corresponding distances are', dist[key] )
    newlist.append( dist[key] )
    print('appending', key, 'to', dist)

#print('populated newlist:', newlist)

'''
assigns address keys from dist to list distList
'''

distList = []

for key in dist:
    distList.append( key )

print( '\ndist list: ', distList[0] )

'''
returns the specified address from distList
'''


def findDistAddress(input):
    print(distList[input])

def returnDistAddress(input):
    return distList[input]



'''
Find shortest of specified row
'''

distSum = 0  # Initial sum of total shortest distance


def findClosest(row):
    smallest = 100
    global distSum
    listCounter = 0
    positive = False  # check to make sure the 0.0 dist location is not pertaining to itself

    def closest():
        print( '\nClosest neighbor distance for:\n', returnDistAddress( row ) )
        print( '\nIndex in the distance list:', listCounter, '\n' )
        print( 'Closest address:' )
        print( distList[listCounter] )

    for i in newlist[row][0]:
        j = range( 27 )
        if i == '':
            break
        if i == '0.0' and not positive:
            smallest = i
            closest()
        elif i != '' and i != '0.0' and float( i ) < float( smallest ):
            smallest = i
            closest()
            positive = True
        listCounter += 1
    print( '\nWith a distance of only', smallest, 'miles' )
    distSum += float( smallest )
    print( 'Total distance thus far:', distSum, 'miles\n' )


'''
call findClosest()
'''

findClosest( 1 )

'''
compare starting index to 
'''

'''
- prints each key from the distance csv
- names and addresses
'''
'''
print( '\nkeys are as follows:\n', dist.keys() )
'''
'''
List of packages on trucks
'''

trucks = [1, 4, 5, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 19, 20, 21, 2, 3, 12, 18, 22, 24, 26, 27, 29, 30, 31, 33, 36, 38, 6, 23, 25, 28, 32, 34, 35, 37, 39, 40]

truck1 = [1, 4, 5, 8, 7, 10, 11, 13, 14, 15, 16, 17, 19, 20, 34, 40] #leaves at 08:00

#The wrong delivery address for package #9, Third District Juvenile Court,
# will be corrected at 10:20 a.m. The correct address is “410 S State St., Salt Lake City, UT 84111”.
# You may assume that WGUPS knows the address is incorrect and when it will be corrected.

truck2 = [2, 3, 12, 18, 21, 22, 24, 26, 27, 29, 30, 31, 33, 36, 37, 38] #leaves at 08:00
truck3 = [6, 9, 23, 25, 28, 32, 35, 39] #leaves after truck 1 gets back

datetime.time()

class checks:
    searching = False
    searchTruck = 0
    checkall = False
    checkallTime = 100000
    time = 800
    workingOn = 0


'''used for trucks 1'''
class stopsa:
    tentwenty = False
    addCorrected = False
    currentStop = 0
    mileage = 0.0
    time = 800
    addedTime = 0
    finalTime = 0
    triggerStop = 100000
    triggerTime = 100000
    override = 0
    unchanged = True
    departTime = 800

'''used for truck 2'''
class stopsb:
    tentwenty = False
    addCorrected = False
    currentStop = 0
    mileage = 0.0
    time = 800
    addedTime = 0
    finalTime = 0
    triggerStop = 100000
    triggerTime = 100000
    override = 0
    unchanged = True
    departTime = 800



'''used for truck 3'''
class stopsc:
    tentwenty = False
    addCorrected = False
    currentStop = 0
    mileage = 0.0
    datetime.time()
    time = datetime.time(8,0)
    addedTime = 0
    finalTime = 0
    triggerStop = 100000
    triggerTime = 100000
    override = 0
    unchanged = True
    departTime = 800
    initializedTime = False
    initialHours = 0
    firstRun = True



def checkPackageStatus(package, time):
    print('Searching trucks')
    if package in truck1:
        print('truck 1')
        stopsa.triggerTime = time
        stopsa.triggerStop = package
    elif package in truck2:
        print(package, 'in truck 2')
        stopsb.triggerTime = time
        stopsb.triggerStop = package
        print(stopsb.triggerStop)
    elif package in truck3:
        print( 'truck 3' )
        stopsc.triggerTime = time
        stopsc.triggerStop = package
    else:
        print('not on trucks')

print('Would you like to check the status on a package? Y/N')
x = input()
if x.lower() == 'y':
    y = input("Please enter a package ID 1-40 or type 'All'\n")
    if y.lower() == 'all':
        checks.checkall = True
        z = input( 'Please enter a time. IE: 1030\n' )
        checks.checkallTime = z
    elif type(int(y)) is int:
        z = input('Please enter a time. IE: 1030\n')
        checks.time = z
        print('Checking for a package', y, 'at time', z)
        if int(y) in truck1:
            checks.searchTruck = 1
        elif int(y) in truck2:
            checks.searchTruck = 2
        elif int(y) in truck3:
            checks.searchTruck = 3
        checks.searching = True
        checkPackageStatus(int(y), int(z))
elif x.lower() == 'n':
    y = input("Enter 'Q' to quit.\n")
    if y.lower() == 'q':
        quit()
else:
    print('Exiting program.')
    quit()

'''
Dict for correcting bad addresses
'''

badAdd = {}

def updateAddress(package):
    print('Package Number:', package)
    print('Address:', returnDistAddress(package))
    print('Enter new address:')
    newAddress = '410 S State St,Salt Lake City,UT,84111'
    addSplit = newAddress.split(',')
    print(addSplit[0])
    for j in range(len(distList)):
        if addSplit[0] in distList[j]:
            print(distList[j])
            print( 'Package', package, 'updated to address ID:', j )
            distList[package] = distList[j]
            print( packageFile.search( package.__str__() ) )
            packageFile.insert( package.__str__(), distList[j], packageFile.search( package.__str__() )[1], packageFile.search( package.__str__() )[2],
                               addSplit[3],
                                packageFile.search( package.__str__() )[4], packageFile.search( package.__str__() )[5] )
            packageFile.remove( package.__str__() )
            print( packageFile.search( package.__str__() ) )
            for j in range( len( distList ) ):
                if packageFile.search( f'{package}' )[0] in distList[j]:
                    print( 'package', package, 'located at address ID:', j )
                    packageAndID[package] = j
                    break

    print('Corrected Address:', returnDistAddress(package))




'''
Loops through the list of packages and their corresponding distances from each other
'''


class truckManifest( dict ):
    def __init__(self):
        self = dict()

    def add(self, key, value):
        self[key] = value

    def remove(self, key):
        del self[key]

class neighbors( dict ):
    def __init__(self):
        self = dict()

    def add(self, key, value):
        self[key] = value

    def remove(self, key):
        del self[key]

class used( dict ):
    def __init__(self):
        self = dict()

    def add(self, key, value):
        self[key] = value

    def remove(self, key):
        del self[key]

closest = truckManifest()
neighborsList = neighbors()
used = neighbors()
packageAndID = neighbors()
correspondingAdd = []


print('length of distlist:', len(distList))


for i in trucks:
    for j in range(len(distList)):
        if packageFile.search( f'{i}' )[0] in distList[j]:
            print( 'package', i, 'located at address ID:', j )
            packageAndID[i] = j


print('package and ID:', packageAndID)

def findClosestOnTruck(input, truck):
    shortest = 100
    if input == 0:
        print(newlist[input][0][0])
        for j in range( 27 ):
            if newlist[input][0][0] == 0.0:
                for i in range( 27 ):
                    if float( newlist[0][0][j] ) < float( shortest ):
                        shortest = float( newlist[input][0][j] )
            elif newlist[0][0][j] != '' and newlist[0][0][j] != '0.0':
                for key, value in packageAndID.items():
                    if j == value:
                        if key in truck:
                            '''
                            Part A - Self-Adjusting greedy algorithm
                            '''
                            print( truck )
                            print( 'Index of ', key, 'before adjusting:', truck.index( key ) )
                            del truck[truck.index( key )]
                            truck.append(key)
                            print( truck )
                            print( value, 'On Truck! Package', key )
                            if float( newlist[0][0][j] ) < float( shortest ):
                                shortest = float( newlist[0][0][j] )
                                closest.add( input, shortest )
                                neighborsList.add(input,key)
                                print( 'New shortest distance for package', input, ':', shortest, 'found at index', j,
                                       'which belongs to', key, 'at', returnDistAddress( j ) )
            elif newlist[0][0][j] == '':
                for key, value in packageAndID.items():
                    if j == value:
                        if key in truck:
                            '''
                            Part A - Self-Adjusting greedy algorithm
                            '''
                            print(truck)
                            print('Index of ', key, 'before adjusting:', truck.index(key))
                            del truck[truck.index(key)]
                            truck.append(key)
                            print(truck)
                            print( input, 'Leaving the HUB! Checking package', key )
                            if float( newlist[j][0][0] ) < float( shortest ):
                                shortest = float( newlist[j][0][0] )
                                closest.add( input, shortest )
                                neighborsList.add(input, key)
                                print( 'new norm shortest distance for package', input, ':', shortest, 'found at index',j,
                                       'which belongs to package', key, 'at', returnDistAddress(j) )
    else:
        print( 'Working on package:', input, 'with an address index of:', packageAndID[input] )
        for j in range( 27 ):
            if newlist[packageAndID[input]][0][0] == 0.0:
                for i in range( 27 ):
                    if float( newlist[input][0][j] ) < float( shortest ):
                        shortest = float( newlist[input][0][j] )
            elif newlist[packageAndID[input]][0][j] != '' and newlist[packageAndID[input]][0][j] != '0.0':
                for key, value in packageAndID.items():
                    if j == value:
                        if key in truck:
                            '''
                            Part A - Self-Adjusting greedy algorithm
                            '''
                            print( input, 'On Truck! Package', key )
                            print( 'Key:', key )
                            print( truck )
                            print( 'Index of ', key, 'before adjusting:', truck.index( key ) )
                            del truck[truck.index( key )]
                            truck.append(key)
                            print( truck )
                            if float( newlist[packageAndID[input]][0][j] ) < float( shortest ):
                                shortest = float( newlist[packageAndID[input]][0][j] )
                                closest.add( input, shortest )
                                neighborsList.add(input,key)
                                print( 'New shortest distance for package', input, ':', shortest, 'found at index', j,
                                       'which belongs to', key, 'at', returnDistAddress( j ) )
            elif newlist[packageAndID[input]][0][j] == '':
                for key, value in packageAndID.items():
                    if j == value:
                        if key in truck:
                            '''
                            Part A - Self-Adjusting greedy algorithm
                            '''
                            print( value, 'On Truck! Package', key )
                            print( 'key:', key )
                            print( truck )
                            print( 'Index of ', key, 'before adjusting:', truck.index( key ) )
                            del truck[truck.index( key )]
                            truck.append(key)
                            print( truck )
                            if float( newlist[j][0][packageAndID[input]] ) < float( shortest ):
                                shortest = float( newlist[j][0][packageAndID[input]] )
                                closest.add( input, shortest )
                                neighborsList.add(input, key)
                                print( 'New shortest distance for package', input, ':', shortest, 'found at index',j,
                                       'which belongs to package', key, 'at', returnDistAddress(j) )
    print( 'Package IDs and their closest neighbors:', closest )
    print('neighbors:', neighborsList)



listSize = len(truck1)

used = neighbors()

def stopOrder(input, truck):
    if checks.workingOn == 1 and stopsa.finalTime > stopsa.time:
        for i in truck1:
            packageFile.search( i.__str__() )[5] = 'Out For Delivery'
    elif checks.workingOn == 2 and stopsb.finalTime > stopsb.time:
        for i in truck2:
            packageFile.search( i.__str__() )[5] = 'Out For Delivery'
    elif checks.workingOn == 3 and stopsc.finalTime > stopsc.time:
        for i in truck3:
            packageFile.search( i.__str__() )[5] = 'Out For Delivery'
            print('Changing 3!')
    findClosestOnTruck(input, truck )
    quickest = 100
    quickIndex = 0
    print(packageAndID)
    for i in closest:
        if closest[i] < quickest and i not in used:
            print( 'Closest neighbor for package', input, 'on the truck: Package', neighborsList.__getitem__(input), 'with a distance of', closest.__getitem__(input) )
            quickest = closest.__getitem__(input)
            quickIndex = neighborsList.__getitem__(input)
            if truck == truck1:
                stopsa.mileage += float( closest[i] )
                stopsa.addedTime += float(closest[i] / .3)
            elif truck == truck2:
                stopsb.mileage += float( closest[i] )
                stopsb.addedTime += float(closest[i] / .3)
            else:
                stopsc.mileage += float( closest[i] )
                stopsc.time = float(closest[i] / .3)
            used.add( quickIndex, closest.__getitem__(input) )
    print(closest)
    truck.remove(quickIndex)
    print(truck)
    if truck == truck2:
        print('Mileage', stopsb.mileage)
        print('Added Time', stopsb.addedTime)
        addedHours = stopsb.addedTime // 60
        print( 'Added Hours:', addedHours )
        addedMinutes = stopsb.addedTime % 60
        print( 'Added Minutes:', addedMinutes )
        stopsb.finalTime = stopsb.time + (addedHours * 100) + addedMinutes
        print(stopsb.finalTime)
        if input == 0:
            print('INPUT 0')
            stopsb.departTime = stopsb.time
            print(stopsb.departTime)
        finalTime = stopsb.finalTime
        if checks.checkall is True:
            print( 'checkall' )
            if finalTime >= float(checks.checkallTime):
                print('checkallTime')
                for i in range( len( trucks ) ):
                    print( 'Address -- Commitment -- City -- Zipcode -- Weight -- Status' )
                    print( packageFile.search( (i + 1).__str__() ) )
                quit()
        if stopsb.triggerTime < 1000:
            stopsb.override = '0'+stopsb.triggerTime.__str__()
        else:
            stopsb.override = stopsb.triggerTime
        if len(truck) == 0 and checks.searchTruck == 2:
            stopsb.triggerTime = finalTime
        if finalTime >= stopsb.triggerTime and checks.searching is True:
            print('\nPackage ID: ' + stopsb.triggerStop.__str__() + '. Status as of ' + stopsb.override.__str__() + ':\n')
            printPackage(stopsb.triggerStop)
            quit()
        if stopsb.tentwenty is True and stopsb.addCorrected is False:
            updateAddress(9)
            stopsb.addCorrected = True
    elif truck == truck1:
        print( 'Mileage', stopsa.mileage )
        print( 'Added Time', stopsa.addedTime )
        addedHours = stopsa.addedTime // 60
        print( 'Added Hours:', addedHours )
        addedMinutes = stopsa.addedTime % 60
        print( 'Added Minutes:', addedMinutes )
        stopsa.finalTime = stopsa.time + (addedHours * 100) + addedMinutes
        print(stopsa.finalTime)
        if input == 0:
            print('INPUT 0')
            stopsa.departTime = stopsa.time
            print(stopsa.departTime)
        finalTime = stopsa.finalTime
        if checks.checkall is True:
            print( 'checkall' )
            if finalTime >= float(checks.checkallTime):
                for i in range( len( trucks ) ):
                    print( 'Address -- Commitment -- City -- Zipcode -- Weight -- Status' )
                    print( packageFile.search( (i + 1).__str__() ) )
                quit()
        if stopsa.triggerTime < 1000:
            stopsa.override = '0'+stopsa.triggerTime.__str__()
        else:
            stopsa.override = stopsa.triggerTime
        if len(truck) == 0 and checks.searchTruck == 1:
            stopsa.triggerTime = finalTime
        if finalTime >= stopsa.triggerTime and checks.searching is True:
            print(stopsa.triggerStop)
            print(checks.searchTruck)
            print('\nPackage ID: ' + stopsa.triggerStop.__str__() + '. Status as of ' + stopsa.override.__str__() + ':\n')
            printPackage( stopsa.triggerStop )
            quit()
        if stopsa.tentwenty is True and stopsa.addCorrected is False:
            updateAddress( 9 )
            stopsa.addCorrected = True
    elif truck == truck3:
        print('Truck 3')
        print( 'Mileage', stopsc.mileage )
        print('Time:', stopsc.time)
        '''if stopsc.initializedTime is False:
            print('Time:', stopsc.time)
            stopsc.initialHours = stopsc.time // 100
            print('initial hours', stopsc.initialHours)
            stopsc.time = stopsc.time % 100
            stopsc.initializedTime = True
            print('New Time:', stopsc.time)
            stopsc.addedTime = stopsc.addedTime + stopsc.time
        print( 'Added Time', stopsc.addedTime )
        addedHours = stopsc.addedTime // 60
        if stopsc.firstRun is True:
            addedHours = stopsc.initialHours
            stopsc.firstRun = False
        print('Added Hours:', addedHours)
        addedMinutes = stopsc.addedTime % 60
        print('Added Minutes:', addedMinutes)
        if stopsc.initializedTime is False:
            stopsc.finalTime = (stopsc.time // 100) * 100 + (stopsc.time % 60)
            stopsc.initializedTime = True
        else:
            stopsc.finalTime = stopsc.time
        print(stopsc.finalTime)
        if input == 0:
            print('INPUT 0')
            stopsc.departTime = stopsc.time
            print(stopsc.departTime)
        if stopsc.finalTime % 100 > 60:
            stopsc.finalTime = stopsc.time'''
        finalTime = datetime.time(8,0).hour * 100
        print('current time:', finalTime)
        '''
        if checks.checkall is True:
            print( 'checkall' )
            if finalTime >= float(checks.checkallTime):
                for i in range( len( trucks ) ):
                    print( 'Address -- Commitment -- City -- Zipcode -- Weight -- Status' )
                    print( packageFile.search( (i + 1).__str__() ) )
                quit()
        if finalTime >= 1020:
            stopsc.tentwenty = True
        if stopsc.triggerTime < 1000:
            stopsc.override = '0'+stopsc.triggerTime.__str__()
        else:
            stopsc.override = stopsc.triggerTime
        if len(truck3) == 0 and checks.searchTruck == 3:
            stopsc.triggerTime = finalTime
            print('trigger time:', stopsc.triggerTime)
        if finalTime >= stopsc.triggerTime and checks.searching is True:
            print(stopsc.triggerStop)
            print(checks.searchTruck)
            print('\nPackage ID: ' + stopsc.triggerStop.__str__() + '. Status as of ' + stopsc.override.__str__() + ':\n')
            printPackage( stopsc.triggerStop )
            quit()
        if stopsc.tentwenty is True and stopsc.addCorrected is False:
            updateAddress( 9 )
            stopsc.addCorrected = True'''
    if int( finalTime ) < 1000:
        currentTime = '0' + finalTime.__str__()[0] + ':' + finalTime.__str__()[1] + finalTime.__str__()[2]
    else:
        currentTime = finalTime.__str__()[0] + finalTime.__str__()[1] + ':' + finalTime.__str__()[2] + finalTime.__str__()[3]
    print(packageFile.search(input.__str__()))
    packageFile.search(quickIndex.__str__())[5] = 'Delivered at ' + currentTime

    print( packageFile.search( input.__str__() ) )
    if truck == truck2:
        stopsb.currentStop = quickIndex
    elif truck == truck1:
        stopsa.currentStop = quickIndex
    elif truck == truck3:
        stopsc.currentStop = quickIndex


def returnToHubA(stop):
    print('Distance from last stop to HUB:', newlist[packageAndID[stop]][0][0])
    stopsa.mileage += float( newlist[packageAndID[stop]][0][0] )
    stopsa.addedTime += float( (newlist[packageAndID[stop]][0][0])) / .3
    print('Final Mileage', stopsa.mileage)
    stopsa.finalTime = stopsa.time + stopsa.addedTime / 60 * 100
    addedHours = stopsa.addedTime // 60
    addedMinutes = stopsa.addedTime % 60

    stopsa.finalTime = stopsa.time + (addedHours * 100) + addedMinutes
    print('Package 9 Corrected yet?', stopsa.addCorrected)
    if int( stopsa.finalTime ) < 1000:
        print( 'Finishing Time:  ' + '0' + stopsa.finalTime.__str__()[0] + ':' + stopsa.finalTime.__str__()[1] + stopsa.finalTime.__str__()[2])
    else:
        print( 'Finishing Time: ' + stopsa.finalTime.__str__()[0] + stopsa.finalTime.__str__()[1] + ':' + stopsa.finalTime.__str__()[2] + stopsa.finalTime.__str__()[3])
    stopsa.currentStop = 0

    if len(truck1) == 0 and checks.searchTruck == 1:
        printPackage( stopsa.triggerStop )

def returnToHubB(stop):
    print( 'Distance from last stop to HUB:', newlist[packageAndID[stop]][0][0] )
    stopsb.mileage += float( newlist[packageAndID[stop]][0][0] )
    stopsb.addedTime += float( (newlist[packageAndID[stop]][0][0]) ) / .3
    stopsb.finalTime = stopsb.time + stopsb.addedTime / 60 * 100
    addedHours = stopsb.addedTime // 60
    addedMinutes = stopsb.addedTime % 60

    stopsb.finalTime = stopsb.time + (addedHours * 100) + addedMinutes
    print('Package 9 Corrected yet?', stopsb.addCorrected)
    if int( stopsb.finalTime ) < 1000:
        print( 'Finishing Time: ' + '0' + stopsb.finalTime.__str__()[0] + ':' + stopsb.finalTime.__str__()[1] + stopsb.finalTime.__str__()[2])
    else:
        print( 'Finishing Time: ' + stopsb.finalTime.__str__()[0] + stopsb.finalTime.__str__()[1] + ':' + stopsb.finalTime.__str__()[2] + stopsb.finalTime.__str__()[3])
    stopsb.currentStop = 0

    if len(truck2) == 0 and checks.searchTruck == 2:
        printPackage( stopsb.triggerStop )

def returnToHubC(stop):
    print( 'Distance from last stop to HUB:', newlist[packageAndID[stop]][0][0] )
    stopsc.mileage += float( newlist[packageAndID[stop]][0][0] )
    stopsc.addedTime += float( (newlist[packageAndID[stop]][0][0]) ) / .3
    stopsc.finalTime = stopsc.time + stopsc.addedTime / 60 * 100
    addedHours = stopsc.addedTime // 60
    addedMinutes = stopsc.addedTime % 60
    print(addedHours)
    print(addedMinutes)

    stopsc.finalTime = stopsc.time + (addedHours * 100) + addedMinutes
    print( 'Package 9 Corrected yet?', stopsc.addCorrected )
    print('Final Time', stopsc.finalTime)
    if int( stopsc.finalTime ) < 1000:
        print( 'Finishing Time:  ' + '0' + stopsc.finalTime.__str__()[0] + ':' + stopsc.finalTime.__str__()[1] +
               stopsc.finalTime.__str__()[2] )
    else:
        print( 'Finishing Time: ' + stopsc.finalTime.__str__()[0] + stopsc.finalTime.__str__()[1] + ':' +
               stopsc.finalTime.__str__()[2] + stopsc.finalTime.__str__()[3] )
    stopsc.currentStop = 0

    if len(truck3) == 0 and checks.searchTruck == 3:
        printPackage( stopsc.triggerStop )


'''Finds package ID and searches through distList for the same address and prints out the addressId'''

print(packageAndID)

'''runs main program'''

def rollOut():
    while len(truck1) > 0:
        checks.workingOn = 1
        stopOrder(stopsa.currentStop, truck1)
        print( 'remaining list: truck 1', truck1 )
        if len(truck1) == 0:
            print('Out of Stops. Returning to HUB')
            returnToHubA( stopsa.currentStop )


    while len( truck2 ) > 0:
        checks.workingOn = 2
        stopOrder( stopsb.currentStop, truck2 )
        print( 'remaining list: truck 2', truck2 )
        if len( truck2 ) == 0:
            print('Out of Stops. Returning to HUB')
            returnToHubB( stopsb.currentStop )


    while len( truck3 ) > 0:
        checks.workingOn = 3
        stopsc.time = stopsa.finalTime
        stopOrder( stopsc.currentStop, truck3 )
        print( 'remaining list: truck 3', truck3 )
        if len( truck3 ) == 0:
            stopsc.triggerTime = stopsc.finalTime
            print('Out of Stops. Returning to HUB')
            returnToHubC( stopsc.currentStop )
        if checks.searching is False:
            'Printing Status for all Packages'
            for i in range(len(trucks)):
                print( 'Address -- Commitment -- City -- Zipcode -- Weight -- Status' )
                print( packageFile.search((i + 1).__str__() ) )


def printPackage(package):
    if package in truck3:
        if int(checks.time) < 830:
            for i in truck3:
                packageFile.search( i.__str__() )[5] = 'At Hub'
    print('Address -- Commitment -- City -- Zipcode -- Weight -- Status')
    print( packageFile.search(package.__str__()) )

rollOut()