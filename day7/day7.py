'''Parse input and load the data into both tasks'''
commands = []
with open('test1.txt', 'r', encoding='utf-8') as file:
    commands = file.readlines()

def size_of_directories(command_file,name_of_directory):
    '''Obtain size of a directory'''
    count = 0
    size_of_commands = int(len(command_file))
    for rows in range(size_of_commands):
        if command_file[rows].split(' ')[1] == 'cd':
            a = '\n'
            converted_name_of_directory = name_of_directory+a
            if command_file[rows].split(' ')[2] == converted_name_of_directory:
                '''Loop through the files or firectories in our desired directory'''
                for subsidiaries in range(size_of_commands):
                    if int(len(command_file[rows+subsidiaries+2].split(' '))) == 2:
                        if command_file[rows+subsidiaries+2].split(' ')[0] != 'dir':
                            count = count + int((command_file[rows+subsidiaries+2].split(' '))[0])
                        else:
                            moderated_name = (command_file[rows+subsidiaries+2].split(' ')[1])[:-1]
                            count = count + size_of_directories(command_file,moderated_name)
                    else:
                        return count

print(size_of_directories(commands,'/'))

def task1(command_file):
    

