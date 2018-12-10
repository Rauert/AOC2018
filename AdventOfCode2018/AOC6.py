import time
import Functs
import re
import math

class AOC6:
    inFile = ""
    lines = []
    co = [[0 for x in range(2)] for y in range(2)] 
    mCo = []
    areas = {}

    def __init__(self, filePath):
        self.inFile = filePath
        self.lines = Functs.importFile(self.inFile)

    def mCoExists(self, x, y):
        rtn = False
        for i in range(0,len(self.mCo),2):
            if x == self.mCo[i] and y == self.mCo[i+1]:
                rtn = True
        return rtn

    def AOC6_1(self):
        now = time.time()
        maxC = 0
        #Create list of master coords and size of grid
        for l in self.lines:
            c = re.split(", |\n", l)
            #self.co = int(c[0])
            self.mCo.append(int(c[0]))
            if int(c[0]) > maxC:
                maxC = int(c[0])
            #self.co = int(c[1])
            self.mCo.append(int(c[1]))
            if int(c[1]) > maxC:
                maxC = int(c[1])
        maxC = maxC + 1
        self.co = [[0 for x in range(maxC)] for y in range(maxC)] 

        #Calc Manhatten distance of each x,y in grid
        for y in range(maxC):
            for x in range(maxC):
                if self.mCoExists(x, y) == True: #Alternatively just set val = 0 to x,y
                    self.co[x][y] = str(x) + ',' + str(y)
                else:
                    lVal = 100000
                    for i in range(0,len(self.mCo),2):
                        #print(i)
                        val = abs(x - self.mCo[i]) + abs(y - self.mCo[i+1])
                        #print(str(x) + "," + str(y) + ": " + str(self.mCo[i]) + "," + str(self.mCo[i+1]) + ": " + str(val))
                        if val < lVal:
                            lVal = val
                            #print(str(self.mCo[i]) + "," + str(self.mCo[i+1]) + "i")
                            self.co[x][y] = str(self.mCo[i]) + "," + str(self.mCo[i+1]) + "i"
                        elif val == lVal:
                            self.co[x][y] = '.'
                    #Compare w/ all mCo, Assign lowest value, if equal then .
        #for y in range(maxC):
        #    for x in range(maxC):
        #        print(self.co[x][y], end=' ')
        #    print()

        #Find areas
        for y in range(maxC):
            for x in range(maxC):
                val = self.co[x][y]
                if val[len(val)-1:len(val)] == "i":
                    if val[0:len(val)-1] in self.areas:
                        self.areas[val[0:len(val)-1]] = self.areas.get(val[0:len(val)-1]) + 1
                    else:
                        self.areas[val[0:len(val)-1]] = 1
                elif len(val) > 1:
                    if val in self.areas:
                        self.areas[val] = self.areas.get(val) + 1
                    else:
                        self.areas[val] = 1

        ##Find and remove areas that extend to infinity
        #for y in range(maxC):
        #    for x in range(maxC):
        #        infinite = false
        #        val = self.co[x][y]
        #        #Test up, down, right, left

        for y in range(maxC):
            val = self.co[0][y]
            if val[len(val)-1:len(val)] == "i":
                if val[0:len(val)-1] in self.areas:
                    del self.areas[val[0:len(val)-1]]
            elif len(val) > 1:
                if val in self.areas:
                    del self.areas[val]
            val = self.co[maxC-1][y]
            if val[len(val)-1:len(val)] == "i":
                if val[0:len(val)-1] in self.areas:
                    del self.areas[val[0:len(val)-1]]
            elif len(val) > 1:
                if val in self.areas:
                    del self.areas[val]
        for x in range(maxC):
            val = self.co[x][0]
            if val[len(val)-1:len(val)] == "i":
                if val[0:len(val)-1] in self.areas:
                    del self.areas[val[0:len(val)-1]]
            elif len(val) > 1:
                if val in self.areas:
                    del self.areas[val]
            val = self.co[x][maxC-1]
            if val[len(val)-1:len(val)] == "i":
                if val[0:len(val)-1] in self.areas:
                    del self.areas[val[0:len(val)-1]]
            elif len(val) > 1:
                if val in self.areas:
                    del self.areas[val]
        #Find largest area
        largest = 0
        for a,v in self.areas.items():
            #print(a + "->" + str(v))
            if v > largest:
                largest = v

        print("AOC6_1: Result: " + str(largest))
        print("Time taken: " + str(time.time() - now))

    def AOC6_2(self):
        now = time.time()
        max = 10000
        #max = 32 #Testing
        tot = 0
        maxC = len(self.co[0])
        for y in range(maxC):
            for x in range(maxC):
                sum = 0
                for i in range(0,len(self.mCo),2):
                    sum += abs(x - self.mCo[i]) + abs(y - self.mCo[i+1])
                if sum < max:
                    tot += 1
        print("AOC6_2: " + str(tot))
        print("Time taken: " + str(time.time() - now))

