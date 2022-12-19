'''Parse input and load the data into both tasks'''
def parse_input(filename):
    commands = []
    with open(filename, 'r', encoding='utf-8') as file:
        commands = file.readlines()
    return commands

def size_of_directories(command_file,name_of_directory):
    '''Obtain size of a directory'''
    count = 0
    size_of_commands = int(len(command_file))
    for rows in range(size_of_commands):
        if command_file[rows].split(' ')[1] == 'cd':
            end_of_string = '\n'
            converted_name_of_directory = name_of_directory+end_of_string
            if command_file[rows].split(' ')[2] == converted_name_of_directory:
                for subsidiaries in range(size_of_commands):
                    if int(len(command_file[rows+subsidiaries+2].split(' '))) == 2:
                        if command_file[rows+subsidiaries+2].split(' ')[0] != 'dir':
                            count = count + int((command_file[rows+subsidiaries+2].split(' '))[0])
                        else:
                            moderated_name = (command_file[rows+subsidiaries+2].split(' ')[1])[:-1]
                            count = count + size_of_directories(command_file,moderated_name)
                    else:
                        return count

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

print(task1(commands))
