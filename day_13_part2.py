from common import read_input
from functools import cmp_to_key

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

dividers = [[[2]],[[6]]]
packets = sorted(dividers + [ eval(l) for l in lines if l != ""],key=cmp_to_key(compare))

score = 1
for i in range(len(packets)):
    if packets[i] in dividers: score *= i+1 

print(score)
