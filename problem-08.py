import heapq
filename = "input-08.txt"

def distance(p1, p2):
    x1,y1,z1 = p1
    x2,y2,z2 = p2

    return ((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2) ** 0.5

class Node:
    def __init__(self, num):
        self.parent = self
        self.num = num
        self.size = 0

def find(num):
    if num.parent != num:
        num.parent = find(num.parent)
        return num.parent
    return num

def union(a, b, d):
    a = find(a)
    b = find(b)

    if a == b:
        return False

    b.parent = a
    a.size = a.size + b.size + d
    return True
    
with open(filename, "r") as in_file:
    data = in_file.read().split("\n")
data = data[:-1]

nodes = [Node(x) for x in range(len(data))]

distances = []
for i, line1 in enumerate(data):
    p1 = [int(x) for x in line1.split(',')]
    for j, line2 in enumerate(data[i+1:], start=i+1):
        p2 = [int(x) for x in line2.split(',')]
        d = distance(p1,p2)
        heapq.heappush(distances, (d, nodes[i], nodes[j]))

distances.sort()
last = None
while distances:
    d, i, j = heapq.heappop(distances)
    if union(i,j, d):
        last = i,j

i,j = last
x1, *_ = data[i.num].partition(',')
x2, *_ = data[j.num].partition(',')
print(int(x1) * int(x2))
