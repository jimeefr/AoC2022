from common import read_input

lines = read_input(20)
numbers = []
for l in lines: numbers.append(int(l))

def mix(lin):
    pos = list(range(len(lin)))
    mod = len(lin)-1
    for i in range(len(lin)):
        oldpos = pos.index(i)
        offset = lin[i]
        newpos = (oldpos + offset) % mod
        pos.remove(i)
        pos.insert(newpos,i)
    return [lin[j] for j in pos]

def rep(n):
    p = n.index(0)
    l = len(n)
    return n[(p+1000)%l] + n[(p+2000)%l] + n[(p+3000)%l]

numbers = mix(numbers)
print(rep(numbers))