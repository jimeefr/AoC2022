from common import read_input

lines = read_input(5)

empty_pos = lines.index('')
columns = lines[empty_pos-1][1::4]
stacks = { _:"" for _ in columns }

for l in lines[empty_pos-2::-1]:
    for i,c in zip(columns,l[1::4]):
        if c != ' ': stacks[i]+=c

orders = [ l.split()[1::2] for l in lines[empty_pos+1:] ]
for n,from_stack,to_stack in orders:
    n = int(n)
    stacks[to_stack]  += stacks[from_stack][-n:][::-1]
    stacks[from_stack] = stacks[from_stack][:-n]

print("".join([stacks[s][-1] for s in columns]))
