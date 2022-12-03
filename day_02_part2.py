from common import read_input

lines = read_input(2)

val = {
    'X':{'A':3,'B':1,'C':2},
    'Y':{'A':4,'B':5,'C':6},
    'Z':{'A':8,'B':9,'C':7}}

score = 0
for l in lines:
    a,b = l.split()
    score += val[b][a]

print(score)
