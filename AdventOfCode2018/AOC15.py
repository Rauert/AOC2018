import time
import Functs
import heapq

class AOC15:
    lines = []
    out = []
    vs = [] #Valid states/coords
    #u = []
    round = 0
    elfDied = False

    def __init__(self, inFile):
        self.lines = Functs.importFile(inFile)

    def print(self, u):
        for y in range(len(self.out)):
            for x in range(len(self.out[y])):
                cr = self.out[y][x]
                for i in u:
                    if x == i[0] and y == i[1]:
                        cr = i[3]
                print(cr,end="")
            #print()

    #Determines if c2 reachable from c1
    def bfs(self, c1, c2, coords):
        #https://stackoverflow.com/questions/20583878/python-check-if-coordinates-of-values-in-a-grid-connect-to-one-another
        def neighbours(cc):
            candidates = [[cc[0] - 1, cc[1]], [cc[0] + 1, cc[1]], [cc[0], cc[1] - 1], [cc[0], cc[1] + 1]]
            return [c for c in candidates if c in coords]
        bool = False
        seen = []
        frontier = [c1]

        while not len(frontier) == 0 and bool == False:
            element = frontier.pop()
            seen.append(element)
            if c2 in seen:
                bool = True
            frontier.extend([n for n in neighbours(element) if not n in seen])
        return bool

    #Determines distance to c2 from c1
    def bfsDistNEW(self, c1, c2, coords):
        coords = set(tuple(x) for x in coords)
        def neighbours(cc):
            candidates = [(cc[0] - 1, cc[1]), (cc[0] + 1, cc[1]), (cc[0], cc[1] - 1), (cc[0], cc[1] + 1)]
            return [c for c in candidates if c in coords]
        seen = {}
        seenDist = []
        frontier = [] #Priority Queue
        heapq.heappush(frontier, (0, set(c1)))

        while not len(frontier) == 0:
            (dist, element) = heapq.heappop(frontier)
            seen[element] = dist
            if c2 in seen:
                break
            nextCoords = [n for n in neighbours(element) if not n in seen]
            for i in nextCoords:
                if (dist + 1, set(i)) not in frontier:
                    heapq.heappush(frontier, (dist + 1, set(i)))
        return seen[c2]

    #Determines distance to c2 from c1
    def bfsDist(self, c1, c2, coords):
        def neighbours(cc):
            candidates = [[cc[0] - 1, cc[1]], [cc[0] + 1, cc[1]], [cc[0], cc[1] - 1], [cc[0], cc[1] + 1]]
            return [c for c in candidates if c in coords]
        bool = False
        seen = []
        seenDist = []
        frontier = [c1]
        frontierDist = [0]
        #print(c1,c2)
        #print(coords)
        while not len(frontier) == 0 and bool == False:
            element = frontier.pop(0)
            dist = frontierDist.pop(0)
            seen.append(element)
            seenDist.append(dist)
            if c2 in seen:
                bool = True
            nextCoords = [n for n in neighbours(element) if not n in seen if not n in frontier]
            for i in nextCoords:
                frontierDist.append(dist + 1)
            frontier.extend(nextCoords)
            #print(nextCoords)
            #print(frontier)
            #print(frontierDist)
        return seenDist[seen.index(c2)]

    #Determines set of coords reachable from c
    def bfsAll(self, c, coords):
        def neighbours(cc):
            candidates = [[cc[0] - 1, cc[1]], [cc[0] + 1, cc[1]], [cc[0], cc[1] - 1], [cc[0], cc[1] + 1]]
            return [c for c in candidates if c in coords]
        seen = []
        frontier = [c]

        while not len(frontier) == 0:
            element = frontier.pop()
            seen.append(element)
            frontier.extend([n for n in neighbours(element) if not n in seen])
        return seen

    def attack(self,i,u,t,ti,attackBonus=0):
        aj = [[i[0],i[1]+1],[i[0]+1,i[1]],[i[0]-1,i[1]],[i[0],i[1]-1]] #Adjacent cells in reverse reading order
        lowHP = 201
        target = -1
        attacked = False
        for a in range(len(aj)):
            if aj[a] in t: #If a target is adjacent
                tIndex = ti[t.index(aj[a])]
                #print(u[tIndex],tIndex, u[tIndex], "is adjacent")
                if u[tIndex][2] <= lowHP:
                    target = tIndex
                    lowHP = u[tIndex][2]
        if target != -1: #Attack
            if i[3] == "e":
                u[target][2] -= 3 + attackBonus
            else:
                u[target][2] -= 3
            if u[target][2] <= 0:
                if u[target][3] == "e": self.elfDied = True
                u[target][2] = 0
                u[target][3] = "d"
            attacked = True
            #print(i, "attacks", u[target])
        return attacked

    def combat(self, u, attackBonus=0, partTwo=False):
        targetsRemain = True
        self.round = 0
        u = sorted(u , key=lambda k: [k[1], k[0]]) #Ensures reading order is maintained
        #Mortal Kombat!!
        while targetsRemain == True:
            #print("Start round", self.round+1)
            #print(u)
            for i in u:
                #self.print(u)
                if i[3] != "d":
                    #print(i)
                    #scan for targets
                    t = [] #Targets
                    ti = [] #Target index
                    en = "e" #Enemy
                    if i[3] == "e": en = "g"
                    for j in u:
                        if i != j and j[3] == en:
                            t.append([j[0],j[1]])
                            ti.append(u.index(j))
                    if len(t) == 0:
                        targetsRemain = False
                        return

                    #Can attack?
                    if self.attack(i,u,t,ti,attackBonus) == False: #Else try to Move
                        if partTwo == True and self.elfDied == True: return
                        t = sorted(t , key=lambda k: [k[1], k[0]])
                        ra = [] #Cells in range
                        vt = [] #Valid Targets
                        ob = [] #Obstacles
                        #Find valid squares
                        for j in u:
                            if i != j and j[3] != "d":
                                ob.append([j[0],j[1]])
                        for ii in range(len(t)):
                            aj = [[t[ii][0]+1,t[ii][1]],[t[ii][0]-1,t[ii][1]],[t[ii][0],t[ii][1]+1],[t[ii][0],t[ii][1]-1]] #Adjacent cells of each target
                            for jj in aj:
                                if jj in self.vs and jj not in ob: #Within a valid cell (Not a wall or elf/goblin)
                                    ra.append(jj)
                        #Reachable? (Path simulation)
                        if len(ra) > 0:
                            reachableCoords = self.bfsAll([i[0],i[1]],[item for item in self.vs if item not in ob])
                            ra = [c for c in ra if c in reachableCoords]
                            #Pick closest
                            if len(ra) > 0:
                                #ra = sorted(ra, key=lambda k: [k[1], k[0]])
                                #closest = ra[len(ra)-1]
                                #dist = abs(i[0]- closest[0]) + abs(i[1]- closest[1])
                                #for ii in range(len(ra)-2,0,-1):
                                #    cDist = abs(i[0]- ra[ii][0]) + abs(i[1]- ra[ii][1])
                                #    if cDist <= dist:
                                #        dist = cDist
                                #        closest = ra[ii]

                                ra = sorted(ra, key=lambda k: [k[1], k[0]], reverse=True)
                                closest = ra[0]
                                dist = self.bfsDist([i[0],i[1]],ra[0],reachableCoords)
                                #print(i, "to", closest, "takes",dist)
                                for ii in range(1,len(ra)):
                                    cDist = self.bfsDist([i[0],i[1]],ra[ii],reachableCoords)
                                    #print(i, "to", ra[ii], "takes",cDist)
                                    if cDist <= dist:
                                        dist = cDist
                                        closest = ra[ii]
                                #Move
                                #Find shortest path/s. take one step.
                                #print(i, "moves towards", closest)
                                #Check each of the 4 adjacent squares distance to target in reverse reading order
                                #lowest is winner.
                                aj = [[i[0],i[1]+1],[i[0]+1,i[1]],[i[0]-1,i[1]],[i[0],i[1]-1]] #Adjacent cells in reverse reading order
                                aj = [c for c in aj if c in reachableCoords]
                                maxDist = 10000
                                step = []
                                for coord in aj:
                                    currDist = self.bfsDist(coord,closest,reachableCoords)
                                    #print(coord, "to", closest, "takes", currDist)
                                    if currDist <= maxDist:
                                        maxDist = currDist
                                        step = coord
                                #print(coord, "moves to", step)
                                i[0] = step[0] #Take step
                                i[1] = step[1]
                                #Try to attack
                                self.attack(i,u,t,ti,attackBonus)
                                if partTwo == True and self.elfDied == True: return
                #print()

            self.round += 1
            u = sorted(u , key=lambda k: [k[1], k[0]]) #Ensures reading order is maintained
            #print(u)
            #self.print(u)
            #print("END ROUND", self.round)
            #targetsRemain = False

    def setup(self):
        u = []
        for y in range(len(self.lines)):
            for x in range(len(self.lines[y])):
                val = self.lines[y][x]
                if val == ".":
                    self.vs.append([x,y])
                elif val == "E":
                    self.vs.append([x,y])
                    u.append([x,y,200,"e"])
                elif val == "G":
                    self.vs.append([x,y])
                    u.append([x,y,200,"g"])
        return u

    def AOC15_1(self):
        now = time.time()

        #Setup
        self.out = self.lines.copy()
        for l in range(len(self.out)):
            self.out[l] = self.out[l].replace("E",".")
            self.out[l] = self.out[l].replace("G",".")

        #Else scan for targets, if targets any still alive, find adjacent locations
        #for nearest to farthest.
        #   Check if reachable
        #   Find for shortest path/s
        #   Make step

        u = self.setup()
        #self.print(u)
        self.combat(u)

        sumHP = 0
        for i in u:
            sumHP += i[2]
        print("AOC15_1: Result:",self.round, sumHP,self.round * sumHP)
        print("Time taken: " + str(time.time() - now))

    def AOC15_2(self):
        now = time.time()

        u = self.setup()
        self.out = self.lines.copy()
        for l in range(len(self.out)):
            self.out[l] = self.out[l].replace("E",".")
            self.out[l] = self.out[l].replace("G",".")

        minBoost = 1
        maxBoost = 10

        #Try a boost in factors of 10.
        while True:
            u = self.setup()
            self.elfDied = False
            self.combat(u, maxBoost, True)
            if self.elfDied == True:
                print("Elf Died", maxBoost)
                minBoost += 10
                maxBoost += 10
            else:
                print("No Elfs Died", maxBoost)
                break

        #Asnwer must lie between min and max.
        while True:
            u = self.setup()
            self.elfDied = False
            self.combat(u, minBoost, True)
            if self.elfDied == True:
                print("Elf Died", minBoost)
                minBoost += 1
            else:
                print("No Elfs Died", minBoost)
                break

        sumHP = 0
        for i in u:
            sumHP += i[2]
        print("AOC15_2: Result:",self.round, sumHP,self.round * sumHP)
        print("Time taken: " + str(time.time() - now))


#aoc15 = AOC15("Inputs/AOC15_1.txt")
aoc15 = AOC15(r"C:\Users\michelle\python\AOC2018-master\AdventOfCode2018\Inputs\AOC15_1.txt")
#aoc15 = AOC15(r"C:\Users\michelle\python\AOC2018-master\AdventOfCode2018\Test\AOC15_2.txt")
#aoc15 = AOC15("Test/AOC15_7.txt")
#aoc15 = AOC15(r"C:\Users\michelle\python\AOC2018-master\AdventOfCode2018\Test\AOC15_1.txt")
aoc15.AOC15_1()
aoc15.AOC15_2()
del aoc15