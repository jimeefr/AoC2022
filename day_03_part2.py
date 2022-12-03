from common import read_input

lines = read_input(3)

def priority(item): return "_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ".index(item)

def doubles(pack):
    d = ""
    p = 0
    p1 = pack[:len(pack)//2]
    p2 = pack[len(pack)//2:]
    for i in p1:
        if i in p2:
            if not i in d:
                d += i
                p += priority(i)
    return p

def badge(packs):
    for i in packs[0]:
        if i in packs[1] and i in packs[2]: return priority(i)
    assert(False)

s = 0
for i in range(len(lines)//3): s += badge(lines[3*i:3*i+3])

print(s)
