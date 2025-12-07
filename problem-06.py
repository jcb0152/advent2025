import math
filename = "input-06.txt"

with open(filename, "r") as in_file:
    data = in_file.read().split("\n")
data = data[:-1]

problems = []
nums = []
op = None
for a,b,c,d,e in zip(*data):
    tmp = f'{a}{b}{c}{d}'.strip()
    if not tmp:
        problems.append((op, *nums))
        nums = []
        op = None
        continue

    nums.append(int(tmp))
    if e.strip():
        op = e

problems.append((op, *nums))
    
ans = 0
for op, *nums in problems:
    match op:
        case '+':
            ans += sum(nums)
        case '*':
            ans += math.prod(nums)
print(ans)
    
