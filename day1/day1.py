# Download the file and read it into the code
data = []
with open('day1.txt', 'r', encoding='utf-8') as file:
    data = file.readlines()

# Turn all strings into integers
calories_sum = 0
SUM = 0
for r in data:
    if r != '\n':
        r = int(r)
        calories_sum = calories_sum + r
    else:
        SUM = max(SUM, calories_sum)
        calories_sum = 0
        print(SUM)
