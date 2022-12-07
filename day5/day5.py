# Write the state of 9 stacks into 9 lists 
Stack = []
Stack_1 = ['S','Z','P','D','L','B','F','C']
Stack_2 = ['N','V','G','P','H','W','B']
Stack_3 = ['F','W','B','J','G']
Stack_4 = ['G','J','N','F','L','W','C','S']
Stack_5 = ['W','J','L','T','P','M','S','H']
Stack_6 = ['B','C','W','G','F','S']
Stack_7 = ['H','T','P','M','Q','B','W']
Stack_8 = ['F','S','W','T']
Stack_9 = ['N','C','R']
Stack.append(Stack_1)
Stack.append(Stack_2)
Stack.append(Stack_3)
Stack.append(Stack_4)
Stack.append(Stack_5)
Stack.append(Stack_6)
Stack.append(Stack_7)
Stack.append(Stack_8)
Stack.append(Stack_9)

# Write a function that can turn instructions into a list
def converter(s):
    instructions = []
    if s[6] == ' ':
        number_of_items = int(s[5])
        starting_stack = int(s[12])
        ending_stack = int(s[17])
    else:
        number_of_items = int(s[5:7])
        starting_stack = int(s[13])
        ending_stack = int(s[18])
    
    instructions.append(number_of_items)
    instructions.append(starting_stack)
    instructions.append(ending_stack)

    return(instructions)

# Write a function that rearrange those items on stack
def rearrange(a,b):
    for i in range(b[0]):
        last_item = a[b[1] - 1][int(len(a[b[1] - 1])) - 1]
        a[b[1] - 1].pop()
        a[b[2] - 1].append(last_item)
    
    return(a)
    
Instructions = []
with open('day5.txt', 'r', encoding='utf-8') as file:
    Instructions = file.readlines()

# Task 1
for r in Instructions:
    Stack = rearrange(Stack,converter(r))
print(Stack)