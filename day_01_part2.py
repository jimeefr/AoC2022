from common import read_input

lines = read_input(1)

current_calories = 0
elves = []
for l in lines:
    if l == "":
        elves.append(current_calories)
        current_calories = 0
        continue
    c = int(l)
    current_calories += c
elves.append(current_calories)
print(sum(sorted(elves)[-3:]))
