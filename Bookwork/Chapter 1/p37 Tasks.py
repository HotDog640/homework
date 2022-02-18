# Pg 37
# Q1
"""
for i in range(1, 11):
    print(i)

i = 1
while i < 11:
    print(i)
    i += 1
"""

# Q2
"""
end = int(input("Enter the end number: "))
for i in range(1, end):
    if i % 2 == 1: # If odd
        print(i)
"""

# Q3
"""
sentence = input("Enter a sentence: ")

total = 0
for l in sentence:
    if l == "a" or l == "e" or l == "i" or l == "o" or l == "u":
        total += 1
        
print(total)
"""

# Q4
"""
sentence = input("Enter a sentence: ")

reverse = ""

for letter in sentence:
    reverse = letter + reverse
print(reverse)
"""

# Q5
sentence = input("Enter a sentence: ")
searchChar = input("Enter a character to search for: ")

occurences = 0
for letter in sentence:
    if letter == searchChar:
        occurences += 1
        
print(occurences)
