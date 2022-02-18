# Pg 77 Tasks

# Q1
"""
file = open("name.txt", "w")
file.write(input("What is your name? "))
file.close()
"""

# Q3
"""
password = open("password.txt", "r").read()
inputpwd = input("Please enter the password: ")
print("Correct." if inputpwd == password else "Incorrect.")
"""

# Q4
"""
file = open("values.csv", "w")
values = []
print("Please enter 10 numbers")
for i in range(10):
    values.append(input(f"{i+1}: "))
file.write(",".join(values))
file.close()
"""

# Q5
"""
file = open("values.csv").read()
values = file.split(",")
values = [float(i) for i in values]
print(values)
"""

# Q6
"""
peopleFile = open("salespeople.csv", "r+")
salesFile = open("sales.csv", "r+")

salespeople = peopleFile.read().split(",")
sales = []

for sale in salesFile.read().split(","):
    sale = 0 if sale == "" else sale
    sales.append(int(sale))

i = 1
while True:
    theirName = input(f"Enter Salesperson {i}: ")
    if theirName == "": break # Exit the loop if no name is entered
    salespeople.append(theirName)
    theirSales = input(f"Enter their sales: ")
    sales.append(int(theirSales) if theirSales != "" else 0)
    i = i + 1

peopleFile.write(",".join(salespeople)[1:])
salesFile.write(",".join([str(sale) for sale in sales])[2:])

print("-------------------------")
print("| Salesperson\t| sales\t|")
print("-------------------------")
for i in range(len(salespeople) - 1):
    print(f"| {salespeople[i+1]}\t| {sales[i+1]}\t|")
print("-------------------------")

print(f"\nTotal sales: {sum(sales)}")

peopleFile.close()
salesFile.close()
"""
