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

def print_map():
    for y in range(Y1,Y2+1):
        s=""
        for x in range(X1,X2+1):
            s += '#' if (x,y) in blocks else "."
        print(s)

def sand_can_fall():
    xs,ys = 500,0
    while X1<=xs<=X2 and Y1<=ys<=Y2:
        ys += 1
        if (xs,ys) in blocks:
            xs-=1
            if (xs,ys) in blocks:
                xs+=2
                if (xs,ys) in blocks: 
                    xs-=1
                    ys-=1
                    blocks[(xs,ys)] = True
                    return True
    return False

print(X1,X2,Y1,Y2)

sand = 0
while sand_can_fall(): sand += 1
print_map()
print(sand)