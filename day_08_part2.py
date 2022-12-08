from common import read_input

lines = read_input(8)

def viewable_line(l):
    if len(l)==1: return 0
    r = 0
    for h in l[1:]:
        r += 1
        if h >= l[0]: break
    return r
    
def viewable(x,y):
    r  = viewable_line(lines[x][:y+1][::-1])
    r *= viewable_line(lines[x][y:])
    r *= viewable_line([lines[i][y] for i in range(x+1)][::-1])
    r *= viewable_line([lines[i][y] for i in range(x,len(lines[0]))])
    return r

score = 0
for x in range(len(lines)):
    for y in range(len(lines[0])):
        v = viewable(x,y)
        if v > score: score  = v
print(score)
