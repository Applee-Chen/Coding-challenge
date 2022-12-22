

def parse_input(filename):
    '''Read the data file into a list of movements'''
    movements = []
    with open(filename, 'r', encoding='utf-8') as file:
        movements = file.readlines()
    return movements

def head_movement(movements_file, grid):
    '''Instruct how the head will move according to the file'''





if __name__ == '__main__':
    # day9_test_input = parse_input('day9_test.txt')
    # day9_input = parse_input('day9.txt')
    # print(task1(day9_test_input))
    # assert task1(day9_test_input) == 13140
    # assert task2(day9_test_input) == ''
    # print(task1(day9_input))


