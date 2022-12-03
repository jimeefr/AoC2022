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

s = 0
for l in lines: s += doubles(l)

print(s)
