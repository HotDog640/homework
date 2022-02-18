# Q1
"""
list = [1, -2, 3, -4, 5, -6, 7, -8]

print(list)

for item in list:
    if item < 0:
        list.remove(item)
    
print(list)
"""

# Q2
"""
list = [17, -5, 4, 20, 15, 6, 5, -18, -17, 5, 1, 1, -11, 6, 12, 18, -11, 0, -3, 1]

# Sort tehe list in descending order
list.sort(reverse = True)
print(list)

# Save it as a csv file
stringList = [str(item) for item in list]
file = open("list.csv", "w")
file.write(",".join(stringList))
file.close()

# Find the min and max
minimum = None
maximum = None

for elem in list:
    # Set the min and max if they're not already set
    if minimum == None:
        minimum = maximum = elem
    
    # Set the minimum and maximum
    if elem < minimum:
        minimum = elem
    if elem > maximum:
        maximum = elem
        
print("max: ", maximum)
print("min: ", minimum)
"""

# Q3
"""
# Generate the random numbers
import random
list = [random.randint(0, 100) for i in range(100)]

# Save them in a csv 
stringList = [str(item) for item in list]
file = open("list.csv", "w")
file.write(",".join(stringList))
file.close()
"""

# Q4

file = open("list.csv", "r")



