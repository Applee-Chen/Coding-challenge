'''Parse input and load the data into both tasks'''
def parse_input(filename):
    commands = []
    with open(filename, 'r', encoding='utf-8') as file:
        commands = file.readlines()
    return commands

def search_directory(command_file, name_of_directory):
    '''Find the position where the desired directory starts listing its elements'''
    size_of_commands = int(len(command_file))
    for rows in range(size_of_commands):
        if command_file[rows].split(' ')[1] == 'cd':
            end_of_string = '\n'
            converted_name_of_directory = name_of_directory + end_of_string
            if command_file[rows].split(' ')[2] == converted_name_of_directory:
                return (rows + 2)

def size_of_directories(command_file, name_of_directory):
    '''Obtain size of a directory'''
    size = 0
    size_of_commands = int(len(command_file))
    start_position = search_directory(command_file, name_of_directory)
    for elements in range(size_of_commands):
        # If the element is a file, add the sizes directly
        # If the element is a directory, use recursion 
        if int(len(command_file[start_position+elements].split(' '))) != 2:
            # When the list of elements in a directory end, the new command will be: $ cd X, which is of length 3
            return size
        else:
            if command_file[start_position+elements].split(' ')[0] != 'dir':
                size = size + int((command_file[start_position+elements].split(' '))[0])
            else:
                moderated_name = (command_file[start_position+elements].split(' ')[1])[:-1]
                size = size + size_of_directories(command_file, moderated_name)

def task1(command_file):
    '''identify all directories and write them into a list'''
    sum_of_required_directories = 0
    list_of_directories = []
    size_of_file = len(command_file)
    for rows in range(size_of_file):
        if (command_file[rows].split(' '))[0] == 'dir':
            directory_name = ((command_file[rows].split(' '))[1])[:-1]
            if directory_name not in list_of_directories:
                list_of_directories.append(directory_name)
    number_of_directories = len(list_of_directories)
    for directory in range(number_of_directories):
        if size_of_directories(command_file,list_of_directories[directory]) <= 100000:
            sum_of_required_directories = sum_of_required_directories + size_of_directories(command_file,list_of_directories[directory])
    return sum_of_required_directories

if __name__ == '__main__':
    day7_test_input = parse_input('test1.txt')
    day7_input = parse_input('day7.txt')
    # print(task1(day7_test_input))
    # assert task1(day7_test_input) == 13140
    # assert task2(day7_test_input) == ''
    # print(task1(day7_input))
    print(search_directory(day7_input, 'zgqjbf'))

