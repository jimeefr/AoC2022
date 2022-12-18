from common import read_input

lines = read_input(18)

cubes = []
for l in lines:
    cubes.append(list(map(int,l.split(','))))

free_faces = 6*len(cubes)
for i in range(len(cubes)):
    x1,y1,z1 = cubes[i]
    for j in range(i+1,len(cubes)):
        x2,y2,z2 = cubes[j]
        if abs(x1-x2)+abs(y1-y2)+abs(z1-z2) == 1: free_faces -= 2
print(free_faces)
