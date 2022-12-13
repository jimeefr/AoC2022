from common import read_input
from ast import literal_eval as eval

lines = read_input(13)
lines.append('')

def compare(a,b):
    if type(a) is int and type(b) is int:
        if a==b: return 0
        elif a<b: return -1
        else: return 1
    elif type(a) is list and type(b) is list:
        for i in range(len(a)):
            if i > len(b)-1: return 1
            c = compare(a[i],b[i])
            if c == 0: continue
            return c
        else: 
            if len(b)>len(a): return -1
            else: return 0
    elif type(a) is int: return compare([a],b)
    else: return compare(a,[b])

score = 0
for i in range((len(lines)+1) // 3):
    l1 = eval(lines[3*i])
    l2 = eval(lines[3*i+1])
    c = compare(l1,l2)
    if c<=0: score += i+1
print(score)
