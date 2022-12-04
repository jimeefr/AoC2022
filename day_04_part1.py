from common import read_input

lines = read_input(4)

def includes(set1,set2):
    inter = set1.intersection(set2)
    if inter == set1: return 1
    if inter == set2: return 1
    return 0

def read_line(l):
    a,b,c,d = list(map(int,l.replace('-',',').split(',')))
    return set(range(a,b+1)),set(range(c,d+1))

score = 0
for l in lines: score += includes(*read_line(l))

print(score)
