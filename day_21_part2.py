from common import read_input

lines = read_input(21)

monkeys = {}
for l in lines:
    words = l.split()
    monkey_name = words[0].strip(':')
    if words[1][0] in "0123456789": op,val = 'const',int(words[1])
    else: op,val = words[2], [words[1],words[3]]
    monkey = {'op':op, 'val':val}
    monkeys[monkey_name] = monkey

def locate_humn(monkey):
    if monkeys[monkey]['op'] == 'const': return monkey == 'humn'
    else:
        return locate_humn(monkeys[monkey]['val'][0]) or locate_humn(monkeys[monkey]['val'][1])

def solve_monkey(monkey,val):
    if monkeys[monkey]['op'] == 'const' and monkey == 'humn': return val
    elif monkeys[monkey]['op'] == '+':
        if locate_humn(monkeys[monkey]['val'][0]): return solve_monkey(monkeys[monkey]['val'][0], val-value(monkeys[monkey]['val'][1]))
        else: return solve_monkey(monkeys[monkey]['val'][1], val-value(monkeys[monkey]['val'][0]))
    elif monkeys[monkey]['op'] == '-':
        if locate_humn(monkeys[monkey]['val'][0]): return solve_monkey(monkeys[monkey]['val'][0], val+value(monkeys[monkey]['val'][1]))
        else: return solve_monkey(monkeys[monkey]['val'][1], value(monkeys[monkey]['val'][0])-val)
    elif monkeys[monkey]['op'] == '*':
        if locate_humn(monkeys[monkey]['val'][0]): return solve_monkey(monkeys[monkey]['val'][0], val // value(monkeys[monkey]['val'][1]))
        else: return solve_monkey(monkeys[monkey]['val'][1], val // value(monkeys[monkey]['val'][0]))
    elif monkeys[monkey]['op'] == '/':
        if locate_humn(monkeys[monkey]['val'][0]): return solve_monkey(monkeys[monkey]['val'][0], val*value(monkeys[monkey]['val'][1]))
        else: return solve_monkey(monkeys[monkey]['val'][1], value(monkeys[monkey]['val'][0]) // val)

def value(monkey):
    if monkey == 'humn': print('erreur humn')
    if monkeys[monkey]['op'] == 'const': return monkeys[monkey]['val']
    elif monkeys[monkey]['op'] == '+':
        return value(monkeys[monkey]['val'][0]) + value(monkeys[monkey]['val'][1])
    elif monkeys[monkey]['op'] == '-':
        return value(monkeys[monkey]['val'][0]) - value(monkeys[monkey]['val'][1])
    elif monkeys[monkey]['op'] == '*':
        return value(monkeys[monkey]['val'][0]) * value(monkeys[monkey]['val'][1])
    elif monkeys[monkey]['op'] == '/':
        return value(monkeys[monkey]['val'][0]) // value(monkeys[monkey]['val'][1])

m1 = monkeys['root']['val'][0]
m2 = monkeys['root']['val'][1]
if locate_humn(m1): print(solve_monkey(m1,value(m2)))
else: print(solve_monkey(m2,value(m1)))
