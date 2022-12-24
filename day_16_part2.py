from common import read_input

lines = read_input(16)

G = {}

for l in lines:
    w = l.split(' ')
    valve = w[1]
    flow = int(w[4][:-1].split('=')[1])
    neigh = " ".join(w[9:]).split(', ')
    G[valve] = (flow,neigh)

M = len(G.keys())

cache = {}
def rec(valve,left=26,opened=set(),elephant=False):
    h = frozenset(valve),frozenset(opened),elephant
    if h in cache:
        if left == cache[h][0]: return cache[h][1]
        if left < cache[h][0]: return 0
    if left <= 0:
        if elephant: cache[h] = (left,rec('AA',26,opened,False))
        else: cache[h] = (left,0)
        return cache[h][1]
    best = 0
    if valve not in opened:
        best = rec(valve,left-1,opened.union({valve}),elephant) + G[valve][0]*(left-1)
    for n in G[valve][1]:
        best = max(best,rec(n,left-1,opened,elephant))
    cache[h] = left,best
    return best

opened = set()
for v in G:
    if G[v][0] == 0: opened.add(v)
score = rec('AA',26,opened,True)
print(score)
