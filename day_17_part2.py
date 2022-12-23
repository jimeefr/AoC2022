from common import read_input

lines = read_input(17)
moves = lines[0]
move_index = 0
blocks = [["@@@@"],[".@..","@@@.",".@.."],["@@@.","..@.","..@."],["@...","@...","@...","@..."],["@@..","@@.."]]
block_index = 0
tunnel = []

W = 7
def can_move_l(h):
    H = len(tunnel)
    for li in range(H):
        l = tunnel[li]
        for i in range(W):
            if l[i] == "@":
                if i == 0: return False
                elif l[i-1] == "#": return False
    return True

def move_l(h):
    if not can_move_l(h): return
    H = len(tunnel)
    for li in range(h,min(h+5,H)):
        l = tunnel.pop(li)
        for i in range(W-1):
            if l[i+1] == "@":
                l = l[:i] + "@." + l[i+2:]
        tunnel.insert(li,l)

def can_move_r(h):
    H = len(tunnel)
    for li in range(h,min(h+5,H)):
        l = tunnel[li]
        for i in range(W):
            if l[i] == "@":
                if i == 6: return False
                elif l[i+1] == "#": return False
    return True

def move_r(h):
    if not can_move_r(h): return
    H = len(tunnel)
    for li in range(h,min(h+5,H)):
        l = tunnel.pop(li)
        for i in range(W-2,-1,-1):
            if l[i] == "@":
                l = l[:i] + ".@" + l[i+2:]
        tunnel.insert(li,l)

def move_lr(h):
    global move_index
    m = moves[move_index]
    move_index = (move_index+1)%len(moves)
    if m == '<': move_l(h)
    else: move_r(h)

def can_move_d(h):
    H = len(tunnel)
    for li in range(h,min(h+5,H)):
        for i in range(W):
            if tunnel[li][i] == "@":
                if li < 1: return False
                elif tunnel[li-1][i] == "#": return False
    return True

def move_d(h):
    H = len(tunnel)
    if can_move_d(h):
        for li in range(h,min(h+5,H)):
            l1 = tunnel.pop(li-1)
            l2 = tunnel.pop(li-1)
            for i in range(W):
                if l2[i] == "@":
                    l1 = l1[:i]+"@"+l1[i+1:]
                    l2 = l2[:i]+"."+l2[i+1:]
            tunnel.insert(li-1,l1)
            tunnel.insert(li,l2)
        while tunnel[-1] == ("."*W): tunnel.pop()
        return True
    else: # stopping move
        for li in range(h,min(h+5,H)):
            l = tunnel.pop(li)
            l = l.replace("@","#")
            tunnel.insert(li,l)
        return False

def fall_block():
    global block_index
    for _ in range(3): tunnel.append("."*W)
    h=len(tunnel)
    for l in blocks[block_index]: tunnel.append("."*2 + l + "."*(W-6))
    block_index = (block_index+1) % 5
    can_move = True
    while can_move:
        move_lr(h)
        can_move = move_d(h)
        h -= 1
    
history = {}
end,loop,dlen=0,0,0
for _ in range(1000000):
    fall_block()
    last = "".join(tunnel[-40:])
    if last in history:
        end,loop,dlen = _,_-history[last][0],len(tunnel)-history[last][1]
        break
    history[last] = _,len(tunnel)
print(len(tunnel),end,loop,dlen)
for _ in range((1_000_000_000_000-end)%loop - 1): fall_block()
print(len(tunnel)+((1_000_000_000_000-end)//loop)*dlen)