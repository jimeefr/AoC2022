from common import read_input

lines = read_input(25)

def snafu(s):
    n=0
    for c in s: n = 5*n + "=-012".index(c) - 2
    return n

def unsnafu(n):
    s=""
    while n:
        n,r = divmod(n,5)
        if r>2: n+=1
        s = "012=-"[r%5] + s
    return s

score = 0
for l in lines: score += snafu(l)
print(unsnafu(score))
