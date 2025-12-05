import itertools

filename = "input-04.txt"

with open(filename, "r") as in_file:
    data = in_file.read().split("\n")[:-1]

data = [list(line) for line in data]

dirs = [*itertools.product([-1,0,1], repeat=2)]
dirs.remove((0,0))

access = 0
unchanged = False
while not unchanged:
    unchanged = True
    for y, line in enumerate(data):
        for x, cell in enumerate(line):
            if cell != '@':
                continue
            nearby = 0
            for dx, dy in dirs:
                tx = x + dx
                ty = y + dy
                if tx < 0 or tx >= len(line):
                    continue
                if ty < 0 or ty >= len(data):
                    continue
                if data[ty][tx] == '@':
                    nearby += 1
            if nearby < 4:
                access += 1
                data[y][x] = 'x'
                unchanged = False

print(access)
            
