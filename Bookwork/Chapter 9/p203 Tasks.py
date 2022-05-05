# p203 Tasks

# Q1
"""
def getPi():
    return 22/7

print(getPi())
"""

# Q2
"""
def divide(x, y):
    return x/y

print(divide(6, 3))
"""

# Q3
"""
def spaceCount(string):
    return string.count(" ")

print(spaceCount("The FitnessGram™ Pacer Test is a multistage aerobic capacity test that progressively gets more difficult as it continues."))
"""

# Q4
"""
def dividesEvenly(x, y):
    return x % y == 0

print(dividesEvenly(64, 8))
"""

# Q5
"""
def occurs(theList, value):
    return theList.count(value)

print(occurs([1, 2, 4, 2, 2, 2], 2))
"""

# Q6
"""
def getSalesPrice(RRP, discount):
    return RRP - ((discount / 100) * RRP)

for i in range(6):
    RRP = int(input("Enter the reccomended retail price: "))
    discount = int(input("Enter the percentage discount as a whole number: "))
    salesPrice = getSalesPrice(RRP, discount)
    print("Retail\t% Off\tSales Price")
    print(f"{RRP}\t{discount}\t{salesPrice}")
"""

# Q7
"""
def convertTempFrom(temp, scale):
    if scale == "C":
        return (temp * 1.8) + 32
    elif scale == "F":
        return (temp - 32) / 1.8

temps = [50, 102, 37, 20]
scales = ["C", "F", "C", "F"]
for temp, scale in zip(temps, scales):
    otherTemp = convertTempFrom(temp, scale)
    otherScale = "F" if scale == "C" else "C"
    print(f"{temp}°{scale} = {otherTemp:.2f}°{otherScale}")
"""

# Q8
"""
# returns float of the price in euro
def getTheCostOfPetFoodForThreeWeeks(petType, gramsPerDay):
    foodPrice = None
    if petType == "cat":
        foodPrice = 5
    elif petType == "hamster":
        foodPrice = 3
        
    kilosPerDay = gramsPerDay/1000
    
    return (foodPrice * 21 * kilosPerDay)

petType = input("What type of pet do you have? ")
gramsPerDay = int(input("How much grams of food do they eat a day? "))

costOfPetFoodForThreeWeeks = getTheCostOfPetFoodForThreeWeeks(petType, gramsPerDay)

print(f"The cost of pet food for the next three weeks is: €{costOfPetFoodForThreeWeeks:.2f}")
"""
