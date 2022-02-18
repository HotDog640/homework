# Pg 42, 43
# Q1
"""
numList = []

for i in range(5):
    num = int(input(f"Input a number ({i + 1} of 5): "))
    numList.append(num)

for i in range(len(numList)):
    numList[i] = numList[i] + 1

print(numList)
"""

# Q2
"""
hours = []

for i in range(7):
    hour = int(input(f"Input the amount of hours spent in day {i + 1}: "))
    hours.append(hour)

totalHours = 0
for hour in hours:
    totalHours += hour

milkDrank = totalHours / 2
print(f"The total amount of milk drank throughout the week is {milkDrank}l.")

cost = milkDrank * 1.35
print(f"The cost of this milk is €{round(cost * 100)/100}") # Round to 2 decimal places
"""

# Q3
"""
rainfall = []

for i in range(7):
    rain = float(input(f"Input the amount of rain collected today {i + 1}: "))
    rainfall.append(rain)
    
print("") # Newline for formatting

totalRainfall = sum(rainfall)
averageRainfall = totalRainfall / 7
print(f"Total Rainfall: {totalRainfall}")
print(f"Average Rainfall: {averageRainfall}")

for i in range(7):
    if rainfall[i] > 3.5:
        print(f"There was {rainfall[i]}cm of rainfall on day {i + 1}, exceding 3.5cm")
"""

# Q4
salesPersonCount = int(input("How many salespeople are there? "))
print("----------")

saleNames = []
saleValues = []

for i in range(salesPersonCount):
    saleNames.append(input(f"Input name of salesperson ({i + 1} of {salesPersonCount}): "))
    saleValues.append(float(input(f"Input their sales value in euro ({i + 1} of {salesPersonCount}): ")))

print("----------")

for i in range(salesPersonCount):
    print(f"{saleNames[i]} has €{saleValues[i]} worth of sales.")

print("")
print(f"Highest sales count: {max(saleValues)}")
print(f"Lowest sales count: {min(saleValues)}")
print(f"Average sales: {sum(saleValues)/salesPersonCount}")
print("----------")
