def parse_input(filename):
    '''Read the data file into a list of movements'''
    movements = []
    with open(filename, 'r', encoding='utf-8') as file:
        movements = file.readlines()
    return movements

def head_movements(instructions, head_coordinate):
    '''Instruct how the head will move according to the file;
       Instructions should be a single input: R/L/U/D;
       Coordinate [x,y] means that head is in the (x+1)th row and (y+1)th column'''
    right = [0,1]
    left = [0,-1]
    up = [1,0]
    down = [-1,0]
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
    '''Instruct how the tail should move considering current position of head
       Tail only mnoves when the head is any direction 2 steps away from it'''
    head_row = head_coordinate[0]
    head_column = head_coordinate[1]
    tail_row = tail_coordinate[0]
    tail_column = tail_coordinate[1]
    if tail_row - head_row == 2:
        tail_row += -1
        tail_column = head_column
    elif head_row - tail_row == 2:
        tail_row += 1
        tail_column = head_column
    elif tail_column - head_column == 2:
        tail_row = head_row
        tail_column += -1
    elif head_column - tail_column == 2:
        tail_row = head_row
        tail_column += 1
    tail_coordinate[0] = tail_row
    tail_coordinate[1] = tail_column
    return tail_coordinate

def task1(inputs):
    '''Finish task 1
       Return the number of positions that tail has been to'''
    head = [0,0]
    tail = [0,0]
    list_of_positions = []
    list_of_positions.append([0,0])
    for line in inputs:
        instruction = line[0]
        frequency = int(line[2])
        counter = 0
        while counter < frequency:
            head = head_movements(instruction, head)
            tail = tail_movements(head, tail)
            if tail not in list_of_positions:
                list_of_positions.append(tail)
    return list_of_positions
    


if __name__ == '__main__':
    day9_test_input = parse_input('day9_test.txt')
    day9_input = parse_input('day9.txt')
    print(task1(day9_test_input))
    # assert task1(day9_test_input) == 13140
    # assert task2(day9_test_input) == ''
    # print(task1(day9_input))
    # grid = parse_grid('grid.txt')




