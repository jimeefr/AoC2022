from common import read_input

lines = read_input(15)
sensors = []

for l in lines:
    _,_,sx,sy,_,_,_,_,bx,by = l.split()
    by+=' '
    sx,sy,bx,by = map(lambda s:int(s[:-1].split('=')[1]),[sx,sy,bx,by])
    d = abs(sx-bx)+abs(sy-by)
    sensors.append((sx,sy,bx,by,d))

Y=2000000
score = 0
ranges = []
for xs,ys,xb,yb,d in sensors:
    if abs(ys-Y) > d: continue
    x1 = xs - d+abs(Y-ys)
    x2 = xs + d-abs(Y-ys)
    if yb == Y:
        if x1 == xb: x1 += 1
        if x2 == xb: x2 -= 1
    rem = []
    for r1,r2 in ranges:
        if x2<x1: continue
        if r1<=x1<=r2:
            if x2 <= r2: x2=x1-1
            x1 = r2+1
        if r1<=x2<=r2:
            if x1 >= r1: x2=x1-1
            x2 = r1-1
        if x1 <= r1 and x2 >= r2: rem.append((r1,r2))
    for r in rem: ranges.remove(r)
    if x2>=x1: ranges.append((x1,x2))
for r1,r2 in ranges: score += r2-r1+1
print(score)
