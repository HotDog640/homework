# p84 Tasks
# Q1
"""
ages = [32, 31, 30, 37, 37, 33]
earnings = [1270, 7980, 4700, 1810, 750, 1100]

minAge = min(ages)
maxAge = max(ages)
minEarning = min(earnings)
maxEarning = max(earnings)

print(f"minAge: {minAge}")
print(f"maxAge: {maxAge}")
print(f"minEarning: {minEarning}")
print(f"maxEarning: {maxEarning}")
"""

# Q2
"""
from statistics import mean, median, mode
list = [1, 9, 3, 2, 3, 7, 6, 5, 8, 9, 1, 10]
minE = min(list)
maxE = max(list)
meanE = mean(list)
medianE = median(list)

# frequency
items = []
frequencies = []

for item in list:
    if item not in items:
        items.append(item)
for item in items:
    total = list.count(item)
    frequencies.append(total)
    
# mode
mostOccurences = max(frequencies)
index = frequencies.index(mostOccurences)
mode = items[index]

    
print(
    f"min: {minE}\n" +
    f"max: {maxE}\n" +
    f"mean: {meanE}\n" +
    f"median: {medianE}\n" +
    f"mode: {mode}\n" +
    "\n" +
    f"frequency:\n" +
    f"{items}\n" +
    f"{frequencies}"
)
"""

# Q3
# lottery.ie is blocked

# Q4
from statistics import mode
federalist = open("hamilton-federalist-548.txt", "r").read()
words = federalist.split()

wordlist = []
frequency = []

for word in words:
    if word not in wordlist:
        wordlist.append(word)
for word in wordlist:
    total = words.count(word)
    frequency.append(total)

print(wordlist)
print(frequency)





