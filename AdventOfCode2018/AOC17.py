import time
import Functs
import re
import sys

class AOC17:
    lines = []
    data = []
    grid = []
    maxY = 0
    maxX = 0
    total = -1
    q = []

    def __init__(self, filePath):
        self.lines = Functs.importFile(filePath)

    def print(self):
        for g in self.grid:
            print(''.join(g))

    #Recursive solution
    def falling(self, x , y):
        #print(x,y)
        #self.print()
        self.grid[y][x] = "|"
        while y+1 != self.maxY and (self.grid[y+1][x] == "." or self.grid[y+1][x] == "|"):
            y += 1
            self.grid[y][x] = "|"
        if y+1 != self.maxY:
            rb = False
            lb = False
            startX = x
            while (self.grid[y][x+1] == "." or self.grid[y][x+1] == "|") and (self.grid[y+1][x] == "~" or self.grid[y+1][x] == "#"):
                x += 1
                self.grid[y][x] = "|"
            if self.grid[y+1][x] == "." or self.grid[y+1][x] == "|":
                self.falling(x,y+1)
            elif self.grid[y][x+1] == "#": rb = True

            x = startX
            while (self.grid[y][x-1] == "." or self.grid[y][x-1] == "|") and (self.grid[y+1][x] == "~" or self.grid[y+1][x] == "#"):
                x -= 1
                self.grid[y][x] = "|"
            if self.grid[y+1][x] == "." or self.grid[y+1][x] == "|":
                self.falling(x,y+1)
            elif self.grid[y][x-1] == "#": lb = True

            if rb == True and lb == True:
                while self.grid[y][x] != "#":
                    self.grid[y][x] = "~"
                    x += 1
                self.falling(500,1)

    def run(self,x,y):
        #print(x,y)
        #self.print()
        self.grid[y][x] = "|"
        while y+1 != self.maxY and (self.grid[y+1][x] == "." or self.grid[y+1][x] == "|"):
            y += 1
            self.grid[y][x] = "|"
        if y+1 != self.maxY:
            rb = False
            lb = False
            startX = x
           #while (self.grid[y][x+1] == "." or self.grid[y][x+1] == "|") and (self.grid[y+1][x] == "~" or self.grid[y+1][x] == "#"):
            while (self.grid[y][x+1] == "." or self.grid[y][x+1] == "|" or self.grid[y][x+1] == "~") and (self.grid[y+1][x] == "~" or self.grid[y+1][x] == "#"):
                x += 1
                self.grid[y][x] = "|"
            if self.grid[y+1][x] == "." or self.grid[y+1][x] == "|":
                #self.q.append([x,y+1])
                self.q.append([x,y])
            elif self.grid[y][x+1] == "#": rb = True

            x = startX
            #while (self.grid[y][x-1] == "." or self.grid[y][x-1] == "|") and (self.grid[y+1][x] == "~" or self.grid[y+1][x] == "#"):
            while (self.grid[y][x-1] == "." or self.grid[y][x-1] == "|" or self.grid[y][x-1] == "~") and (self.grid[y+1][x] == "~" or self.grid[y+1][x] == "#"):
                x -= 1
                self.grid[y][x] = "|"
            if self.grid[y+1][x] == "." or self.grid[y+1][x] == "|":
                #self.q.append([x,y+1])
                self.q.append([x,y])
            elif self.grid[y][x-1] == "#": lb = True

            if rb == True and lb == True:
                while self.grid[y][x] != "#":
                    self.grid[y][x] = "~"
                    x += 1
                self.q.append([500,1])

    def count(self):
        sum = 0
        rtn = False
        for y in self.grid:
            for x in y:
                if x == "~" or x == "|":
                    sum += 1
        if sum == self.total: rtn = True
        self.total = sum
        return True

    def AOC17_1(self):
        now = time.time()

        for l in self.lines:
            tmp = re.split(",\s|=|\.\.", l.rstrip())
            self.data.append([tmp[0],int(tmp[1]),int(tmp[3]),int(tmp[4])])

        for d in self.data:
            if d[0] == "x":
                if d[1] > self.maxX: self.maxX = d[1]
                if d[2] > self.maxY: self.maxY = d[2]
                if d[3] > self.maxY: self.maxY = d[3]
            else:
                if d[1] > self.maxY: self.maxY = d[1]
                if d[2] > self.maxX: self.maxX = d[2]
                if d[3] > self.maxX: self.maxX = d[3]
        self.maxX += 1
        self.maxY += 1
        self.grid = [["." for x in range(self.maxX)] for y in range(self.maxY)]
        self.grid[0][500] = "+"

        for d in self.data:
            if d[0] == "x":
                x = d[1]
                for y in range(d[2],d[3]+1):
                    self.grid[y][x] = "#"
            else:
                y = d[1]
                for x in range(d[2],d[3]+1):
                    self.grid[y][x] = "#"
        #sys.setrecursionlimit(1500)
        #self.falling(500,1)
        #self.print()
        self.q.append([500,1])
        while len(self.q)>0:
            xy = self.q.pop(0)
            self.run(xy[0],xy[1])
            #self.print()
        sum = 0
        for y in self.grid:
            for x in y:
                if x == "~" or x == "|":
                    sum += 1
        self.print()
        print("AOC17_1: Result:", sum)
        print("Time taken: " + str(time.time() - now))

    def AOC17_2(self):
        now = time.time()
 
        print("AOC17_2: Result: ")
        print("Time taken: " + str(time.time() - now))
