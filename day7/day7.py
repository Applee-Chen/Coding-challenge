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

def setup_filesystem(lines):
    '''
    Setup the file system based on the command-line input.
    Return the root directory.
    '''
    root = Directory('root', [], [])
    current_directories = [root]
    for line in lines:
        if (line.split(' '))[1] == 'cd':
            if (line.split(' '))[2] != '/\n':
                name = (line.split(' '))[2][:-1]
                position = 

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


