# Write a function that can identify ids from string
def converter(s):
    IDs = []
    for i in range(int(len(s) - 1)):
        if s[i] == '-':
            break_point = i
            break
    for j in range(int(len(s) - 1)):
        if s[j] == ',':
            separation = j
    
    for k in range(int(len(s) - separation)):
        if s[separation + k] == '-':
            second_break = separation + k
    ID_1 = s[0:break_point]
    ID_2 = s[(break_point + 1):separation]
    ID_3 = s[(separation + 1):second_break]
    ID_4 = s[(second_break + 1):int(len(s))]
    IDs.append(ID_1)
    IDs.append(ID_2)
    IDs.append(ID_3)
    IDs.append(ID_4)
    return(IDs)

# Write a function to check if the range of IDs encorporate each other
def comparison(l):
    if (int(l[0]) <= int(l[2]) and int(l[1]) >= int(l[3])):
        return('True')
    elif (int(l[0]) >= int(l[2]) and int(l[1]) <= int(l[3])):
        return('True')
    else:
        return('False')

# Write a function for extension task
def strict_comparison(m):
    if int(m[0]) <= int(m[2]):
        if int(m[1]) >= int(m[2]):
            return('True')
    elif int(m[0]) >= int(m[2]):
        if int(m[3]) >= int(m[0]):
            return('True')

# Open the data file and load it into the code
Ids = []
with open('day4.txt', 'r', encoding='utf-8') as file:
    Ids = file.readlines()

Repetitions = 0
for r in Ids:
    if strict_comparison(converter(r)) == 'True':
        Repetitions = Repetitions + 1
print(Repetitions)
