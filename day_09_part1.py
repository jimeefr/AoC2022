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
        if yy != y: yy += (y-yy)
    if abs(y-yy) == 2:
        yy += (y-yy) // 2
        if xx != x: xx += (x-xx)
    return xx,yy

tail_pos,head_pos = (0,0),(0,0)
path = [tail_pos]
for l in lines:
    d,count = l.split()
    for _ in range(int(count)):
        head_pos = move(*head_pos,d)
        tail_pos = follow(*head_pos,*tail_pos)
        path.append(tail_pos)
print(len(set(path)))
