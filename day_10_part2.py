from common import read_input

lines = read_input(10)

register_X = 1
h_pos = 0
raster = ""

for instr in lines:
    raster += "#" if (h_pos % 40)-register_X in [-1,0,1] else " "
    h_pos += 1
    if instr != "noop":
        raster += "#" if (h_pos % 40)-register_X in [-1,0,1] else " "
        h_pos += 1
        register_X += int(instr[5:])

for i in range(0,220,40): print(raster[i:i+40])
