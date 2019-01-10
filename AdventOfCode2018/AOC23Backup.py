import time
import Functs
import math
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

        #self.data.clear()
        ##"pos=<10,12,12>, r=2"
        ##"pos=<12,14,12>, r=2"
        ##"pos=<16,12,12>, r=4"
        ##"pos=<14,14,14>, r=6"
        ##"pos=<50,50,50>, r=200"
        ##"pos=<10,10,10>, r=5"
        #self.data.append([10,12,12,2])
        #self.data.append([12,14,12,2])
        #self.data.append([16,12,12,4])
        #self.data.append([14,14,14,6])
        #self.data.append([50,50,50,200])
        #self.data.append([10,10,10,5])

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

    #https://stackoverflow.com/questions/5254838/calculating-distance-between-a-point-and-a-rectangular-box-nearest-point
    def distance(self, cube, p):
        dx = max(cube[0] - p[0], 0, p[0] - cube[1]) #MinX, 0, maxX
        dy = max(cube[2] - p[1], 0, p[1] - cube[3])
        dz = max(cube[4] - p[2], 0, p[2] - cube[5])
        #if cube[1] - cube[0] <= 1:
        #    print(cube, p, math.sqrt(dx*dx + dy*dy + dz*dz), (abs(cube[0] - p[0]) + abs(cube[2] - p[1]) + abs(cube[4] - p[2])))
        #    x = (cube[0]+cube[1])/2
        #    y = (cube[2]+cube[3])/2
        #    z = (cube[4]+cube[5])/2
        #    ddx = max(abs(p[0] - x) - (cube[1]-cube[0]) / 2, 0)
        #    ddy = max(abs(p[1] - y) - (cube[3]-cube[2]) / 2, 0)
        #    ddz = max(abs(p[2] - z) - (cube[5]-cube[4]) / 2, 0)
        #    print(math.sqrt(dx*dx + dy*dy + dz*dz))
        return math.sqrt(dx*dx + dy*dy + dz*dz)

    #Subdivide area into 8 cubes, select best, repeat
    def AOC23_2A(self):
        now = time.time()

        minX = min(x[0] for x in self.data)
        maxX = max(x[0] for x in self.data)
        minY = min(x[1] for x in self.data)
        maxY = max(x[1] for x in self.data)
        minZ = min(x[2] for x in self.data)
        maxZ = max(x[2] for x in self.data)
        overallBest = [[minX, maxX, minY, maxY, minZ, maxZ]]
        #if ((abs(minX)+abs(maxX)) % 2) == 1: minX -= 1
        #if ((abs(minY)+abs(maxY)) % 2) == 1: minY -= 1
        #if ((abs(minZ)+abs(maxZ)) % 2) == 1: minZ -= 1

        #while (abs(overallBest[0][1]-overallBest[0][0]))*(abs(overallBest[0][3]-overallBest[0][2]))*(abs(overallBest[0][5]-overallBest[0][4])) != 1:
        while overallBest[0][1] != overallBest[0][0] and overallBest[0][3] != overallBest[0][2] and overallBest[0][5] != overallBest[0][4]:
            best = []
            for b in overallBest:
                maxi = 0
                minX = b[0]
                maxX = b[1]
                minY = b[2]
                maxY = b[3]
                minZ = b[4]
                maxZ = b[5]
                midX = int((minX+maxX)/2)
                midY = int((minY+maxY)/2)
                midZ = int((minZ+maxZ)/2)
                print("Volume:", (abs(maxX-minX))*(abs(maxY-minY))*(abs(maxZ-minZ)))
                #print(minX, midX, maxX, minY, midY, maxY, minZ, midZ, maxZ)
                cubes = [[minX,midX,minY,midY,minZ,midZ],[midX+1,maxX,minY,midY,minZ,midZ],
                         [minX,midX,minY,midY,midZ+1,maxZ],[midX+1,maxX,minY,midY,midZ+1,maxZ],
                         [minX,midX,midY+1,maxY,minZ,midZ],[midX+1,maxX,midY+1,maxY,minZ,midZ],
                         [minX,midX,midY+1,maxY,midZ+1,maxZ],[midX+1,maxX,midY+1,maxY,midZ+1,maxZ]]
                for c in cubes:
                    count = 0
                    for p in self.data:
                        if self.distance(c, p) - p[3] <=0: #Check if bot in range of cube
                            count += 1
                    #print(c, count)
                    if count != 0 and count == maxi and self.distance(c,[0,0,0,0]) < self.distance(best[0],[0,0,0,0]):
                        best.clear()
                        best.append(c)
                    elif count > maxi:
                        maxi = count
                        best.clear()
                        best.append(c)
            overallBest = best

        #for z in range(-100,100):
            #print(z)
            #for y in range(-100,100):
                #for x in range(-100,100):
                    #count = 0

        print("AOC23_2: Result:", overallBest[0], maxi, abs(overallBest[0][0])+abs(overallBest[0][2])+abs(overallBest[0][4]))
        print("Time taken: " + str(time.time() - now))

    #Very Slow and wrong answer.
    #Divide dataset by 1m, find best point 100 distance around 0,0,0
    #Divide by 100000, find best point 100 distance around best point from aove, etc, etc
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

    def testPoint(self,x,y,z):
        count = 0
        for i in self.data:
            if math.sqrt((x - i[0])*(x - i[0]) + (y - i[1])*(y - i[1]) + (z - i[2])*(z - i[2])) <= i[3]:
                count += 1
        print(count)

#aoc = AOC23.AOC23("Inputs/AOC23_1.txt")
aoc = AOC23(r"C:\Users\michelle\python\AOC2018-master\AdventOfCode2018\Inputs\AOC23_1.txt")
aoc.AOC23_1()
aoc.testPoint(11353177, 58282550, 21041575)
aoc.AOC23_2A()
del aoc