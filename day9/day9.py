def parse_grid(filename):
    '''Read the data file into a list of movements'''
    grid = []
    with open(filename, 'r', encoding='utf-8') as file:
        grid = file.readlines()
    return grid

def parse_input(filename):
    '''Read the data file into a list of movements'''
    movements = []
    with open(filename, 'r', encoding='utf-8') as file:
        movements = file.readlines()
    return movements

def head_movements(instructions, grid):
    '''Instruct how the head will move according to the file'''
    '''Instructions here should be only in one go: R,L,U,D'''
    right = [1,0]
    left = [-1,0]
    up = [0,1]
    down = [0,-1]





if __name__ == '__main__':
    # day9_test_input = parse_input('day9_test.txt')
    # day9_input = parse_input('day9.txt')
    # print(task1(day9_test_input))
    # assert task1(day9_test_input) == 13140
    # assert task2(day9_test_input) == ''
    # print(task1(day9_input))
    # grid = parse_grid('grid.txt')


