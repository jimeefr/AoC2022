from common import read_input

lines = read_input(23)

positions = set()
for y,l in enumerate(lines):
    for x,c in enumerate(l):
        if c == '#': positions.add((x,y))

def N(x,y): return {(x-1,y-1),(x,y-1),(x+1,y-1)}
def S(x,y): return {(x-1,y+1),(x,y+1),(x+1,y+1)}
def W(x,y): return {(x-1,y-1),(x-1,y),(x-1,y+1)}
def E(x,y): return {(x+1,y-1),(x+1,y),(x+1,y+1)}
def A(x,y): return {(x-1,y-1),(x-1,y),(x-1,y+1),(x,y+1),(x+1,y+1),(x+1,y),(x+1,y-1),(x,y-1)}

def T(x,y,pos,d):
    d%=4
    nx,ny,m = x,y,False
    if d==0 and not N(x,y).intersection(pos): nx,ny,m = x,y-1,True
    if d==1 and not S(x,y).intersection(pos): nx,ny,m = x,y+1,True
    if d==2 and not W(x,y).intersection(pos): nx,ny,m = x-1,y,True
    if d==3 and not E(x,y).intersection(pos): nx,ny,m = x+1,y,True
    return nx,ny,m

def move(pos,dir):
    dest = set()
    conflicts = set()
    prev = {}
    for x,y in pos:
        nx,ny = x,y
        if not A(x,y).intersection(pos): nx,ny = x,y
        else:
            for d in range(dir,dir+4):
                nx,ny,moved = T(x,y,pos,d)
                if moved: break
        if (nx,ny) in conflicts: nx,ny=x,y
        if (nx,ny) in dest:
            px,py = nx,ny
            while (px,py) in prev:
                dest.remove((px,py))
                conflicts.add((px,py))
                ppx,ppy = prev[(px,py)]
                del prev[(px,py)]
                px,py = ppx,ppy
                dest.add((px,py))
            conflicts.add((px,py))
            nx,ny = x,y
        assert (nx,ny) not in dest
        dest.add((nx,ny))
        if (nx,ny) != (x,y): prev[(nx,ny)]=(x,y)
    assert len(dest)==len(pos)
    return dest

d = 0
while True:
    new_positions = move(positions,d)
    d += 1
    if new_positions == positions: break
    positions = new_positions
print(d)
