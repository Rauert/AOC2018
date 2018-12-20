import time
import Functs
import re
from copy import deepcopy

class AOC19:
    lines = []
    i = 0
    p = []
    r = [0,0,0,0,0,0]

    def __init__(self, filePath):
        self.lines = Functs.importFile(filePath)

    def runInstr(self,i):
            code = i[0]
            if code[0:2] == "ad": #addr
                a = self.r[i[1]]
                if code[3:4] == "i": #addi
                    b = i[2]
                else:
                    b = self.r[i[2]]
                self.r[i[3]] = a + b
            elif code[0:2] == "mu": #mulr
                a = self.r[i[1]]
                if code[3:4] == "i": #muli
                    b = i[2]
                else:
                    b = self.r[i[2]]
                self.r[i[3]] = a * b
            elif code[0:2] == "ba": #banr
                a = self.r[i[1]]
                if code[3:4] == "i": #bani
                    b = i[2]
                else:
                    b = self.r[i[2]]
                self.r[i[3]] = a & b
            elif code[0:2] == "bo": #borr
                a = self.r[i[1]]
                if code[3:4] == "i": #bori
                    b = i[2]
                else:
                    b = self.r[i[2]]
                self.r[i[3]] = a | b
            elif code[0:2] == "se": #setr
                if code[3:4] == "i": #seti
                    a = i[1]
                else:
                    a = self.r[i[1]]
                self.r[i[3]] = a
            elif code[0:2] == "gt": #gtrr
                if code[2:3] == "i": #gtir
                    a = i[1]
                else:
                    a = self.r[i[1]]
                if code[3:4] == "i": #gtri
                    b = i[2]
                else:
                    b = self.r[i[2]]
                self.r[i[3]] = int(a > b)
            elif code[0:2] == "eq": #eqrr
                if code[2:3] == "i": #eqir
                    a = i[1]
                else:
                    a = self.r[i[1]]
                if code[3:4] == "i": #eqri
                    b = i[2]
                else:
                    b = self.r[i[2]]
                self.r[i[3]] = int(a == b)

    def AOC19_1(self):
        now = time.time()
        self.i = int(self.lines[0].split()[1])
        for i in range(1,len(self.lines)):
            l = self.lines[i].split()
            self.p.append([l[0], int(l[1]), int(l[2]), int(l[3])])
        while self.r[self.i] < len(self.p):
            #print(self.r, self.p[self.r[self.i]])
            self.runInstr(self.p[self.r[self.i]])
            self.r[self.i] += 1
        print("AOC19_1: Result: ", self.r[0])
        print("Time taken: " + str(time.time() - now))

    #The program calculates some value in a (user-specific register), then calculates the sum of its factors. When r0 is set to 1 at the start of the program, the value in (user-specific register) is significantly larger.
    #Answer = 1 + 137 + 77017 + 10551329 = 10628484
    def AOC19_2(self):
        now = time.time()
        self.r = [1,0,0,0,0,0]
        #Loop starts at [0, 1, 1, 1, 4, 10551329] ['eqrr', 2, 5, 2]
        #OR [1, 10551330, 1, 2, 13, 10551329] ['gtrr', 3, 5, 2]
        runOnce = False
        while self.r[self.i] < len(self.p):
            print(self.r, self.p[self.r[self.i]])
            if self.r[self.i] == 4 and self.r[5] == 10551329 and runOnce == False:
                self.r[1] = self.r[5]
                self.r[2] = self.r[5]
                #self.r[3] = self.r[5]
                runOnce = True
            self.runInstr(self.p[self.r[self.i]])
            self.r[self.i] += 1
        print("AOC19_2: Result: ", self.r[0])
        print("Time taken: " + str(time.time() - now))

