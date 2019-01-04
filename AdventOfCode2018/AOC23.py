import time
import Functs
import re

class AOC23:
    lines = []
    data = []
    best = [0,0,0]

    def __init__(self, filePath):
        self.lines = Functs.importFile(filePath)


    def AOC23_1(self):
        now = time.time()

        for l in self.lines:
            max = 0
            maxI = 0
            tmp = re.split(",|>,\sr=", l.rstrip()[5:])
            self.data.append([int(tmp[0]),int(tmp[1]),int(tmp[2]),int(tmp[3])])

        for d in range(len(self.data)):
            if self.data[d][3] > max:
                max = self.data[d][3]
                maxI = d

        maxX = self.data[maxI][0]
        maxY = self.data[maxI][1]
        maxZ = self.data[maxI][2]

        count = 0
        for i in self.data:
            if abs(maxX - i[0]) + abs(maxY - i[1]) + abs(maxZ - i[2]) <= max:
                count += 1

        print("AOC23_1: Result:", count)
        print("Time taken: " + str(time.time() - now))

    def reduce(self, factor):
        dataR = []
        for d in self.data:
            dataR.append([int(d[0]/factor),int(d[1]/factor),int(d[2]/factor),int(d[3]/factor)])
            #print(dataR[-1])
        return dataR

    def AOC23_2(self):
        now = time.time()
        factor = 1000000

        #for _ in range(7):
        dataR = self.reduce(factor)
        self.best = [self.best[0]*10,self.best[1]*10,self.best[2]*10]
        best = []
        max = -1

        for z in range(-100,100):
            print(z)
            for y in range(-100,100):
                for x in range(-100,100):
                    count = 0
                    for r in dataR:
                        #print(x,y,z,(abs(r[0] - (self.best[0]+x)) + abs(r[1] - (self.best[1]+y)) + abs(r[2] - (self.best[2]+z))) - r[3])
                        if (abs(r[0] - (self.best[0]+x)) + abs(r[1] - (self.best[1]+y)) + abs(r[2] - (self.best[2]+z))) - r[3] <= 0:
                            count += 1
                    if count > max:
                        max = count
                        best = [x,y,z]
        
        print(best, max)
        self.best = best
        factor = factor / 10

        print("AOC23_2: Result:", self.best)
        print("Time taken: " + str(time.time() - now))