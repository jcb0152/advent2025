filename = "input-01.txt"

with open(filename, "r") as in_file:
    data = in_file.read().split("\n")

num = 50
ans1 = 0
ans2 = 0

for line in data:
    if not line:
        continue
    
    pos, amt = line[0], int(line[1:])
    if pos == 'L':
        amt *= -1

    start = num
    stop = num + amt
    step = 1 if pos == 'R' else -1

    num += amt
    # annoying edge cases
    #ans2 += abs(num // 100)
    ans2 += [x % 100 for x in range(start, stop, step)].count(0)
    num = num % 100
    
    if num == 0:
        ans1 += 1
        
if num == 0:
    ans2 += 1
print(num)
print(ans1)
print(ans2)
