from common import read_input

lines = read_input(6)

buffer = lines[0]

def find_marker(buffer,l):
    for i in range(len(buffer)-l+1):
        marker = buffer[i:i+l]
        if len(set(marker)) == l: return i+l
    return -1

print(find_marker(buffer,14))