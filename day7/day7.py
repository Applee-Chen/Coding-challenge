class File:
    '''Represent a file'''
    def __init__(self, name, size):
        self.name = name
        self.size = size

class Directory:
    '''Represent a directory'''
    def __init__(self, name, files, directories):
        self.name = name
        self.files = files
        self.directories = directories

'''Parse input and load the data into both tasks'''
def parse_input(filename):
    commands = []
    with open(filename, 'r', encoding='utf-8') as file:
        commands = file.readlines()
    return commands

def summarise_directories(command_file):
    '''identify all directories and write them into a list with their positions'''
    list_of_directories = []
    size_of_file = len(command_file)
    for rows in range(size_of_file):
        if (command_file[rows].split(' '))[0] == 'dir':
            directory = []
            directory_name = ((command_file[rows].split(' '))[1])
            directory.append(directory_name)
            directory.append(rows)
            list_of_directories.append(directory)
    return(list_of_directories)

def search_directory(command_file, start_position, name):
    '''locate where the directory starts listing its elements'''
    size_of_commands = int(len(command_file))
    for elements in range(size_of_commands):
        if (command_file[start_position+elements].split(' '))[1] == 'cd' and (command_file[start_position+elements].split(' '))[2] == name:
            return (start_position+elements+2)

def size_of_directories(command_file, start_position, name):
    '''Obtain size of a directory'''
    size = 0
    size_of_commands = int(len(command_file))
    position = search_directory(command_file, start_position, name)
    # If the element is a file, add the sizes directly
    # If the element is a directory, use recursion 
    for elements in range(size_of_commands):
        if int(len(command_file[position+elements].split(' '))) != 2:
            return size
        elif command_file[position+elements].split(' ')[0] != 'dir':
            size = size + int((command_file[position+elements].split(' '))[0])
        else:
            moderated_name = (command_file[position+elements].split(' ')[1])
            size = size + size_of_directories(command_file, (position+elements), moderated_name)

def task1(command_file):
    '''finish task 1'''
    sum_of_required_directories = 0
    list_of_directories = summarise_directories(command_file)
    size_of_file = int(len(list_of_directories))
    for directory in range(size_of_file):
        if size_of_directories(command_file, list_of_directories[directory][1],list_of_directories[directory][0]) <= 100000:
            sum_of_required_directories += size_of_directories(command_file, list_of_directories[directory][1],list_of_directories[directory][0])
    return sum_of_required_directories

def setup_filesystem(lines):
    '''
    Setup the file system based on the command-line input.
    Return the root directory.
    '''
    root = Directory('root', [], [])
    current_directory: Directory = root
    for line in lines:
        if line.startWith("$ "):
            cmd = line.removeFront("$ ")
            if cmd.startWith("cd"):
                pass # cd
            else:
                pass # ls
            # cd xxxx
            # ls
        # $ cd xxxx
        # $ ls
        # file_name
        # directory_name
            

    return root

def calc_directory_size(directory: Directory) -> int:
    '''
    Calculate the size of a directory
    '''
    files_size = 0
    directory_size = 0
    for file in directory.files:
        files_size += file.size
    for dire in directory.directories:
        directory_size += calc_directory_size(dire)
    return files_size + directory_size

def task1_pcloud(input_lines):
    root_directory = setup_filesystem(input_lines)
    size_threshold = 100_000
    size_sum = 0
    queue = []
    queue.append(root_directory)
    while len(queue) > 0:
        directory = queue[0]
        queue.pop(0)
        dir_size = calc_directory_size(directory)
        if dir_size <= size_threshold:
            size_sum += dir_size
        queue += directory.directories
    return size_sum

if __name__ == '__main__':
    sheep_photo = File('main main', 1000)
    shark_photo = File('sha sha', 100000)
    sub_directory = Directory('secret photos', [shark_photo], [])
    home_directory = Directory('home', [sheep_photo], [sub_directory])
    print(calc_directory_size(home_directory))
    # home_directory, -> sub_dir_1
    #                 -> sub_dir_2 -> sub_sub_dir_1

    # day7_test_input = parse_input('test1.txt')
    # day7_input = parse_input('day7.txt')
    # print(task1(day7_test_input))
    # # assert task1(day7_test_input) == 13140
    # # assert task2(day7_test_input) == ''
    # print(task1(day7_input))


