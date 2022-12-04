# Write a function that finds the character in common in two cmpartments
def check_items(s):
    compartment_length = int((len(s) - 1) / 2)
    for i in range(compartment_length):
        for j in range(compartment_length):
            if s[i] == s[compartment_length+j]:
                return(s[i])

# Write a function that calculates priorities for each rucksack
def priority_calculator(r):
    if ord(r) < 97:
        priority = ord(r) - 38
    else:
        priority = ord(r) - 96
    return priority

# Open the data file and load it into our code
items = []
with open('day3.txt', 'r', encoding='utf-8') as file:
    items = file.readlines()

PRIORITY = 0
for r in items:
    PRIORITY = PRIORITY + priority_calculator(check_items(r))
print(PRIORITY)

