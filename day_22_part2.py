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
    dl,dc = dirs[d]
    for _ in range(n):
        nl,nc,nd = l+dl,c+dc,d
        if nl < 0 or nl >= L or nc < 0 or nc >= len(lines[nl]) or lines[nl][nc] == ' ':
            # change face:
            #   1122
            #   33
            # 4455
            # 66
            if d==0:
                if nl < 50:    nl,nc,nd = 149-nl, 99, 2 # face 2 to 5
                elif nl < 100: nl,nc,nd = 49, nl+50,  3 # face 3 to 2
                elif nl < 150: nl,nc,nd = 149-nl, 149,2 # face 5 do 2
                else:          nl,nc,nd = 149, nl-100,3 # face 6 to 5
            elif d==1:
                if nc < 50:    nl,nc,nd = 0, nc+100,  1 # face 6 to 2
                elif nc < 100: nl,nc,nd = nc+100, 49, 2 # face 5 to 6
                else:          nl,nc,nd = nc-50, 99,  2 # face 2 to 3
            elif d==2:
                if nl < 50:    nl,nc,nd = 149-nl, 0,  0 # face 1 to 4
                elif nl < 100: nl,nc,nd = 100, nl-50, 1 # face 3 to 4
                elif nl < 150: nl,nc,nd = 149-nl, 50, 0 # face 4 to 1
                else:          nl,nc,nd = 0, nl-100,  1 # face 6 to 1
            else:
                if nc < 50:    nl,nc,nd = nc+50, 50,  0 # face 4 to 3
                elif nc < 100: nl,nc,nd = nc+100, 0,  0 # face 1 to 6
                else:          nl,nc,nd = 199, nc-100,3 # face 2 to 6
        if lines[nl][nc] == '#': return l,c,d
        assert lines[nl][nc] == '.'
        l,c,d = nl,nc,nd
        dl,dc = dirs[d]
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