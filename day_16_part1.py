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
def rec(valve,left=30,opened=set()):
    h = frozenset(valve),frozenset(opened)
    if h in cache:
        if left == cache[h][0]: return cache[h][1]
        if left < cache[h][0]: return 0
    if len(opened) == M or left <= 0:
        cache[h] = (left,0)
        return 0
    best = 0
    if valve not in opened:
        best = rec(valve,left-1,opened.union({valve})) + G[valve][0]*(left-1)
    for n in G[valve][1]:
        best = max(best,rec(n,left-1,opened))
    cache[h] = left,best
    return best

opened = set()
for v in G:
    if G[v][0] == 0: opened.add(v)
score = rec('AA',opened=opened)
print(score)
