
filename = "input-07.txt"

with open(filename, "r") as in_file:
    data = in_file.read().split("\n")
data = data[:-1]

current = [0] * len(data[0])
splits = 0
for line in data:
    for i, val in enumerate(line):
        if val == 'S':
            current[i] = 1
        elif val == '^' and current[i] != 0:
            tmp = current[i]
            current[i] = 0
            splits += 1
            if i > 0:
                current[i-1] += tmp
            if i < len(line) - 1:
                current[i+1] += tmp
                
print(splits)
print(sum(current))
