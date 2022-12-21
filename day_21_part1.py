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

def value(monkey):
    if monkeys[monkey]['op'] == 'const': return monkeys[monkey]['val']
    elif monkeys[monkey]['op'] == '+':
        return value(monkeys[monkey]['val'][0]) + value(monkeys[monkey]['val'][1])
    elif monkeys[monkey]['op'] == '-':
        return value(monkeys[monkey]['val'][0]) - value(monkeys[monkey]['val'][1])
    elif monkeys[monkey]['op'] == '*':
        return value(monkeys[monkey]['val'][0]) * value(monkeys[monkey]['val'][1])
    elif monkeys[monkey]['op'] == '/':
        return value(monkeys[monkey]['val'][0]) // value(monkeys[monkey]['val'][1])
    return False

print(value('root'))