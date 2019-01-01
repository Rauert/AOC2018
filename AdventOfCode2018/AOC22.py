#depth: 6969
#target: 9,796

import time

class AOC22:
    depth = 0
    target = [0,0]
    el = [] #Erosion level
    gi = [] #Geological Index

    def __init__(self, test):
        if test == True:
            self.depth = 510
            self.target = [10,10]
        else:
            self.depth = 6969
            self.target = [9,796]
        self.el = [[0 for x in range(self.target[0]+1)] for y in range(self.target[1]+1)]
        self.gi = [["." for x in range(self.target[0]+1)] for y in range(self.target[1]+1)]

    def print(self):
        for i in self.gi:
            print("".join(i))

    def AOC22_1(self):
        now = time.time()
        types = [".","=","|"]
        count = 0
        for y in range(self.target[1]+1):
            for x in range(self.target[0]+1):
                if (x == 0 and y == 0) or (x == self.target[0] and y == self.target[1]):
                    self.el[y][x] = self.depth % 20183
                elif y == 0:
                    self.el[y][x] = ((x * 16807) + self.depth) % 20183
                elif x == 0:
                    self.el[y][x] = ((y * 48271) + self.depth) % 20183
                else:
                    self.el[y][x] = ((self.el[y][x-1] * self.el[y-1][x]) + self.depth) % 20183
                gi = self.el[y][x] % 3
                count += gi
                self.gi[y][x] = types[gi]

        self.print()
        print("AOC22_1: Result:", count)
        print("Time taken: " + str(time.time() - now))


    def AOC22_2(self):
        now = time.time()

 
        print("AOC22_2: Result:")
        print("Time taken: " + str(time.time() - now))
