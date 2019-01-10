import time
import Functs

class AOC15:
    lines = []
    out = []
    #vs = []
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

    def bfs(self, c1, c2, coords):
        #https://stackoverflow.com/questions/20583878/python-check-if-coordinates-of-values-in-a-grid-connect-to-one-another
        def neighbours(cc):
            candidates = [(cc[0] - 1, cc[1]), (cc[0] + 1, cc[1]), (cc[0], cc[1] - 1), (cc[0], cc[1] + 1)]
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

    def combat(self, lines, vs, u):
        targetsRemain = True
        #Mortal Kombat!!
        while targetsRemain == True:
            for i in u:
                #self.print(u)
                if i[3] != "d":
                    #scan for targets
                    t = []
                    ti = [] #Target index
                    e = "e"
                    if i[3] == "e":
                        e = "g"
                    for j in u:
                        if i != j and j[3] == e:
                            t.append([j[0],j[1]])
                            ti.append(u.index(j))
                    if len(t) == 0:
                        targetsRemain = False
                        return
                    #Can attack?
                    attacked = False
                    vt = [] #Valid Targets
                    t = sorted(t , key=lambda k: [k[1], k[0]])
                    aj = [[i[0]+1,i[1]],[i[0]-1,i[1]],[i[0],i[1]+1],[i[0],i[1]-1]] #Adjacent cells
                    for a in range(3,0,-1):
                        if aj[a] not in vs: #Invalid location
                            del aj[a]
                    for T in t:
                        if T in aj:
                            vt.append(u[ti[t.index(T)]])
                    print(vt)
                    print(u)
                    if len(vt) > 0:
                        attacked = True
                        ii = u.index(vt[0])
                        if len(vt) > 1:
                            lowHP = 201
                            for jj in range(len(vt)-1,0,-1):
                                if vt[jj][2] <= 201:
                                    lowHP = vt[jj][2]
                                    ii = u.index(vt[jj])
                        u[ii][2] -= 3
                        if u[ii][2] <= 0:
                            u[ii][3] = "d"
                    #Else move
                    if attacked == False:
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
                                if jj in vs and jj not in ob: #Within a valid cell (Not a wall or elf/goblin)
                                    ra.append(jj)
                        #Reachable? (Path simulation)
                        if len(ra) > 0:
                            for kk in range(len(ra)-1,0,-1):
                                if self.bfs((i[0],
                                             i[1]),
                                            ra[kk],
                                            [item for item in vs if item not in ob]) == False: ####Error cant use - on lists of lists
                                    del ra[kk]
                        #Pick closest
                        closest = ra[len(ra)-1]
                        dist = abs(i[0]- closest[0]) + abs(i[1]- closest[1])
                        for ii in range(len(ra)-1,0,-1):
                            cDist = abs(i[0]- ra[ii][0]) + abs(i[1]- ra[ii][1])
                            if cDist <= dist:
                                dist = cDist
                                closest = ra[ii]
                        #Move
                        if len(aj) > 0:
                            if len(aj) == 1:
                                u[1][0] = aj[0][0]
                                u[1][1] = aj[0][1]
                            else:
                                movePos = aj[len(aj)-1]
                                moveDist = abs(movePos[0]- closest[0]) + abs(movePos[1]- closest[1])
                                for iii in range(len(aj)-1,0,-1):
                                    cMDist = abs(aj[iii][0]- closest[0]) + abs(aj[iii][1]- closest[1])
                                    if cMDist <= moveDist:
                                        moveDist = cMDist
                                        movePos = aj[iii]
                                u[1][0] = movePos[0]
                                u[1][1] = movePos[1]
            self.round += 1
            u = sorted(u , key=lambda k: [k[1], k[0]]) #Ensures reading order is maintained
            self.print(u)

    def setup(self):
        vs = []
        u = []
        for y in range(len(self.lines)):
            for x in range(len(self.lines[y])):
                val = self.lines[y][x]
                if val == ".":
                    vs.append([x,y])
                elif val == "E":
                    vs.append([x,y])
                    u.append([x,y,200,"e"])
                elif val == "G":
                    vs.append([x,y])
                    u.append([x,y,200,"g"])
        return u,vs

    def AOC15_1(self):
        now = time.time()
        lines = self.lines
        #vs = []
        #u = []

        #Setup
        u,vs = self.setup()

        self.out = self.lines.copy()
        for l in range(len(self.out)):
            self.out[l] = self.out[l].replace("E",".")
            self.out[l] = self.out[l].replace("G",".")

        #look up/down/left/right for enemy, attack if there
        #Else scan for targets, if targets any still alive, find adjacent locations
        #for nearest to farthest.
        #   Check if reachable
        #   Find for shortest path/s
        #   Make step

        self.print(u)
        self.combat(lines, vs, u)

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