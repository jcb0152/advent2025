

filename = "input-03.txt"

with open(filename, "r") as in_file:
    data = in_file.read().split("\n")

joltages = []
for line in data:
    if not line:
        continue

    num_batteries = 12
    nums = []

    start = 0
    end = len(line) - num_batteries
    for i in range(num_batteries, 0, -1):
        current = -1
        loc = start
        for val in line[start:end + 1]:
            val = int(val)
            if val > current:
                current = val
                start = loc + 1
            loc += 1
        end += 1
        nums.append(current)
    joltages.append(int(''.join(str(x) for x in nums)))

print(sum(joltages))
