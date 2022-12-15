from common import read_input

lines = read_input(15)
sensors = []

for l in lines:
    _,_,sx,sy,_,_,_,_,bx,by = l.split()
    by+=' '
    sx,sy,bx,by = map(lambda s:int(s[:-1].split('=')[1]),[sx,sy,bx,by])
    d = abs(sx-bx)+abs(sy-by)
    sensors.append((sx,sy,bx,by,d))

def fusion(ranges,m=0,M=4000000):
    cont = True
    while cont:
        cont = False
        rem = []
        app = []
        for r1,r2 in ranges:
            if r2 < m or r1 > M:
                rem.append((r1,r2))
                cont = True
                break
            if r1 < m:
                rem.append((r1,r2))
                app.append((m,r2))
                cont = True
                break
            if r2 > M:
                rem.append((r1,r2))
                app.append((r1,M))
                cont = True
                break
            for r3,r4 in ranges:
                if r2+1 == r3:
                    app.append((r1,r4))
                    rem.append((r1,r2))
                    rem.append((r3,r4))
                    cont = True
                    break
            if cont: break
        for r in rem: ranges.remove(r)
        for r in app: ranges.append(r)
    return ranges

def no_beacons(Y,m,M):
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
    return fusion(ranges,m,M)

for y in range(4000001):
    r = no_beacons(y,0,4000000)
    if len(r) > 1:
        if r[0][1] < r[1][0]: x = r[0][1]+1
        else: x = r[1][1]+1
        if (x,y) in [(xb,yb) for _,_,xb,yb,_ in sensors]: continue
        print(x*4000000+y)
        break
