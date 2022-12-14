from common import read_input

lines = read_input(14)

blocks = {}
for l in lines:
    points = l.split(' -> ')
    x1,y1 = points[0].split(',')
    for p in points[1:]:
        x2,y2 = p.split(',')
        x1,x2,y1,y2 = map(int,([x1,x2,y1,y2]))
        if x1==x2:
            d = 1 if y2>y1 else -1
            for y in range(y1,y2,d): blocks[(x1,y)] = True
        else:
            d = 1 if x2>x1 else -1
            for x in range(x1,x2,d): blocks[(x,y1)] = True
        x1,y1 = x2,y2
    blocks[(x2,y2)] = True

X1 = min([p[0] for p in blocks])
X2 = max([p[0] for p in blocks])
Y1 = min([p[1] for p in blocks])
Y2 = max([p[1] for p in blocks])

Y1 = min(0,Y1)

def print_map(sands):
    for y in range(Y1,Y2+1):
        s=""
        for x in range(X1,X2+1):
            if (x,y) in blocks: s += "#"
            elif (x,y) in sands: s += "o"
            else: s += "."
        print(s)

def sands_that_can_fall():
    global X1,Y1,X2,Y2
    xs,ys = 500,0
    sands = {(xs,ys):True}
    c = 1
    x1,x2 =xs,xs
    while ys <= Y2:
        x1,x2 = x1-1,x2+1
        X1,X2 = min(X1,x1),max(X2,x2)
        ys += 1
        for xs in range(x1,x2+1):
            if (xs-1,ys-1) in sands or (xs,ys-1) in sands or (xs+1,ys-1) in sands:
                if not (xs,ys) in blocks:
                    sands[(xs,ys)] = True
                    c += 1
    print_map(sands)
    return c

sand = sands_that_can_fall()
print(sand)