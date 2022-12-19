'''
Solution for day 10
'''

def parse_input(filename):
    '''Read the data file into a list of instructions'''
    actions = []
    with open(filename, 'r', encoding='utf-8') as file:
        actions = file.readlines()
    return actions

def converter(instructions_strings):
    '''convert the given instructions strings into a list of instructions'''
    instructions = []
    for instruction in instructions_strings:
        instructions.append(0)
        if instruction[0:4] == 'addx':
            instructions.append(int(instruction[5:8]))
    return instructions

def task1(inputs):
    '''Write a function that can turn day10.txt into a converted_actions of integers'''
    instructions = converter(inputs)
    positions = [20, 60, 100, 140, 180, 220]
    strength = 1
    signal_strength = 0
    for position in positions:
        strength = 1
        for changes in range(position - 1):
            strength += instructions[changes]
        signal_strength += strength * position
    return signal_strength

# # Task 2
# images = []
# def signal_calculator(position,file):
#     '''Write a function that only return the register X'''
#     register = 1
#     if position>=2:
#         for j in range(position-1):
#             register += file[j]
#     return register

# for k in range(240):
#     if k % 40 == (signal_calculator(k+1,converted_actions) - 1) or k == signal_calculator(k+1,converted_actions) or k == (signal_calculator(k+1,converted_actions) + 1):
#         images.append('#')
#     else:
#         images.append('.')

# for i,j in enumerate(images):
#     print(j,end='')
#     if i % 40 == 39:
#         print(' ')

# def task2(input_lines):
#     '''solve task 2'''

#     return 'string'




if __name__ == '__main__':
    day10_test_input = parse_input('Day10_test.txt')
    day10_input = parse_input('Day10.txt')
    print(task1(day10_test_input))
    assert task1(day10_test_input) == 13140
    # assert task2(day10_test_input) == ''
    print(task1(day10_input))
    # print(task2(day10_input))