# Python program to demonstrate working of HashTable

hashTable = [[]] * 10

def checkPrime(n):
    if n == 1 or n == 0:
        return 0
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return 0
    return 1

def getPrime(n):
    if n % 2 == 0:
        n += 1
    while not checkPrime(n):
        n += 2
    return n

def hashFunction(key):
    capacity = getPrime(10)
    return key % capacity

def insertData(key, data):
    index = hashFunction(key)
    hashTable[index] = [key, data]

def removeData(key):
    index = hashFunction(key)
    hashTable[index] = 0

    
def traverseHashTable():
    print("Hash Table:")
    for i in range(len(hashTable)):
        if hashTable[i]:
            print("Index", i, ":", hashTable[i])
        else:
            print("Index", i, ": Empty")

# Insert data into hash table

insertData(123, "C")
insertData(432, "Python")
insertData(213, "JAVA")
insertData(654, "C++")
print("After inserting:")
print(hashTable,"\n")

# Remove data from hash table
removeData(123)
print("After removing [123,C] :")
print(hashTable,"\n")

#Travesing
print("travesing hash table:")
traverseHashTable()
