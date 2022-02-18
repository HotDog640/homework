# Task 1
"""
fave_artist = input("What is your favourite artist? ")
output_string = fave_artist + " is brilliant."
print(output_string)
"""

# Task 2
"""
fullName = input("What's your full name? ")
spaceIdx = fullName.index(" ")
fName = fullName[:spaceIdx]
sName = fullName[spaceIdx + 1:]
print(fName)
print(sName)
"""

# Task 3
"""
hours = int(input("How many hours? "))
mins = int(input("How many minutes? "))
secs = int(input("How many seconds? "))

totalSecs = 0
totalSecs += hours * 60 * 60
totalSecs += mins * 60
totalSecs += secs

print(str(totalSecs) + " seconds total.")
"""

# Task 4
"""
secs = int(input("Enter a 5 digit number of seconds: "))
mins = round(secs / 60)
print("This is aprox. " + str(mins) + " minutes.")
"""

# Task 5
"""
output = ""

for i in range(5):
    letter = input(f"Enter 1 letter ({i + 1} of 5): ")
    output += f"{letter}: {ord(letter)}\n"

print(output)
"""

# Task 6
"""
amountOfUnits = int(input("How many units of electricity have you used this month? "))
total = 26.20 + (amountOfUnits * .19)
print(f"€{total} due ")
"""

# Task 7
"""
total = 0
fishCount = int(input("How much fish would you like to order? "))
total += fishCount * 4.50
chipCount = int(input("How many chips would you like to order? "))
total += chipCount * 2.80

print(f"Total: {total}")
totalPlusVAT = total + ((total / 100) * 9)
print(f"Total + VAT: {totalPlusVAT}")
"""

# Task 8
word = input("Input the word to be ciphered: ")
key = int(input("Caesar key: "))

newWord = ""
for letter in word:
    newAscii = ord(letter) + key
    if newAscii > 122:
        newAscii = newAscii % 122 + 96
    newWord += chr(newAscii)

print(newWord)