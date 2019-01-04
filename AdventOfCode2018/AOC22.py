#depth: 6969
#target: 9,796

import time

class AOC22:
    depth = 0
    target = [0,0]
    el = [] #Erosion level
    gi = [] #Geological Index
    giv = [] #GI value

    def __init__(self, test):
        if test == True:
            self.depth = 510
            self.target = [10,10]
        else:
            self.depth = 6969
            self.target = [9,796]
        self.el = [[0 for x in range(self.target[0]+100)] for y in range(self.target[1]+100)]
        self.gi = [["." for x in range(self.target[0]+100)] for y in range(self.target[1]+100)]
        self.giv = [[0 for x in range(self.target[0]+100)] for y in range(self.target[1]+100)]

    def print(self):
        for i in self.gi:
            print("".join(i))
        print()
        for i in self.giv:
            print(''.join(str(x) for x in i))

    def populate(self):
        types = [".","=","|"]
        for y in range(self.target[1]+100):
            for x in range(self.target[0]+100):
                if (x == 0 and y == 0) or (x == self.target[0] and y == self.target[1]):
                    self.el[y][x] = self.depth % 20183
                elif y == 0:
                    self.el[y][x] = ((x * 16807) + self.depth) % 20183
                elif x == 0:
                    self.el[y][x] = ((y * 48271) + self.depth) % 20183
                else:
                    self.el[y][x] = ((self.el[y][x-1] * self.el[y-1][x]) + self.depth) % 20183
                self.giv[y][x] = self.el[y][x] % 3
                self.gi[y][x] = types[self.giv[y][x]]

    def AOC22_1(self):
        now = time.time()
        self.populate()
        count = 0
        for y in range(self.target[1]+1):
            for x in range(self.target[0]+1):
                count += self.giv[y][x]

        #self.print()
        print("AOC22_1: Result:", count)
        print("Time taken: " + str(time.time() - now))


    def AOC22_2(self):
        now = time.time()

 
        print("AOC22_2: Result:")
        print("Time taken: " + str(time.time() - now))
