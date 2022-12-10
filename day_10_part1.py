from common import read_input

lines = read_input(10)

register_X = 1
cycle = 1
signal = []

for instr in lines:
    signal.append(register_X*cycle)
    cycle += 1
    if instr != "noop":
        signal.append(register_X*cycle)
        cycle += 1
        register_X += int(instr[5:])

print(sum(signal[19::40]))
