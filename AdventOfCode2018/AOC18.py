import time
import Functs

class AOC18:
    filePath = ""
    lines = []

    def __init__(self, filePath):
        self.filePath = filePath
        self.lines = Functs.importFile(filePath)

    def print(self):
        for l in self.lines:
            print(l)
        print()

    def run(self):
        nLines = []
        yl = len(self.lines)
        for y in range(yl):
            nl = "" #New line
            xl = len(self.lines[y])
            for x in range(xl):
                nb = [[x-1,y-1], [x,y-1], [x+1,y-1], [x-1,y], [x+1,y], [x-1,y+1], [x,y+1], [x+1,y+1]] #Neighbours coords
                nv = "" #Neighbours values
                for i in range(len(nb)):
                    if nb[i][0] >= 0 and nb[i][0] < xl and nb[i][1] >= 0 and nb[i][1] < yl:
                        nv += self.lines[nb[i][1]][nb[i][0]]
                val = self.lines[y][x]
                #print(str(x) + " " + str(y) + " " + str(val) + " " + nv)
                if val == ".":
                    if nv.count("|") >= 3:
                        nl += "|"
                    else:
                        nl += "."
                elif val == "|":
                    if nv.count("#") >= 3:
                        nl += "#"
                    else:
                        nl += "|"
                elif val == "#":
                    if nv.count("#") >= 1 and nv.count("|") >= 1:
                        nl += "#"
                    else:
                        nl += "."
            nLines.append(nl)
        self.lines = nLines
        #self.print()

    def AOC18_1(self):
        now = time.time()

        for ll in range(len(self.lines)):
            self.lines[ll] = self.lines[ll].rstrip()

        #self.print()
        for j in range(10):
            self.run()

        wt = 0
        lt = 0
        for k in self.lines:
            wt += k.count("|")
            lt += k.count("#")
        #print(wt)
        #print(lt)
        print("AOC18_1: Result: " + str(wt * lt))
        print("Time taken: " + str(time.time() - now))

    #Need to look for a loop in the data
    def AOC18_2(self):
        now = time.time()
        self.lines = Functs.importFile(self.filePath) #Reinitialise
        ans = []
        loop = []
        ls = 0 #Loop Start
        for j in range(10000):
            self.run()
            wt = 0
            lt = 0
            for k in self.lines:
                wt += k.count("|")
                lt += k.count("#")
            ans.append([wt,lt])
            if ans.count([wt,lt]) == 3:
                loop.append([wt,lt])
            elif ans.count([wt,lt]) == 4:
                ls = j
                break
        i = (1000000000 - ls - 1) % len(loop)
        print("AOC18_2: Result: " + str(loop[i][0] * loop[i][1]))
        print("Time taken: " + str(time.time() - now))
