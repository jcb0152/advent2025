from collections import deque
filename = "input-02.txt"

with open(filename, "r") as in_file:
    data = in_file.read().split(",")

cases = deque(data)
invalid = set()
while cases:
    case = cases.pop()
    start, _, end = case.strip().partition('-')

    if len(start) < len(end):
        new_start = f'1{"0"*len(start)}'
        new_end = end
        end = '9'*len(start)
        cases.appendleft(f'{new_start}-{new_end}')

    low = int(start)
    high = int(end)

    for mag in range(len(start) // 2, 0, -1):
        final = end[:(mag - len(start))]
        first = start[:mag]
        for val in range(int(first), int(final) + 1):
            current = val
            while current < low:
                current *= 10 ** len(str(val))
                current += val
            if current > high:
                continue
            invalid.add(current)

print(sum(invalid))

