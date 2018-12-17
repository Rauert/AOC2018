import time
import Functs
import re
from copy import deepcopy

class AOC16:
    lines = []
    lines2 = []
    b = []
    a = [] 
    i = [] 
    p = [] 
    r = []
    ins = ["addr","addi","mulr","muli","banr","bani","borr","bori","setr","seti","gtir","gtri","gtrr","eqir","eqri","eqrr"]

    def __init__(self, filePath1, filePath2):
        self.lines = Functs.importFile(filePath1)
        self.lines2 = Functs.importFile(filePath2)

    def runInstr(self,code,r,i):
            a = r[i[1]]
            b = r[i[2]]
            if code[0:2] == "ad": #addr
                if code[3:4] == "i": #addi
                    b = i[2]
                r[i[3]] = a + b
            elif code[0:2] == "mu": #mulr
                if code[3:4] == "i": #muli
                    b = i[2]
                r[i[3]] = a * b
            elif code[0:2] == "ba": #banr
                if code[3:4] == "i": #bani
                    b = i[2]
                r[i[3]] = a & b
            elif code[0:2] == "bo": #borr
                if code[3:4] == "i": #bori
                    b = i[2]
                r[i[3]] = a | b
            elif code[0:2] == "se": #setr
                if code[3:4] == "i": #seti
                    a = i[1]
                r[i[3]] = a
            elif code[0:2] == "gt": #gtrr
                if code[2:3] == "i": #gtir
                     a = i[1]
                if code[3:4] == "i": #gtri
                     b = i[2]
                r[i[3]] = int(a > b)
            elif code[0:2] == "eq": #eqrr
                if code[2:3] == "i": #eqir
                     a = i[1]
                if code[3:4] == "i": #eqri
                     b = i[2]
                r[i[3]] = int(a == b)
            return r

    def AOC16_1(self):
        now = time.time()

        for i in range(0,len(self.lines),4):
            self.b.append(list(map(int, [self.lines[i][9],self.lines[i][12],self.lines[i][15],self.lines[i][18]])))
            self.i.append(list(map(int, self.lines[i+1].split())))
            self.a.append(list(map(int, [self.lines[i+2][9],self.lines[i+2][12],self.lines[i+2][15],self.lines[i+2][18]])))
        for i in range(len(self.b)):
            ops = []
            #All opcode inputs/outputs are all <=3 so no register range checking required.
            for ii in self.ins:
                bef = self.b[i]
                inst = self.i[i]
                aft = self.a[i]
                #print(bef)
                if aft == self.runInstr(ii,deepcopy(bef),inst):
                    ops.append(ii)
                #print(ii)
                #print(bef)
            self.r.append(ops)
        #print(self.r)
        sum = 0
        for j in self.r:
            if len(j) > 2:
                sum += 1
        print("AOC16_1: Result: " + str(sum))
        print("Time taken: " + str(time.time() - now))

    def AOC16_2(self):
        now = time.time()
 
        #Look for examples that only correspond to one code. Once known delete this code from dataset. Loop until all found
        for i in range(len(self.lines2)):
            self.p.append(list(map(int, self.lines2[i].split())))
        codes = []
        while len(codes) < 16:
            currCode = ""
            for j in range(len(self.r)):
                if len(self.r[j]) == 1:
                    currCode = self.r[j][0]
                    codes.append([currCode, self.i[j][0]])
                    break
            for i in range(len(self.r)):
                if currCode in self.r[i]:
                    self.r[i].remove(currCode)
        #for i in sorted(codes , key=lambda k: [k[1]]):
            #print(i)
        codes = sorted(codes , key=lambda k: [k[1]])
        r = [0,0,0,0]
        for i in self.p:
            r = self.runInstr(codes[i[0]][0],r,i)
        print("AOC16_2: Result: " + str(r[0]))
        print("Time taken: " + str(time.time() - now))

