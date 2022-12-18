from common import read_input

lines = read_input(18)

cubes = []
for l in lines:
    cubes.append(list(map(int,l.split(','))))


X1=min([c[0] for c in cubes])
X2=max([c[0] for c in cubes])
Y1=min([c[1] for c in cubes])
Y2=max([c[1] for c in cubes])
Z1=min([c[2] for c in cubes])
Z2=max([c[2] for c in cubes])

p = [X1-1,Y1-1,Z1-1]
to_visit = [p]
visited = cubes[:]
ext_faces = 0
while to_visit:
    x1,y1,z1 = to_visit.pop()
    visited.append([x1,y1,z1])
    if not X1-1 <= x1 <= X2+1: continue
    if not Y1-1 <= y1 <= Y2+1: continue
    if not Z1-1 <= z1 <= Z2+1: continue
    for x2,y2,z2 in cubes:
        if abs(x1-x2)+abs(y1-y2)+abs(z1-z2) == 1: ext_faces += 1
    for p in [[x1-1,y1,z1],[x1+1,y1,z1],[x1,y1-1,z1],[x1,y1+1,z1],[x1,y1,z1-1],[x1,y1,z1+1]]:
        if p in visited: continue
        if p in to_visit: continue
        if p in cubes: continue
        to_visit.append(p)
print(ext_faces)