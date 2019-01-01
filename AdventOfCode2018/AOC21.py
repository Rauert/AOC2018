import time
import Functs
import re
from copy import deepcopy

class AOC21:
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

    def AOC21(self):
        now = time.time()
        self.r[0] = 11474091 #Ans 1
        self.r[0] = 4520776 #Ans 2
        hist = []
        self.i = int(self.lines[0].split()[1])
        for i in range(1,len(self.lines)):
            l = self.lines[i].split()
            self.p.append([l[0], int(l[1]), int(l[2]), int(l[3])])
        count = 0
        while self.r[self.i] < len(self.p):
            if self.r[self.i] == 28:
                if self.r[3] not in hist:
                    print(self.r[3])
                    hist.append(self.r[3])
                else:
                    print("loop",self.r[3])
                    break
            #print(self.r, self.p[self.r[self.i]])
            self.runInstr(self.p[self.r[self.i]])
            self.r[self.i] += 1
            count += 1
        print("AOC21_1: Result: ", hist[0])
        print("AOC21_2: Result: ", hist[-1])
        print("Time taken: " + str(time.time() - now))


