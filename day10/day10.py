'''
qaq
'''
# noop does nothing and takes 1 loop to complete

def converter(instructions_strings):
    '''Write a function that can turn day10.txt into a converted_actions of integers'''
    instructions = []
    for instruction in instructions_strings:
        if instruction[0:4] == 'addx':
            instructions.append(0)
            instructions.append(int(instruction[5:8]))
        else:
            instructions.append(0)
    return instructions

def signal_strengths_calculator(position,converted_instructions):
    '''Write a function that can calculate signal strengths at any position'''
    strength = 1
    for j in range(position-1):
        strength = strength + converted_instructions[j]
    signal_strength = strength * position
    return signal_strength


# Open the file and load it into the code
actions = []
with open('day10.txt', 'r', encoding='utf-8') as file:
    actions = file.readlines()
converted_actions = converter(actions)

# Task 1
strength_sum = 0
for k in range(6):
    strength_sum += signal_strengths_calculator((40*k + 20),converted_actions)
print(strength_sum)


# Task 2
images = []
def signal_calculator(position,file):
    '''Write a function that only return the register X'''
    register = 1
    if position>=2:
        for j in range(position-1):
            register += file[j]
    return register

for k in range(240):
    if k % 40 == (signal_calculator(k+1,converted_actions) - 1) or k == signal_calculator(k+1,converted_actions) or k == (signal_calculator(k+1,converted_actions) + 1):
        images.append('#')
    else:
        images.append('.')

for i,j in enumerate(images):
    print(j,end='')
    if i % 40 == 39:
        print(' ')

def parse_input(filename: str):
    '''Read all lines from the file and return a list of strings'''    
    return []


def task1(input_lines):
    
    '''solve task 1'''

    
    return 'string'

def task2(input_lines):
    '''solve task 2'''

    return 'string'




if __name__ == '__main__':
    day10_test_input = parse_input('Day10_test.txt')
    day10_input = parse_input('Day10.txt')
    assert task1(day10_test_input) == ''
    assert task2(day10_test_input) == ''
    print(task1(day10_input))
    print(task2(day10_input))
