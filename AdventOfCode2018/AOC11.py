import time
import Functs

class AOC11:
    sr = 0
    co = [[0 for x in range(301)] for y in range(301)] 

    def __init__(self, inSR):
        self.sr = inSR

    def AOC11_1(self):
        now = time.time()

        #Calc power level for each coord
        for y in range(1, 301):
            for x in range(1, 301):
                val = str((((x + 10) * y) + self.sr) * (x + 10))
                if len(val) > 2:
                    self.co[x][y] = int(val[len(val)-3:len(val)-2]) - 5
                else:
                    self.co[x][y] = -5

        #Find 3x3 grid section with most power
        largest = 0
        larX = 0
        larY = 0
        for y in range(2,300):
            for x in range(2,300):
                val = self.co[x-1][y-1] + self.co[x][y-1] + self.co[x+1][y-1] + self.co[x-1][y] + self.co[x][y] + self.co[x+1][y] + self.co[x-1][y+1] + self.co[x][y+1] + self.co[x+1][y+1]
                if val > largest:
                    largest = val
                    larX = x-1
                    larY = y-1
        print("AOC11_1: Result: " + str(largest) + " " + str(larX) + "," + str(larY))
        print("Time taken: " + str(time.time() - now))

    def AOC11_2(self):
        now = time.time()
        largest = 0
        larX = 0
        larY = 0
        larS = 0

        for s in range(1,301): #Grid size
            for y in range(1,302-s):
                for x in range(1,302-s):
                    val = 0
                    for b in range(s):
                        for a in range(s):
                            val += self.co[x+a][y+b]
                    if val > largest:
                        largest = val
                        larX = x
                        larY = y
                        larS = s
            print(s)
            print("Largest: " + str(largest) + " " + str(larX) + "," + str(larY) + "," + str(larS))
        print("AOC11_2: " + str(largest) + " " + str(larX) + "," + str(larY) + "," + str(larS))
        print("Time taken: " + str(time.time() - now))

