from collections import defaultdict

filename = "input-05.txt"

with open(filename, "r") as in_file:
    data = in_file.read().split("\n")
data = data[:-1]

ranges = []

lines = iter(data)
for line in lines:
    if not line:
        break
    low, _, high = line.partition('-')
    ranges.append((int(low), int(high)))

ranges.sort(key=lambda x: x[0])

combined = []
prev = ranges[0]
for low, high in ranges:
    if low <= prev[1]:
        prev = (prev[0], max(prev[1], high))
    else:
        combined.append(prev)
        prev = (low, high)

combined.append(prev)

total = 0
for low, high in combined:
    total += high - low + 1
print(total)
