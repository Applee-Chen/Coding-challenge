# addx takes 2 loops to complete and only complete adding after the second loop
# noop does nothing and takes 1 loop to complete

# Write a function that can turn day10.txt into a list of integers
def converter(s):
    instructions = []
    for r in s:
        if r[0:4] == 'addx':
            instructions.append(0)
            instructions.append(int(r[5:8]))
        else:
            instructions.append(0)
    return(instructions)

# Write a function that can calculate signal strengths at any position
def signal_strengths_calculator(i,file):
    strength = 1
    for j in range(i-1):
        strength = strength + file[j]
    signal_strength = strength * i
    return(signal_strength)


# Open the file and load it into the code
Actions = []
with open('day10.txt', 'r', encoding='utf-8') as file:
    Actions = file.readlines()
List = converter(Actions)
print(List)
# Task 1
answer1 = signal_strengths_calculator(20,List) + signal_strengths_calculator(60,List) + signal_strengths_calculator(100,List) + signal_strengths_calculator(140,List) + signal_strengths_calculator(180,List) + signal_strengths_calculator(220,List)

# Task 2
Image = []
# Write a function that only return the register X
def signal_calculator(i,file):
    X = 1
    if i>=2:
        for j in range(i-1):
            X = X + file[j]
    return(X)

for k in range(240):
    if k == (signal_calculator(k+1,List) - 1) or k == signal_calculator(k+1,List) or k == (signal_calculator(k+1,List) + 1):
        Image.append('#')
    else:
        Image.append('.')

for i,j in enumerate(Image):
    print(j,end='')
    if i % 40 == 39:
        print('\n')

for b in range(240):
    print(signal_calculator(b+1,List),end=' ')