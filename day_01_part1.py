from common import read_input

lines = read_input(1)

current_calories = 0
max_calories = 0
for l in lines:
    if l == "":
        current_calories = 0
        continue
    c = int(l)
    current_calories += c
    max_calories = max(max_calories,current_calories)
print(max_calories)
