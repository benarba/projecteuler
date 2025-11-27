def int_to_bytes(n):
    return bytes(sorted(str(n).encode()))


cubes = {}
for i in range(2, 10**10):
    cube = i**3
    index = int_to_bytes(cube)
    if index in cubes:
        cubes[index].add(cube)
        if len(cubes[index]) == 5:
            print(min(cubes[index]))
            break
    else:
        cubes[index] = {cube}
