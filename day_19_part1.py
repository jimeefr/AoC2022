from common import read_input

lines = read_input(19)

blueprints = {}
for l in lines : 
    bl = l.split()
    b = {}
    blueprints[int(bl[1].strip(':'))] = [ int(bl[6]), int(bl[12]), int(bl[18]),int(bl[21]), int(bl[27]),int(bl[30]) ]

cache = {}
def best(bid,time=24,bo=1,bc=0,bb=0,bg=0,ro=0,rc=0,rb=0,rg=0):
    global cache
    if time==0: return rg
    coo,cco,cbo,cbc,cgo,cgb = blueprints[bid]
    Mco = max([coo,cco,cbo,cgo])
    if bo > Mco: bo = Mco
    if ro > time*Mco-(time-1)*bo: ro = time*Mco-(time-1)*bo
    if bc > cbc: bc = cbc
    if rc > time*cbc - bc*(time-1): rc = time*cbc - bc*(time-1)
    if bb > cgb: bb = cgb
    if rb > time*cgb - bb*(time-1): rb = time*cgb - bb*(time-1)
    if (bid,time,bo,bc,bb,bg,ro,rc,rb,rg) in cache:
        return cache[(bid,time,bo,bc,bb,bg,ro,rc,rb,rg)]
    if ro >= cgo and rb >= cgb:
        rep = best(bid,time-1,bo,bc,bb,bg+1,ro+bo-cgo,rc+bc,rb+bb-cgb,rg+bg)
        cache[(bid,time,bo,bc,bb,bg,ro,rc,rb,rg)] = rep
        return rep
    scores = [best(bid,time-1,bo,bc,bb,bg,ro+bo,rc+bc,rb+bb,rg+bg)]
    if ro >= cbo and rc >= cbc:
        scores.append(best(bid,time-1,bo,bc,bb+1,bg,ro+bo-cbo,rc+bc-cbc,rb+bb,rg+bg))
    if ro >= cco:
        scores.append(best(bid,time-1,bo,bc+1,bb,bg,ro+bo-cco,rc+bc,rb+bb,rg+bg))
    if ro >= coo:
        scores.append(best(bid,time-1,bo+1,bc,bb,bg,ro+bo-coo,rc+bc,rb+bb,rg+bg))
    rep = max(scores)
    cache[(bid,time,bo,bc,bb,bg,ro,rc,rb,rg)] = rep
    return rep

scores = []
for i in blueprints:
    cache = {}
    s = best(i)
    print(i,s,len(cache.keys()))
    scores.append(i*s)
print(sum(scores))