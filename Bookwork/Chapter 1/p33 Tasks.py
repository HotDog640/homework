# Pg 33-34
# Q1
"""
counter = 1000
total = 0
while counter <= 1500:
    total += counter
    counter += 1

print(total)
"""

# Q2
"""
total = 0
counter = 1

while counter <= 6:
    total += int(input(f"Enter number {counter}: "))
    counter += 1

print(f"Average: {total / 6}")
"""

# Q3
"""
name = input("What is your name? ")
while name != "Maureen":
    name = input("Try again. What is your name? ")

password = input("Enter your password: ")
if (password == "Password1"):
    print("Access granted!")
else:
    print("Access denied!")
"""

# Q4
"""
limit = int(input("Please enter a limit: "))
counter = 1

oddTotal = 0
evenTotal = 0

while counter <= limit:
    if counter % 2 == 0:
        evenTotal += counter
    else:
        oddTotal += counter
    counter += 1

print(f"Even total: {evenTotal}\nOdd total: {oddTotal}")
"""

# Q5
"""
total = 0
number = int(input("Enter a number: "))
count = 0
while number >= 0:
    count += 1
    total += number
    number = int(input("Enter a number: "))

print(f"Average: {0 if count == 0 else total / count}") # To avoid ZeroDivisionError if count is 0
"""

# Q6
"""
string = input("Enter a string: ")
spaceCount = 0

i = 0
while i < len(string):
    if string[i] == " ":
        spaceCount += 1
    i += 1

print(f"Word count: {spaceCount + 1}")
"""

# Q7
selection = input(
"**************************\n\
* Lucy's sewing Business *\n\
**************************\n\
* 1: Curtains            *\n\
* 2: Cushion covers      *\n\
* 3: Quilts              *\n\
**************************\n\
* Q: Quit (exit)         *\n\
**************************\n\
")

while selection.lower() != "q":
    if selection == "1":
        print("We sell curtains!")
    elif selection == "2":
        print("We sell Cushion covers!")
    elif selection == "3":
        print("We sell quilts!")
    else:
        print("Invalid input.")
    selection = input()

print("Quitting...")