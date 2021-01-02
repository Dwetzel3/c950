# Daniel Wetzel #000975667

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
                prev.next = prev.next
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
                                row[6].__str__(), 'Out For Delivery' )
            d[row[0]] = [row[1], row[5], row[2], row[4], row[6]]
    print( f'Processed {line_count} lines.' )

''' - searches for package 40
print( packageFile.search( '40' ) )
'''

'''
for key in d:
    print( 'Package ID', key, 'corresponds to', d[key] )
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

print('populated newlist:', newlist)

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

print( '\nkeys are as follows:\n', dist.keys() )

'''
List of packages on trucks
'''

trucks = [1, 4, 5, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 19, 20, 21, 2, 3, 12, 18, 22, 24, 26, 27, 29, 30, 31, 33, 36, 38, 6, 23, 25, 28, 32, 34, 35, 37, 39, 40]

truck1 = [1, 4, 5, 8, 7, 10, 11, 13, 14, 15, 16, 17, 19, 20, 21] #leaves at 08:00

#The wrong delivery address for package #9, Third District Juvenile Court,
# will be corrected at 10:20 a.m. The correct address is “410 S State St., Salt Lake City, UT 84111”.
# You may assume that WGUPS knows the address is incorrect and when it will be corrected.

truck2 = [2, 3, 12, 18, 22, 24, 26, 27, 29, 30, 31, 33, 36, 38] #leaves at 08:00
truck3 = [6, 9, 23, 25, 28, 32, 34, 35, 37, 39, 40] #leaves at 09:05


'''
Dict for correcting bad addresses
'''

badAdd = {}


def updateAddress(package):
    print('Package Number:', package)
    print('Address:', returnDistAddress(package))
    print('Enter new address:')
    newAddress = '410 S State St., Salt Lake City, UT 84111'
    addSplit = newAddress.split('.')
    print(addSplit[0])
    for j in range(len(distList)):
        if addSplit[0] in distList[j]:
            print( 'Package', package, 'updated to address ID:', j )
            #packageAndID[i] = j



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

'''
FIXME!!!!!!! NEEDS TO ASSIGN ALL STOPS WITH AN ADDRESS INDEX
'''

for i in trucks:
    for j in range(len(distList)):
        if packageFile.search( f'{i}' )[0] in distList[j]:
            print( 'package', i, 'located at address ID:', j )
            packageAndID[i] = j


print('package and ID:', packageAndID)

def findClosestOnTruck(input, truck):
    print(newlist)
    shortest = 100
    print('working on', input)
    if input == 0:
        print('0!')
        print(newlist[input][0][0])
        for j in range( 27 ):
            if newlist[input][0][0] == 0.0:
                print( 'zero')
                for i in range( 27 ):
                    if float( newlist[0][0][j] ) < float( shortest ):
                        shortest = float( newlist[input][0][j] )
            elif newlist[0][0][j] != '' and newlist[0][0][j] != '0.0':
                print( 'valid' )
                for key, value in packageAndID.items():
                    if j == value:
                        if key in truck:
                            print( value, 'On Truck! Package', key )
                            print( 'Key:', key )
                            if float( newlist[0][0][j] ) < float( shortest ):
                                shortest = float( newlist[0][0][j] )
                                closest.add( input, shortest )
                                neighborsList.add(input,key)
                                print( 'new shortest distance for package', input, ':', shortest, 'found at index', j,
                                       'which belongs to', key, 'at', returnDistAddress( j ) )
            elif newlist[0][0][j] == '':
                print('empty')
                print(packageAndID)
                #print([0], [j], 'is empty')
                #print('inverse is', newlist[j][0][0])
                #print('inverse of', j, ':', newlist[j][0][input])
                for key, value in packageAndID.items():
                    if j == value:
                        if key in truck:
                            print( input, 'Leaving the HUB! Checking package', key )
                            print( 'key:', key )
                            if float( newlist[j][0][0] ) < float( shortest ):
                                shortest = float( newlist[j][0][0] )
                                closest.add( input, shortest )
                                print('closest:', closest)
                                neighborsList.add(input, key)
                                print( 'new norm shortest distance for package', input, ':', shortest, 'found at index',j,
                                       'which belongs to package', key, 'at', returnDistAddress(j) )
    else:
        print( 'working on package:', input, 'with an address of:', packageAndID[input] )
        for j in range( 27 ):
            print(j)
            if newlist[packageAndID[input]][0][0] == 0.0:
                for i in range( 27 ):
                    if float( newlist[input][0][j] ) < float( shortest ):
                        shortest = float( newlist[input][0][j] )
            elif newlist[packageAndID[input]][0][j] != '' and newlist[packageAndID[input]][0][j] != '0.0':
                print(newlist[packageAndID[input]][0][j])
                for key, value in packageAndID.items():
                    if j == value:
                        if key in truck:
                            print( input, 'On Truck! Package', key )
                            print( 'Key:', key )
                            if float( newlist[packageAndID[input]][0][j] ) < float( shortest ):
                                shortest = float( newlist[packageAndID[input]][0][j] )
                                closest.add( input, shortest )
                                neighborsList.add(input,key)
                                print( 'new shortest distance for package', input, ':', shortest, 'found at index', j,
                                       'which belongs to', key, 'at', returnDistAddress( j ) )
            elif newlist[packageAndID[input]][0][j] == '':
                print("it's one of those quotes", j)
                print(newlist[j][0][packageAndID[input]])
                #print([key], [j], 'is empty!')
                #print('inverse is', newlist[j][0][packageAndID[input]])
                #print('inverse of', j, ':', newlist[j][0][input])
                for key, value in packageAndID.items():
                    if j == value:
                        if key in truck:
                            print( value, 'On Truck! Package', key )
                            print( 'key:', key )
                            if float( newlist[j][0][packageAndID[input]] ) < float( shortest ):
                                shortest = float( newlist[j][0][packageAndID[input]] )
                                closest.add( input, shortest )
                                neighborsList.add(input, key)
                                print( 'new norm shortest distance for package', input, ':', shortest, 'found at index',j,
                                       'which belongs to package', key, 'at', returnDistAddress(j) )
    print( 'Package IDs and their closest neighbors:', closest )
    print('neighbors:', neighborsList)


'''
ADD FUNCTIONALITY OF CURRENT STOP AND TO CONTINUE SEARCHING FOR THE CLOSEST NEIGHBOR FOR NEXT CURRENT STOP
'''
class stops:
    correctedBadAdd = False
    currentStop = 0
    mileage = 0.0
    time = 800
    addedTime = 0


listSize = len(truck1)

used = neighbors()


def stopOrder(input, truck):
    findClosestOnTruck(input, truck )
    quickest = 100
    quickIndex = 0
    print('Closest before:', closest)
    print(len(closest))
    print(packageAndID)
    for i in closest:
        if closest[i] < quickest and i not in used:
            print( 'Closest neighbor for package', input, 'on the truck: Package', neighborsList.__getitem__(input), 'with a distance of', closest.__getitem__(input) )
            quickest = closest.__getitem__(input)
            print('quickest is:', quickest)
            quickIndex = neighborsList.__getitem__(input)
            print('quickindex:', quickIndex)
            stops.mileage += float( closest[i] )
            stops.addedTime += float(closest[i] / .3)
            used.add( quickIndex, closest.__getitem__(input) )
            print( 'used', used )
            print('Closest:', closest)
    print(closest)
    print( 'quickindex is', quickIndex )
    print('deleting:', quickIndex)
    truck.remove(quickIndex)
    print(truck)
    print('mileage', stops.mileage)
    print('Added Time', stops.addedTime)
    stops.currentStop = quickIndex

def returnToHub(stop):
    print('Distance from last stop to HUB:', newlist[packageAndID[stop]][0][0])
    stops.mileage += float( newlist[packageAndID[stop]][0][0] )
    stops.addedTime += float( (newlist[packageAndID[stop]][0][0])) / .3
    print('Final Mileage', stops.mileage)
    finalTime = stops.time + stops.addedTime / 60 * 100
    print('Final Time:', finalTime)
    if finalTime > 1020:
        print('Past 10:20')
        stops.correctedBadAdd = True
    print('Package 9 Corrected yet?', stops.correctedBadAdd)
    if int( finalTime ) < 1000:
        print( 'Finishing Time: ' + '0' + finalTime.__str__()[0] + ':' + finalTime.__str__()[1] + finalTime.__str__()[2])
    else:
        print( 'Finishing Time: ' + finalTime.__str__()[0] + finalTime.__str__()[1] + ':' + finalTime.__str__()[2] + finalTime.__str__()[3])
    stops.currentStop = 0


while len(truck1) > 0:
    stopOrder(stops.currentStop, truck1)
    print( 'remaining list:', truck1 )
    if len(truck1) == 0:
        print('Out of Stops. Returning to HUB')
        returnToHub(stops.currentStop)


'''Finds package ID and searches through distList for the same address and prints out the addressId'''

print(packageAndID)

'''
print(packageAndID[7])
'''


while len( truck2 ) > 0:
    stopOrder( stops.currentStop, truck2 )
    print( 'remaining list:', truck2 )
    if len( truck2 ) == 0:
        print('Out of Stops. Returning to HUB')
        returnToHub( stops.currentStop )


while len( truck3 ) > 0:
    stopOrder( stops.currentStop, truck3 )
    print( 'remaining list:', truck3 )
    if len( truck3 ) == 0:
        print('Out of Stops. Returning to HUB')
        returnToHub( stops.currentStop )


if stops.correctedBadAdd is True:
    updateAddress(9)