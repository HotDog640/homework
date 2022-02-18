# Page 18 Q1
'''
age = input("How old are you? ")
print(str(age) + ", What a great age!")
'''

# Q2
'''
num1 = 1.9
num2 = 2.5

print(num1 + num2)
print(num1 - num2)
print(num1 ** num2)
'''

# Q3
'''
num1 = 43.2
num2 = 2.72

print((num1 + num2) / 2) # Average
print(num1 % num2) # Remainder
print(num1 ** num2) # Power
'''

# Q4
'''
inputTemp = input("Temperature in Freedom Units: ")
fTemp = int(inputTemp)
cTemp = (5 / 9) * (fTemp - 32)
print(str(round(cTemp)) + "°C")
'''

# Q5
'''
miToSingapore = 8638
kmToSingapore = miToSingapore * 1.60935
costToFlyToSingapore = kmToSingapore * 900
print("The cost to fly to Singapore is: €" + str(costToFlyToSingapore) + ".")
'''

# Q6
'''
cylH = 20 # Height
cylR = 15 # Width
cylV = 3.14 * (cylR ** 2) * cylH # Calculate volume
totalLiquid = 100000
print(totalLiquid / cylV)
'''

# Q7
'''
inputWeight = int(input("How much do you weigh? "))
moonWeight = inputWeight / 100 * 16.5
print(str(moonWeight) + " is your weight on the moon.")
'''

# Q8
'''
gardenL = int(input("What is the length of the garden? "))
gardenW = int(input("What is the width of the garden? "))
gardenA = gardenL * gardenW
houseL = int(input("What is the length of your house? "))
houseW = int(input("What is the width of your house? "))
houseA = houseL * houseW
trueGardenA = gardenA - houseA
timeToTakeS = trueGardenA / 2
timeToTakeM = timeToTakeS / 60
print("It will take " + str(timeToTakeM) + " minutes to cut the grass")
'''