import sys,re, Functs
from queue import PriorityQueue

#bots = [map(int, re.findall("-?\d+", line)) for line in r"C:\Users\michelle\python\AOC2018-master\AdventOfCode2018\Inputs\AOC23_1.txt"]
bots = []

lines = Functs.importFile(r"C:\Users\michelle\python\AOC2018-master\AdventOfCode2018\Inputs\AOC23_1.txt")
for l in lines:
    tmp = re.split(",|>,\sr=", l.rstrip()[5:])
    bots.append([int(tmp[0]),int(tmp[1]),int(tmp[2]),int(tmp[3])])

q = PriorityQueue()
for x,y,z,r in bots:
  d = abs(x) + abs(y) + abs(z)
  q.put((max(0, d - r),1))
  q.put((d + r + 1,-1))
count = 0
maxCount = 0
result = 0
while not q.empty():
  dist,e = q.get()
  count += e
  if count > maxCount:
    result = dist
    maxCount = count
print(result)
