# p213 Tasks and Questions
"""
1. The key
2. It goes from the start to the end (or vice versa) of an array, and returns
    the index of the key.
3. The binary search requires the list to be sorted first.
4. half-interval search.
5. The binary search starts in the middle, then halves the array each time
    until it finds the key.
6. The start position of the sub-list, the end position of the sub-list.
7. The halfway index of the list.
"""

# Tasks
# Q1
"""
def linear_search(listIn, key):
    index = 0
    for element in listIn:
        if element == key:
            return index
        index += 1
    return -1

myList = [19, 87, 1, -1, 11, 0, -1, 33, 19]
print(binary_search(myList, -1))
print(binary_search(myList, 33))
"""

# Q2
"""
def binary_search(listIn, key):
    first = 0
    last = len(listIn) - 1
    while (last - first >= 0):
        index = first + ((last - first) // 2)
        if listIn[index] == key:
            return index
        elif listIn[index] < key:
            first = index + 1
        else:
            last = index - 1

    return -1

myList = [19, 87, 1, -1, 11, 0, -1, 33, 19]
myList.sort()
print(binary_search(myList, -1))
print(binary_search(myList, 33))
"""

# Q3
"""
Linear search goes from the start to the end (or vice versa) of an array, and
returns the index of the key. The binary search starts in the middle, then
halves the array each time until it finds the key, then returns it's index.
Linear can be used on unsorted arrays, whereas binary requires a sorted array.
Linear is slower on average, however, wheas binary search is on average much
faster.
"""

# Q4

def linear_search(listIn, key):
    index = 0
    for element in listIn:
        if element == key:
            return index
        index += 1
    return -1

def binary_search(listIn, key):
    first = 0
    last = len(listIn) - 1
    while (last - first >= 0):
        index = first + ((last - first) // 2)
        if listIn[index] == key:
            return index
        elif listIn[index] < key:
            first = index + 1
        else:
            last = index - 1

    return -1

myList = [19, 87, 1, -1, 11, 0, -1, 33, 19]
# Linear
print(linear_search(myList, -1))
print(linear_search(myList, 33))
print(linear_search(myList, 117))
# Binary
myList.sort()
print(binary_search(myList, -1))
print(binary_search(myList, 33))
print(binary_search(myList, 117))
