from common import read_input
from heapq import *

lines = read_input(12)

H,W = len(lines),len(lines[0])
M = "".join(lines)

def height(x,y): return "SabcdefghijklmnopqrstuvwxyzE".index(M[x + y*W])
def moves(x,y):
    res = []
    h = height(x,y)
    for dx,dy in [(0,-1),(-1,0),(1,0),(0,1)]:
        xx,yy = x+dx,y+dy
        if not 0<=xx<W: continue
        if not 0<=yy<H: continue
        hh = height(xx,yy)
        if hh-h <= 1: res.append((xx,yy))
    return res

SY,SX = divmod(M.index("S"),W)
EY,EX = divmod(M.index("E"),W)

def heuristic(a, b): return (abs(b[0]-a[0] + abs(b[1]-a[1])))
def astar(start, goal):
    close_set,came_from = set(),{}
    gscore,fscore = {start:0},{start:heuristic(start, goal)}
    oheap = []

    heappush(oheap, (fscore[start], start))
    while oheap:
        current = heappop(oheap)[1]
        if current == goal:
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
                
    return False

path = astar((SX,SY), (EX,EY))
print(len(path))
