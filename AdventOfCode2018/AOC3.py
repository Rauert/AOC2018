import time
import Functs
import re

class AOC3:
    inFile = ""
    history = {}
    lines = []

    def __init__(self, filePath):
        self.inFile = filePath
        self.lines = Functs.importFile(self.inFile)

    def AOC3_1(self):
        now = time.time()

        sum = 0

        for line in self.lines:
            currLine = re.split(' @ |,|: |x|\n',line)
            x = int(currLine[1])
            y = int(currLine[2])
            a = int(currLine[3])
            b = int(currLine[4])
            #print("Processing claim " + currLine[0])
            for ai in range(a):
                for bi in range(b):
                    key = str(x + ai) + "," + str(y + bi)
                    if key in self.history:
                        if self.history.get(key) == 1:
                            sum = sum + 1
                        self.history[key] = self.history.get(key) + 1
                    else:
                        self.history[key] = 1
                    #print(key)
            #for h, v in self.history.items():
                #print(h + " " + str(v))
        print("AOC3_1: " + str(sum))
        print("Time taken: " + str(time.time() - now))

    def AOC3_2(self):
        now = time.time()

        for line in self.lines:
            currLine = re.split(' @ |,|: |x|\n',line)
            claim = currLine[0]
            x = int(currLine[1])
            y = int(currLine[2])
            a = int(currLine[3])
            b = int(currLine[4])
            sum = 0
            size = a * b
            #print("Processing claim " + claim)
            for ai in range(a):
                for bi in range(b):
                    key = str(x + ai) + "," + str(y + bi)
                    if key in self.history:
                        sum = sum + self.history.get(key)
            if sum == size:
                break

        print("AOC3_2: " + claim)
        print("Time taken: " + str(time.time() - now))
