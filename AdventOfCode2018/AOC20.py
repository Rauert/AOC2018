import time
import Functs

class AOC20:
    r = "" #Route
    test = ["^WNE$","^N(E|W)N$","^ENWWW(NEEE|SSE(EE|N))$","^ENNWSWW(NEWS|)SSSEEN(WNSE|)EE(SWEN|)NNN$","^ESSWWN(E|NNENN(EESS(WNSE|)SSS|WWWSSSSE(SW|NNNE)))$", "^WSSEESWWWNW(S|NENNEEEENN(ESSSSW(NWSW|SSEN)|WSWWN(E|WWS(E|SS))))$"]
    g = [] #Grid
    fR = [] #Farthest Room
    doors = 0 #Doors to farthest room
    dist = {(0, 0): 0}

    def __init__(self, filePath):
        self.r = Functs.importFile(filePath)[0].rstrip()

    def count(self):
        sum = 0
        for g in self.g:
            sum += ''.join(g).count(".")
        print(sum)

    def print(self):
        for g in self.g:
            s = ''.join(g).replace("?","#").replace(" ","")
            if len(s) > 0:
                print(s)

    #Check if farthest room 
    def chkDistance(self,x,y,dist):
        if dist > self.doors:
            self.doors = dist
            self.fR = [x,y]

    #Create new room
    def addRoom(self,x,y):
        self.g[y][x] = "."
        if self.g[y][x-1] == " ": self.g[y][x-1] = "?"
        if self.g[y][x+1] == " ": self.g[y][x+1] = "?"
        if self.g[y+1][x] == " ": self.g[y+1][x] = "?"
        if self.g[y-1][x] == " ": self.g[y-1][x] = "?"
        self.g[y-1][x-1] = "#"
        self.g[y-1][x+1] = "#"
        self.g[y+1][x-1] = "#"
        self.g[y+1][x+1] = "#"

    def runA(self,i,x,y,dist,path):
        while self.r[i] in "NSWE":
            if self.r[i] == "N":
                y -= 2
                self.g[y+1][x] = "-"
            elif self.r[i] == "S":
                y += 2
                self.g[y-1][x] = "-"
            elif self.r[i] == "W":
                x -= 2
                self.g[y][x+1] = "|"
            elif self.r[i] == "E":
                x += 2
                self.g[y][x-1] = "|"
            self.addRoom(x,y)
            dist += 1
            #self.chkDistance(x,y,dist)
            if (x, y) not in self.dist or dist < self.dist[(x, y)]:
                    self.dist[(x, y)] = dist
            path += self.r[i]
            i += 1
        if self.r[i] == "$": #End of route
            print(path)
            self.count()
            return #end sub
        elif self.r[i] == "(": #Beginning of branch. Need to find start i of each branch and resumption point (i after ")"). Spin up new self.run for each branch.
            branchs = [i+1]
            endVal = 0
            depth = 0
            j = i
            j += 2
            while True:
                if depth == 0 and self.r[j] == ")":
                    endVal = j+1
                    break
                elif depth == 0 and self.r[j] == "|":
                    if self.r[j+1] == ")":
                        branchs.append(j+2)
                    else:
                        branchs.append(j+1)
                elif self.r[j] == "(":
                    depth += 1
                elif self.r[j] == ")":
                    depth -= 1
                j += 1
            #print(i,branchs, endVal)
            for b in branchs:
                if b == endVal:
                    self.runA(endVal,x,y,dist,path)
                else:
                    self.runA(b,x,y,dist,path)
        elif self.r[i] == "|" or self.r[i] == ")": #End of this option for this route
            return

    #Super slow
    #Covers same ground over and over. Misunderstanding of question. Presumed each branch creates x new paths each resuming after ).
    def run(self,i,x,y,dist,resumption: list, path):
        while self.r[i] in "NSWE":
            if self.r[i] == "N":
                y -= 2
                self.g[y+1][x] = "-"
            elif self.r[i] == "S":
                y += 2
                self.g[y-1][x] = "-"
            elif self.r[i] == "W":
                x -= 2
                self.g[y][x+1] = "|"
            elif self.r[i] == "E":
                x += 2
                self.g[y][x-1] = "|"
            self.addRoom(x,y)
            dist += 1
            self.chkDistance(x,y,dist)
            path += self.r[i]
            i += 1
        if self.r[i] == "$": #End of route
            if len(resumption) == 0:
                print(path)
                self.count()
                return #end sub
            else:
                print("ERROR", resumption) #Shouldnt run
                print(path)
        elif self.r[i] == "(": #Beginning of branch. Need to find start i of each branch and resumption point (i after ")"). Spin up new self.run for each branch.
            branchs = [i+1]
            endVal = 0
            depth = 0
            j = i
            j += 2
            while True:
                if depth == 0 and self.r[j] == ")":
                    endVal = j+1
                    break
                elif depth == 0 and self.r[j] == "|":
                    if self.r[j+1] == ")":
                        branchs.append(j+2)
                    else:
                        branchs.append(j+1)
                elif self.r[j] == "(":
                    depth += 1
                elif self.r[j] == ")":
                    depth -= 1
                j += 1
            #print(i,branchs, endVal)
            for b in branchs:
                if b == endVal:
                    self.run(endVal,x,y,dist,resumption,path)
                else:
                    nResumption = resumption
                    nResumption.append(endVal)
                    self.run(b,x,y,dist,nResumption,path)
        elif self.r[i] == "|" or self.r[i] == ")": #End of this option for this route
            if len(resumption) != 0:
                nextI = resumption.pop()
                self.count()
                self.run(nextI,x,y,dist,resumption,path)
            #else:
                #print("Partial:",path)
                #self.run(i+1,x,y,dist,resumption,path) #Causing logic error

    def AOC20_1A(self, test:bool):
        print()
        #Build graph using coords and {}. OR store in [] - [[x,y,[Connections]],] May have to maintain list of [[x,y],] as well.
        #Start at 0,0
        #Then depth first to find path.

    #From reddit: nightcoder01\
    def AOC20_1S(self):
        grid = {(0, 0): 0}
        dist = x = y = 0
        stack = []

        #for char in open('Inputs/AOC20_1.txt').read()[1:-1]:
        for char in self.test[3][1:-1]: #"^ENNWSWW(NEWS|)SSSEEN(WNSE|)EE(SWEN|)NNN$"
            if char == '(':
                stack.append((dist, x, y))
            elif char == ')':
                dist, x, y = stack.pop()
            elif char == '|':
                dist, x, y = stack[-1]
            else:
                x += (char == 'E') - (char == 'W')
                y += (char == 'S') - (char == 'N')
                dist += 1
                if (x, y) not in grid or dist < grid[(x, y)]:
                    grid[(x, y)] = dist
            
        print('ans (part 1): %d' % max(grid.values()))
        print('ans (part 2): %d' % sum(value >= 1000 for value in grid.values()))

    def AOC20(self, test:bool):
        now = time.time()
        if test == True:
            self.r = self.test[5]
        size = len(self.r.replace("^","").replace("$","").replace("(","").replace(")","").replace("|",""))
        #size *= 2
        x = y = size
        size *= 2
        self.g = [[" " for y in range(size)] for x in range(size)]
        self.dist = {(x, y): 0}

        #Initialise
        self.addRoom(x,y)
        self.g[y][x] = "X"

        self.runA(1,x,y,0,"")
        maxX, maxY = max(self.dist, key=self.dist.get)
        self.g[maxY][maxX] = "F"
        #self.g[self.fR[1]][self.fR[0]] = "F"

        #print(maxX, maxY)
        #print(self.dist)
        self.print()
        print("AOC20_1: Result: ",max(self.dist.values()))
        print("AOC20_2: Result: ",sum(value >= 1000 for value in self.dist.values()))
        print("Time taken: " + str(time.time() - now))

