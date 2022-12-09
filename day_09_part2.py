from common import read_input

lines = read_input(9)

def move(x,y,d):
    if 'R' in d: x+=1
    if 'L' in d: x-=1
    if 'U' in d: y+=1
    if 'D' in d: y-=1
    return x,y

def follow(x,y,xx,yy):
    if abs(x-xx) < 2 and abs(y-yy) < 2: return xx,yy
    if abs(x-xx) == 2:
        xx += (x-xx) // 2
        if abs(y-yy) == 2: yy += (y-yy) // 2
        elif yy != y: yy += (y-yy)
    if abs(y-yy) == 2:
        yy += (y-yy) // 2
        if abs(x-xx) == 2: xx += (x-xx) // 2
        elif xx != x: xx += (x-xx)
    return xx,yy

rope = [(0,0)] * 10
path = [(0,0)]
for l in lines:
    d,count = l.split()
    for _ in range(int(count)):
        rope[0] = move(*rope[0],d)
        for i in range(len(rope)-1): rope[i+1] = follow(*rope[i],*rope[i+1])
        path.append(rope[-1])
print(len(set(path)))
