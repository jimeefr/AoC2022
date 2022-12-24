from common import read_input
from math import gcd
from heapq import *

lines = read_input(24)
dirs = [(0,1),(1,0),(0,-1),(-1,0)]

W = len(lines[0])
H = len(lines)

blizzards = []
for y,l in enumerate(lines):
    for x,c in enumerate(l):
        d = "v>^<".find(c)
        if d>=0: blizzards.append((x,y,d))

def move_blizzards(blizzards):
    new_blizzards = []
    for x,y,d in blizzards:
        x += dirs[d][0]
        y += dirs[d][1]
        if x==0: x=W-2
        if x==W-1: x=1
        if y==0: y=H-2
        if y==H-1: y=1
        new_blizzards.append((x,y,d))
    return new_blizzards

blizzards_list = []
B = (H-2)*(W-2) // gcd(H-2,W-2)
b = blizzards
for _ in range(B):
    blizzards_list.append(set((x,y) for x,y,d in b))
    b = move_blizzards(b)

def moves(x,y,turn):
    bl = blizzards_list[turn%B]
    n = []
    for dx,dy in dirs:
        xx,yy = x+dx,y+dy
        if not 0<=xx<=W-1: continue
        if not 0<=yy<=H-1: continue
        if lines[yy][xx] == '#': continue
        if (xx,yy) not in bl: n.append((xx,yy,turn+1))
        if (x,y) not in bl: n.append((x,y,turn+1))
    return n

def heuristic(a, b): return (abs(b[0]-a[0] + abs(b[1]-a[1])) + abs(b[2]-a[2]))
def astar(start, goal):
    close_set,came_from = set(),{}
    gscore,fscore = {start:0},{start:heuristic(start, goal)}
    oheap = []

    heappush(oheap, (fscore[start], start))
    while oheap:
        current = heappop(oheap)[1]
        if current[0] == goal[0] and current[1] == goal[1]:
            data = []
            while current in came_from:
                data.append(current)
                current = came_from[current]
            return data

        close_set.add(current)
        for neighbor in moves(*current):
            tentative_g_score = gscore[current] + heuristic(current, neighbor)
            if neighbor in close_set and tentative_g_score >= gscore.get(neighbor, 0): continue
            if tentative_g_score < gscore.get(neighbor, 0) or neighbor not in [i[1]for i in oheap]:
                came_from[neighbor] = current
                gscore[neighbor] = tentative_g_score
                fscore[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                heappush(oheap, (fscore[neighbor], neighbor))

print(W,H,B)
path = astar((1,0,1),(W-2,H-1,0))
print(len(path))