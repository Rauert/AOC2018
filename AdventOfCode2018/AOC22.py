#depth: 6969
#target: 9,796

import time
import heapq

class AOC22:
    depth = 0
    target = [0,0]
    el = [] #Erosion level
    gi = [] #Geological Index - [".","=","|"]
    giv = [] #GI value - [0,1,2]
    offset = 10

    def __init__(self, test):
        if test == True:
            self.depth = 510
            self.target = [10,10]
            self.offset = 10
            #self.target = [2,2]
            #self.offset = 3
        else:
            self.depth = 6969
            self.target = [9,796]
        self.el = [[0 for x in range(self.target[0]+self.offset)] for y in range(self.target[1]+self.offset)]
        self.gi = [["." for x in range(self.target[0]+self.offset)] for y in range(self.target[1]+self.offset)]
        self.giv = [[0 for x in range(self.target[0]+self.offset)] for y in range(self.target[1]+self.offset)]

    def print(self):
        for i in self.gi:
            print("".join(i))
        print()
        for i in self.giv:
            print(''.join(str(x) for x in i))

    def populate(self):
        types = [".","=","|"]
        for y in range(self.target[1]+self.offset):
            for x in range(self.target[0]+self.offset):
                if (x == 0 and y == 0) or (x == self.target[0] and y == self.target[1]):
                    self.el[y][x] = self.depth % 20183
                elif y == 0:
                    self.el[y][x] = ((x * 16807) + self.depth) % 20183
                elif x == 0:
                    self.el[y][x] = ((y * 48271) + self.depth) % 20183
                else:
                    self.el[y][x] = ((self.el[y][x-1] * self.el[y-1][x]) + self.depth) % 20183
                self.giv[y][x] = self.el[y][x] % 3
                self.gi[y][x] = types[self.giv[y][x]]

    def AOC22_1(self):
        now = time.time()
        self.populate()
        count = 0
        for y in range(self.target[1]+1):
            for x in range(self.target[0]+1):
                count += self.giv[y][x]

        #self.print()
        print("AOC22_1: Result:", count)
        print("Time taken: " + str(time.time() - now))


    def AOC22_2(self):
        now = time.time()
        validItems = [[0,1],[1,2],[0,2]] #Index is region's type. 0 = Torch, 1 = Climbing gear, 2 = neither.
        
        #Build Graph
        nodes = []
        edges = {}
        xLen = self.target[0]+self.offset
        yLen = self.target[1]+self.offset

        for y in range(yLen):
            for x in range(xLen):
                for i in range(2):
                    a = (x,y,validItems[self.giv[y][x]][i])
                    j = 0
                    if i == 0: j = 1
                    b = (x,y,validItems[self.giv[y][x]][j])
                    nodes.append(a)
                    if a in edges:
                        edges[a][b] = 7
                    else:
                        edges[a] = {b:7}
                    for dx, dy in ((x, y+1), (x, y-1), (x+1, y), (x-1, y)):
                        #if a == (1, 0, 1): print(dx, dy)
                        if 0 <= dx < xLen and 0 <= dy < yLen:
                            if a[2] in validItems[self.giv[dy][dx]]:
                                #if a == (1, 0, 1): print(i,dx, dy, validItems[self.giv[dy][dx]])
                                edges[a][(dx,dy,a[2])] = 1
        #print(self.target)
        print(xLen*yLen*2)
        #print(len(nodes))
        #print(len(edges))
        #for ii, jj in edges.items():
            #if ii == (1, 0, 1): print(ii, jj)
            #print(ii, jj)
        #Run dijkstra
        #https://stackoverflow.com/questions/30431495/dijkstra-algorithm-python
        start = (0,0,0)
        end = (self.target[0],self.target[1],0)

        pq = [] #Priority queue
        heapq.heappush(pq, (0, start))
        visited = {}
        while pq:
            (currDist, current) = heapq.heappop(pq)
            visited[current] = currDist
            if current == end: break
            if current in edges:
                for neighbour, distance in edges[current].items():
                    #print(neighbour, distance)
                    if neighbour not in visited:
                        #print(neighbour)
                        newDist = currDist + distance
                        heapq.heappush(pq, (newDist, neighbour))
                        #print(len(pq))

        #https://stackoverflow.com/questions/22897209/dijkstras-algorithm-in-python
        #unvisited = {node: None for node in nodes} #using None as +inf
        #visited = {}
        #current = (0,0,0)
        #currentDistance = 0
        #unvisited[current] = currentDistance
        #while True:
        #    for neighbour, distance in edges[current].items():
        #        if neighbour not in unvisited: continue
        #        newDistance = currentDistance + distance
        #        if unvisited[neighbour] is None or unvisited[neighbour] > newDistance:
        #            unvisited[neighbour] = newDistance
        #    visited[current] = currentDistance
        #    del unvisited[current]
        #    if not unvisited: break
        #    candidates = [node for node in unvisited.items() if node[1]]
        #    current, currentDistance = sorted(candidates, key = lambda x: x[1])[0]
        #print(visited)
        print("AOC22_2: Result:", visited[end])
        print("Time taken: " + str(time.time() - now))
