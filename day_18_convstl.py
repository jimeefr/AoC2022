from common import read_input

lines = read_input(18)

cubes = []
for l in lines:
    cubes.append(list(map(int,l.split(','))))

def face_stl(x,y,z,dx,dy,dz,r=.5):
    v = []
    if   dx ==-1: v = [(x-r,y-r,z-r),(x-r,y-r,z+r),(x-r,y+r,z+r),(x-r,y+r,z-r)]
    elif dx == 1: v = [(x+r,y-r,z-r),(x+r,y+r,z-r),(x+r,y+r,z+r),(x+r,y-r,z+r)]
    elif dy ==-1: v = [(x-r,y-r,z-r),(x+r,y-r,z-r),(x+r,y-r,z+r),(x-r,y-r,z+r)]
    elif dy == 1: v = [(x-r,y+r,z-r),(x-r,y+r,z+r),(x+r,y+r,z+r),(x+r,y+r,z-r)]
    elif dz ==-1: v = [(x-r,y-r,z-r),(x-r,y+r,z-r),(x+r,y+r,z-r),(x+r,y-r,z-r)]
    elif dz == 1: v = [(x-r,y-r,z+r),(x+r,y-r,z+r),(x+r,y+r,z+r),(x-r,y+r,z+r)]
    print(f"  facet normal {dx:.2e} {dy:.2e} {dz:.2e}")
    print("    outer loop")
    for x,y,z in [v[0],v[1],v[3]]:
        x/=10
        y/=10
        z/=10
        print(f"      vertex {x:.2e} {y:.2e} {z:.2e}")
    print("    endloop")
    print("  endfacet")
    print(f"  facet normal {dx:.2e} {dy:.2e} {dz:.2e}")
    print("    outer loop")
    for x,y,z in [v[1],v[2],v[3]]:
        x/=10
        y/=10
        z/=10
        print(f"      vertex {x:.2e} {y:.2e} {z:.2e}")
    print("    endloop")
    print("  endfacet")


r=.4
print("solid lava")
for x,y,z in cubes:
    if r < .5 or not [x-1,y,z] in cubes: face_stl(x,y,z,-1,0,0,r)
    if r < .5 or not [x+1,y,z] in cubes: face_stl(x,y,z, 1,0,0,r)
    if r < .5 or not [x,y-1,z] in cubes: face_stl(x,y,z,0,-1,0,r)
    if r < .5 or not [x,y+1,z] in cubes: face_stl(x,y,z,0, 1,0,r)
    if r < .5 or not [x,y,z-1] in cubes: face_stl(x,y,z,0,0,-1,r)
    if r < .5 or not [x,y,z+1] in cubes: face_stl(x,y,z,0,0, 1,r)
print("endsolid lava")