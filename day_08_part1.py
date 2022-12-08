from common import read_input

lines = read_input(8)

def is_visible(x,y):
    h = lines[x][y]
    if x==0 or x==len(lines)-1 or y == 0 or y==len(lines[0])-1: return True
    if max(lines[x][:y]) < h: return True
    if max(lines[x][y+1:]) < h: return True
    if max([lines[i][y] for i in range(x)]) < h: return True
    if max([lines[i][y] for i in range(x+1,len(lines))]) < h: return True
    return False
    
score = 0
for x in range(len(lines)):
    for y in range(len(lines[0])):
        if is_visible(x,y): score += 1
print(score)
