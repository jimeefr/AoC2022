from common import read_input

lines = read_input(7)

G = {'':[[],0]}

def add_child(dir,name,size=0):
    G[dir][0].append(dir+'/'+name)
    G[dir+'/'+name] = [[],size]

cwd = ''
for l in lines[1:]:
    if l[0] == '$':
        if l[2:4] == "cd":
            if l[5:] == '..':
                cwd = "/".join(cwd.split("/")[:-1])
            else:
                cwd = cwd + '/' + l[5:]
        elif l[2:4] == "ls":
            pass
        else:
            print(l," : Command not found")
    else: # ls output
        size,name = l.split()
        if size == "dir": add_child(cwd,name)
        else: add_child(cwd,name,int(size))

def du(dir):
    if G[dir][1] == 0:
        for d in G[dir][0]:
            G[dir][1] += du(d)
    return G[dir][1]

def du_limit(dir,limit):
    s = 0
    if G[dir][1] <= limit and G[dir][0]: s += G[dir][1]
    for d in G[dir][0]:
        s += du_limit(d,limit)
    return s

du('')
print(du_limit('',100000))