# Write a function that checks if the consecutive 4 characters are distinct
def check(s):
    counter = 0
    for i in range(int(len(s) - 3)):
        counter = counter + 1
        if s[i] != s[i + 1] and s[i] != s[i + 2] and s[i] != s[i + 3]:
            if s[i + 1] != s[i + 2] and s[i + 1] != s[i + 3]:
                if s[i + 2] != s[i + 3]:
                    return(int(counter + 3))

# Write a function that deals with checking 14 distinct numbers
def strict_check(a,b,c):
    if c == 0:
        return('True')
    for i in range(c):
        if a[b] == a[b + i + 1]:
            return('False')
    return strict_check(a,(b+1),(c-1))

# Day 6 task 1
Data = []
with open('day6.txt', 'r', encoding='utf-8') as file:
    Data = file.read()

count = 0
for r in range(int(len(Data) - 13)):
    count = count + 1
    if strict_check(Data,r,13) == 'True':
        print(int(count + 13))
