import time
import Functs

class AOC15:
    lines = []
    out = []
    vs = [] #Valid states/coords
    #u = []
    round = 0

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

    def combat(self, lines, u):
        targetsRemain = True
        u = sorted(u , key=lambda k: [k[1], k[0]]) #Ensures reading order is maintained
        #Mortal Kombat!!
        while targetsRemain == True:
            for i in u:
                #self.print(u)
                if i[3] != "d":
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
                    #t = sorted(t , key=lambda k: [k[1], k[0]])
                    aj = [[i[0],i[1]+1],[i[0]+1,i[1]],[i[0]-1,i[1]],[i[0],i[1]-1]] #Adjacent cells in reverse reading order
                    lowHP = 201
                    target = -1
                    for a in range(len(aj)):
                        if aj[a] in t: #If a target is adjacent
                            tIndex = ti[t.index(aj[a])]
                            if t[tIndex][2] <= lowHP:
                                target = tIndex
                                lowHP = t[tIndex][2]
                    if target != -1: #Attack
                        t[tIndex][2] -= 3
                        if u[tIndex][2] <= 0:
                            u[ii][3] = "d"
                        print(i, "attacks", t[tIndex])
                        #print(vt)
                        #print(u)
                    else: #Try to Move
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
                            reachableCoords = self.bfsAll((i[0],i[1]),[item for item in self.vs if item not in ob])
                            ra = [c for c in ra if c in reachableCoords]
                            #Pick closest
                            if len(ra) > 0:
                                ra = sorted(ra, key=lambda k: [k[1], k[0]])
                                closest = ra[len(ra)-1]
                                dist = abs(i[0]- closest[0]) + abs(i[1]- closest[1])
                                for ii in range(len(ra)-2,0,-1):
                                    cDist = abs(i[0]- ra[ii][0]) + abs(i[1]- ra[ii][1])
                                    if cDist <= dist:
                                        dist = cDist
                                        closest = ra[ii]
                                #Move
                                #Find shortest path/s. take one step.
                                print(i, "moves towards", closest)
                                #Check each of the 4 adjacent squares distance to target in reverse reading order
                                #lowest is winner.
            self.round += 1
            u = sorted(u , key=lambda k: [k[1], k[0]]) #Ensures reading order is maintained
            self.print(u)
            targetsRemain = False

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
        lines = self.lines

        #Setup
        u = self.setup()

        self.out = self.lines.copy()
        for l in range(len(self.out)):
            self.out[l] = self.out[l].replace("E",".")
            self.out[l] = self.out[l].replace("G",".")

        #Else scan for targets, if targets any still alive, find adjacent locations
        #for nearest to farthest.
        #   Check if reachable
        #   Find for shortest path/s
        #   Make step

        self.print(u)
        self.combat(lines, u)

        sumHP = 0
        for i in u:
            if i[3] == "g" or i[3] == "e":
                sumHP += i[2]
        print("AOC15_1: Result: " + str(self.round * sumHP))
        print("Time taken: " + str(time.time() - now))

    def AOC15_2(self):
        now = time.time()

        print("AOC15_2: ")
        print("Time taken: " + str(time.time() - now))

#aoc15 = AOC15.AOC15("Inputs/AOC15_1.txt")
#aoc15 = AOC15.AOC15("Test/AOC15_1.txt")
aoc15 = AOC15(r"C:\Users\michelle\python\AOC2018-master\AdventOfCode2018\Test\AOC15_1.txt")
aoc15.AOC15_1()
#aoc15.AOC15_2()
del aoc15