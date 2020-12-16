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
        for idx, c in enumerate(key):
            hashsum += (idx + len(key)) ** ord(c)
            hashsum = hashsum % self.capacity
        return hashsum

    '''
    insert function
    '''

    def insert(self, pkg_id, address, deadline, city, zipcode, weight, status):
        self.size += 1
        index = self.hash(pkg_id)
        node = self.buckets[index]
        if node is None:
            self.buckets[index] = Node(pkg_id, address, deadline, city, zipcode, weight, status)
            return
        prev = node
        while node is not None:
            prev = node
            node = node.next
        prev.next = Node(pkg_id, address, deadline, city, zipcode, weight, status)

    '''
    search function
    '''

    def search(self, key):
        index = self.hash(key)
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
        index = self.hash(key)
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

ht1 = HashTable()

'''
creates an empty dictionary
'''

d = {}

'''
converts the WGUPS_Package_File.csv csv into a python list
'''

with open('WGUPS_Package_File.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            line_count += 1
            ht1.insert(row[0].__str__(), row[1].__str__(), row[5].__str__(), row[2].__str__(), row[4].__str__(),
                       row[6].__str__(), 'Out For Delivery')
            d[row[0]] = [row[1], row[5], row[2], row[4], row[6]]
    print(f'Processed {line_count} lines.')

print(ht1.search('40'))

for key in d:
    print('Package ID', key, 'corresponds to', d[key])

'''
creates an empty dictionary
'''

dist = {}

'''
converts the WGUPS_Distance_Table.csv into a python list
'''

with open('WGUPS_Distance_Table.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0: 
            line_count += 1
        else:
            line_count += 1
            dist[row[0]] = [row[2:29]]
    print(f'Processed {line_count} lines.')

print(dist)

'''
newList used to format distance data into an ordered list
'''

newlist = []

'''
populates newlist
'''

for key in dist:
    print('\nAddress for', key, 'corresponding distances are', dist[key])
    newlist.append(dist[key])

'''
Finds the shortest distance from the called address id to the next closest id

///NOT CURRENTLY NEEDED
'''


def findShortest():
    for i in newlist:
        smallest = 100
        j = range(27)

        for n in j:
            if i[0][n] != '' and float(i[0][n]) < 2:
                smallest = float(i[0][n])
                print('\n', smallest, 'is smaller than 2')


'''
test findShortest function...
'''

# findShortest()

'''
assigns address keys from dist to list distList
'''

distList = []

for key in dist:
    distList.append(key)

print('\ndist list: ', distList[0])


'''
returns the specified address from distList
'''


def findDistAddress(input):
    return distList[input]


'''
Find shortest of specified row
'''

distSum = 0 #Initial sum of total shortest distance


def findClosest(row):
    smallest = 100
    global distSum
    listCounter = 0
    positive = False #check to make sure the 0.0 dist location is not pertaining to itself

    def closest():
        print('\nClosest neighbor distance for:\n', findDistAddress( row ) )
        print('\nIndex in the distance list:', listCounter, '\n')
        print('Closest address:')
        print(distList[listCounter])

    for i in newlist[row][0]:
        j = range(27)
        if i == '':
            break
        if i == '0.0' and not positive:
            smallest = i
            closest()
        elif i != '' and i != '0.0' and float(i) < float(smallest):
            smallest = i
            closest()
            positive = True
        listCounter += 1
    print('\nWith a distance of only', smallest, 'miles')
    distSum += float(smallest)
    print('Total distance thus far:', distSum, 'miles')

'''
call findShortestInRow
'''

findClosest(14)

'''
compare starting index to 
'''

'''
- prints each key from the distance csv
- names and addresses
'''

print('\nkeys are as follows:\n', dist.keys())

'''
calls the distance at the specified index from the list newlist
'''

#print(newlist[26][0][0])

'''
loops through a list of addresses and adds the miles together of nearest neighbors
'''

index = 0

for i in newlist:
    findClosest( index )
    index += 1


'''
List of packages on truck 1
'''

manifestTruck1 = [0,1,2,3,4,5]

'''
Loops through the list of packages and their corresponding distances from each other
'''
for i in manifestTruck1:
    for j in manifestTruck1:
        def aToB():
            if newlist[i][0][j] != '':
                return newlist[i][0][j]
            else:
                return newlist[j][0][i] #returns the inverse if null
        print('Distance from stop', i, 'to stop', str(j) + ':', aToB())
