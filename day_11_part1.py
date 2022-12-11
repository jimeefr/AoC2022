from common import read_input

lines = read_input(11)
lines.append("")
M = []

for l in lines:
    if l[2:10] == "Starting": items = list(map(int,l[18:].split(', ')))
    elif l[2:4] == "Op": op = l.split()[-2:]
    elif l[2:4] == "Te": te = int(l.split()[-1])
    elif l[7:9] == "tr": tr = int(l.split()[-1])
    elif l[7:9] == "fa": fa = int(l.split()[-1])
    elif l == "": M.append([items,op,te,tr,fa])

def inspect(m,i):
    _,op,te,tr,fa = m
    t = i if op[1] == 'old' else int(op[1])
    if   op[0] == '+': i += t
    elif op[0] == '*': i *= t
    i //= 3
    d = tr if i%te == 0 else fa
    M[d][0].append(i)

n_monkeys = len(M)
inspections = [0]*len(M)

def monkey_business():
    for m in range(n_monkeys):
        for i in M[m][0]:
            inspections[m] += 1
            inspect(M[m],i)
        M[m][0]=[]

for _ in range(20): monkey_business()

inspections.sort()
print(inspections[-1]*inspections[-2])
