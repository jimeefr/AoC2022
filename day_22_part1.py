from common import read_input

lines = read_input(22)
path = lines.pop()
lines.pop()

start = 0,lines[0].index('.'),0
dirs = [(0,1),(1,0),(0,-1),(-1,0)]
L = len(lines)
C = max(len(l) for l in lines)

def move(pos,n):
    l,c,d = pos
    C = len(lines[l])
    dl,dc = dirs[d]
    for _ in range(n):
        nl,nc = (l+dl)%L,(c+dc)%C
        while nc >= len(lines[nl]) or lines[nl][nc] == ' ':
            nl,nc = (nl+dl)%L,(nc+dc)%C
        if lines[nl][nc] == '#': return l,c,d
        l,c = nl,nc
    return l,c,d

def turn(pos,dir):
    l,c,d = pos
    if dir == 'R': return l,c,(d+1)%4
    return l,c,(d-1)%4

def res(pos):
    l,c,d = pos
    l+=1
    c+=1
    return 1000*l + 4*c + d

pos = start
dep = 0
for c in path:
    if c in "LR":
        pos = move(pos,dep)
        dep = 0
        pos = turn(pos,c)
    else:
        dep = dep*10 + "0123456789".index(c)
pos = move(pos,dep)
print(res(pos))