# Q1
"""
age = int(input("What is your age? "))
score = int(input("What is your test score? "))

if score >= 80 and age <= 16:
    print("Excellent")
elif score >= 80 and age > 16:
    print("Good")
else:
    print("Please try harder next time!")
"""

# Q2
"""
bags = int(input("How many bags have been purchased? "))
goldInput = input("Are you a gold customer (y/n)? ")
isGold = goldInput == "y"

discount = 0
if bags >= 100:
    discount = 10
elif bags >= 25:
    discount = 5
if isGold:
    discount += 3.5
    
percentageOfCost = 100 - discount
total = (((bags * 2.23) / 100) * percentageOfCost)

print(f"Your total is €{total:.2f}")
"""

# Q3
"""
from datetime import date
birthMonth = int(input("What is your month of birth (in number form)? "))
currentMonth = date.today().month

monthsUntil = (12 - (currentMonth - birthMonth)) % 12

print(f"We are {monthsUntil} months away from your birthday!")
"""

# Q4

'''
isWeekend = input("Is it the Weekend? (Saturday or Sunday) (y/n)? ") == "y"
cc = int(input("What cc is the moped (enter as a number)? "))
hours = int(input("How many hours will you be renting for? "))

init = None
hourly = None

if isWeekend and cc == 50:
    init = 30
    hourly = 3
elif isWeekend and cc == 250:
    init = 35
    hourly = 5
elif cc == 50:
    init = 15
    hourly = 2.50
elif cc == 250:
    init = 25
    hourly = 3.50
else:
    raise Exception("Invalid Moped Type Exception")
    
realHours = hours - 3 # Hours after the first 3 covered by the init cost
if realHours >= 0: # If positive
    cost = init + (realHours * hourly)
else:
    cost = init

print(f"""
============
Moped Rental
============
Weekend: {isWeekend}
Type: {cc} cc
Total: €{cost}
""")
'''

#Q5
"""
email = input("What is your email? ")
atSplit = email.split("@")

if (len(atSplit) != 2) or ("." not in atSplit[1]) or (len(email) < 8):
    print("Invalid email")
else:
    print("Valid email")
"""

# Q6
"""
isHigher = input("Are you doing higher level (y/n)? ") == "y"
marks = int(input("What percentage did you get? "))

grade = None

if marks < 30:
    grade = 8
elif marks < 40:
    grade = 7
elif marks < 50:
    grade = 6
elif marks < 60:
    grade = 5
elif marks < 70:
    grade = 4
elif marks < 80:
    grade = 3
elif marks < 90:
    grade = 2
else:
    grade = 1
    
print(f"Your grade is {'H' if isHigher else 'O'}{grade}")
"""

# Q7
stickLens = []

for i in range(3):
    stickLens.append(int(input(f"Enter a stick length ({i+1} of 3): ")))

hyp = max(stickLens)
stickLens.remove(hyp)

if (stickLens[0]**2 + stickLens[1]**2 == hyp**2):
    print("You have a right angle triangle!")
else:
    print("You don't have a right angle triangle")
