from common import read_input

lines = read_input(2)

val = {
    'X':{'A':4,'B':1,'C':7},
    'Y':{'A':8,'B':5,'C':2},
    'Z':{'A':3,'B':9,'C':6}}

score = 0
for l in lines:
    a,b = l.split()
    score += val[b][a]

print(score)
