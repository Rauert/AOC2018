import time
import Functs
import re

class AOC23:
    lines = []
    data = []

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
