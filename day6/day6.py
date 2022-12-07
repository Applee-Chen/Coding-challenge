# Write a function that checks if the consecutive 4 characters are distinct
def check(s):
    counter = 0
    for i in range(int(len(s) - 3)):
        counter = counter + 1
        if s[i] != s[i + 1] and s[i] != s[i + 2] and s[i] != s[i + 3]:
            if s[i + 1] != s[i + 2] and s[i + 1] != s[i + 3]:
                if s[i + 2] != s[i + 3]:
                    return(int(counter + 3))

            
# Day 6 task 1
Data = []
with open('day6.txt', 'r', encoding='utf-8') as file:
    Data = file.read()

print(check(Data))