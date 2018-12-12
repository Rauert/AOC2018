import time
import Functs
import re

class AOC12:
    inFile = ""
    lines = []
    rl = [] #Rule left
    rr = [] #Rule right
    p = "" #Pots 

    def __init__(self, filePath):
        self.inFile = filePath
        self.lines = Functs.importFile(self.inFile)

    def AOC12_1(self):
        now = time.time()
        self.p = "." * 20 + re.split("initial state: |\n", self.lines[0])[1] + "." * 20
        #sum = self.p.count("#")

        for i in range(2,len(self.lines)):
            rule = re.split(" => |\n", self.lines[i])
            self.rl.append(rule[0])
            self.rr.append(rule[1])

        #print(self.p, end = " ")
        #print(self.p.count("#"))
        #Iterate 20 generations
        for g in range(20):
            newP = ".."
            for i in range(2, len(self.p)-2):
                val = "."
                for r in range(len(self.rl)):
                    ss = self.p[i-2:i+3]
                    if self.rl[r] == ss:
                        val = self.rr[r]
                newP += val
                    
                        #self.p = self.p[0:i] + self.rr[r] + self.p[i+1:len(self.p)+1]
            self.p = newP + ".."

            #print(self.p, end = " ")
            #print(self.p.count("#"))
            #sum += self.p.count("#")
        sum = 0
        for i in range(len(self.p)):
            if self.p[i] == "#":
                sum+= i-20
        print("AOC12_1: Result: " + str(sum))
        print("Time taken: " + str(time.time() - now))

    def AOC12_2(self):
        now = time.time()
        self.p = "." * 1000 + re.split("initial state: |\n", self.lines[0])[1] + "." * 1000

        for i in range(2,len(self.lines)):
            rule = re.split(" => |\n", self.lines[i])
            self.rl.append(rule[0])
            self.rr.append(rule[1])

        sumP = 0
        change = 0 #Change between one gen and the next. In provided input, after gen 162 every gen just adds 23
        for g in range(1000):
            newP = ".."
            for i in range(2, len(self.p)-2):
                val = "."
                for r in range(len(self.rl)):
                    ss = self.p[i-2:i+3]
                    if self.rl[r] == ss:
                        val = self.rr[r]
                newP += val

            self.p = newP + ".."
            sum = 0
            for i in range(len(self.p)):
                if self.p[i] == "#":
                    sum+= i-1000
            #print(str(g+1) + " " + str(sum) + " dif: " + str(sum - sumP))
            change = sum - sumP
            sumP = sum

        print("AOC12_2: Result: " + str(sum + ((50000000000 - 1000) * change)))
        print("Time taken: " + str(time.time() - now))

