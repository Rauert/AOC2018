import time
import Functs
import re

class AOC10:
    inFile = ""
    lines = []
    mCo = []

    def __init__(self, filePath):
        self.inFile = filePath
        self.lines = Functs.importFile(self.inFile)

    def mCoExists(self, x, y):
        rtn = False
        for i in range(0,len(self.mCo),4):
            if x == self.mCo[i] and y == self.mCo[i+1]:
                rtn = True
        return rtn

    def AOC10(self):
        now = time.time()
        inRange = False
        running = True
        count = 0 #Of seconds

        #Create list of master coords and velocity
        for l in self.lines:
            c = re.split("position=<\s+|position=<|,\s+|>\s+velocity=<\s+|>\s+velocity=<|>\n", l)
            self.mCo.append(int(c[1]))
            self.mCo.append(int(c[2]))
            self.mCo.append(int(c[3]))
            self.mCo.append(int(c[4]))
        
        while running == True:
            max = 0
            count += 1
            for i in range(0,len(self.mCo),4):
                #Iterate each coord
                self.mCo[i] += self.mCo[i+2]
                self.mCo[i+1] += self.mCo[i+3]

                #Test if coords are close to one another sing manhatten distance
                val = abs(self.mCo[0] - self.mCo[i]) + abs(self.mCo[1] - self.mCo[i+1])
                if val > max:
                    max = val

            #Print if coords are close to one another.
            if max < 100:
                inRange = True
                #Find coord range
                x = maxX = self.mCo[0]
                y = maxY = self.mCo[1]
                for i in range(4,len(self.mCo),4):
                    if self.mCo[i] < x:
                        x = self.mCo[i]
                    if self.mCo[i] > maxX:
                        maxX = self.mCo[i]
                    if self.mCo[i+1] < y:
                        y = self.mCo[i+1]
                    if self.mCo[i+1] > maxY:
                        maxY = self.mCo[i+1]
                #Print
                for yi in range(y, maxY+1):
                    for xi in range(x, maxX+1):
                        if self.mCoExists(xi, yi) == True:
                            print("#", end=" ")
                        else:
                            print(".", end=" ")
                    print()
                print()
                print("Time elapsed: " + str(count))
                print()
            else:
                if inRange == True:
                    running = False

        print("Time taken: " + str(time.time() - now))

