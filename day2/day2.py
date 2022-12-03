# Write a function that returns scores of each round
def score(s):
    SCORE = 0
    if s[2] == 'X':
        if s[0] == 'A':
            SCORE = SCORE + 3
        elif s[0] == 'B':
            SCORE = SCORE + 1
        else:
            SCORE  = SCORE + 2
        
    elif s[2] == 'Y':
        SCORE = SCORE + 3
        if s[0] == 'A':
            SCORE = SCORE + 1
        elif s[0] == 'B':
            SCORE = SCORE + 2
        else:
            SCORE = SCORE + 3
    else:
        SCORE = SCORE + 6
        if s[0] == 'A':
            SCORE = SCORE + 2
        elif s[0] == 'B':
            SCORE = SCORE + 3
        else:
            SCORE = SCORE + 1
        
    return SCORE

# Open the file and load it into our code
strategies = []
with open('day2.txt', 'r', encoding='utf-8') as file:
    strategies = file.readlines()
# Pass the file into a for loop
total_score = 0
for r in strategies:
    total_score = total_score + score(r)
print(total_score)

