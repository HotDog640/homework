# Q1
"""
1) The inner loop prints each column of stars.
2) The print function at the end prints a line break for each row.
3)
**************************************************
**************************************************
**************************************************
**************************************************
**************************************************
**************************************************
**************************************************
**************************************************
**************************************************
**************************************************
"""

# Q2
"""
for timesTable in range(1, 13):
    print(f"\n\nTimes table for {timesTable}:\n")
    for i in range(1, 13):
        print(timesTable, "x", i, "=", timesTable * i)
"""

# Q3
"""
rows = int(input("How many rows do you want? "))
cols = int(input("How many columns do you want? "))

for row in range(rows):
    for col in range(cols):
        print("*", end = "")
    print()
"""

# Q4
"""
rows = int(input("How many rows do you want? "))
for row in range(rows+1):
    for i in range(row):
        print("*", end="")
    print()
"""

# Q5

rows = int(input("How many rows do you want? "))
