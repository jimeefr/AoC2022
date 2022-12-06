from common import read_input

lines = read_input(6)

buffer = lines[0]

def find_marker(buffer):
    for i in range(len(buffer)-3):
        marker = buffer[i:i+4]
        if len(set(marker)) == 4: return i+4
    return -1

print(find_marker(buffer))