def parse_input(filename):
    '''Read the data file into a list of movements'''
    movements = []
    with open(filename, 'r', encoding='utf-8') as file:
        movements = file.readlines()
    return movements

def head_movements(instructions, head_coordinate):
    '''Instruct how the head will move according to the file'''
    '''Instructions here should be only in one go: R,L,U,D'''
    '''Coordinates are lists, [2,3] means it's in the 3rd row and 4th column of the grid'''
    right = [1,0]
    left = [-1,0]
    up = [0,1]
    down = [0,-1]
    if instructions == 'R':
        head_coordinate[0] = head_coordinate[0] + right[0]
        head_coordinate[1] = head_coordinate[1] + right[1]
    elif instructions == 'L':
        head_coordinate[0] = head_coordinate[0] + left[0]
        head_coordinate[1] = head_coordinate[1] + left[1]
    elif instructions == 'U':
        head_coordinate[0] = head_coordinate[0] + up[0]
        head_coordinate[1] = head_coordinate[1] + up[1]
    elif instructions == 'D':
        head_coordinate[0] = head_coordinate[0] + down[0]
        head_coordinate[1] = head_coordinate[1] + down[1]
    return head_coordinate

def tail_movements(head_coordinate, tail_coordinate):
    '''Instruct how the tail should move considering current position of head'''
    head_horizontal = head_coordinate[1]
    tail_horizontal = tail_coordinate[1]
    head_vertical = head_coordinate[0]
    tail_vertical = tail_coordinate[0]
    if head_horizontal - tail_horizontal == 2:
        tail_horizontal = head_horizontal - 1
        tail_vertical = head_vertical
    elif tail_horizontal - head_horizontal == 2:
        tail_horizontal = head_horizontal + 1
        tail_vertical = head_vertical
    elif head_vertical - tail_vertical == 2:
        tail_vertical = head_vertical - 1
        tail_horizontal = head_horizontal
    elif tail_vertical - head_vertical == 2:
        tail_vertical = head_vertical + 1
        tail_horizontal = head_horizontal
    tail_coordinate[0] = tail_vertical
    tail_coordinate[1] = tail_horizontal
    return tail_coordinate

def task1(inputs):
    '''Finish task 1'''
    head = [4,0]
    tail = [4,0]
    trace_of_tail = []
    for movements in inputs:
        frequency = int(movements[2])
        instruction = movements[0]
        for i in range(frequency):
            head = head_movements(instruction, head)
            tail = tail_movements(head, tail)
            




if __name__ == '__main__':
    # day9_test_input = parse_input('day9_test.txt')
    # day9_input = parse_input('day9.txt')
    # print(task1(day9_test_input))
    # assert task1(day9_test_input) == 13140
    # assert task2(day9_test_input) == ''
    # print(task1(day9_input))
    # grid = parse_grid('grid.txt')


