import time
import Functs
import re
import datetime
import Entry

class AOC4:
    inFile = ""
    guards = {}
    lines = []
    entries = []

    def __init__(self, filePath):
        self.inFile = filePath
        self.lines = Functs.importFile(self.inFile)

    def AOC4_1(self):
        now = time.time()

        #Create object of each entry and sort the entries chronologically.
        for line in self.lines:
            #print(line)
            currLine = re.split('] |\n',line[1:len(line)-1])
            currDate = re.split('-| |:',currLine[0])
            self.entries.append(Entry.Entry(datetime.datetime(int(currDate[0]),int(currDate[1]),int(currDate[2]),int(currDate[3]),int(currDate[4])),currLine[0],currLine[1]))
            #print(currLine)
        self.entries.sort(key=lambda x: x.oDate, reverse=False)

        guard = 0
        startMin = 0
        endMin = 0
        for e in self.entries:
            #print(e.txtDate + " " + e.entry + "\n")
            type = e.entry.split()[0]
            if type == "Guard":
                guard = int(e.entry.split()[1][1:len(e.entry.split()[1])])
                if guard not in self.guards:
                    self.guards[guard] = {}
                    #print(guard)
            elif type == "wakes":
                endMin = e.oDate.minute
                for i in range(startMin, endMin):
                    if i in self.guards[guard]:
                        self.guards[guard][i] = self.guards.get(guard).get(i) + 1
                    else:
                        self.guards[guard][i] = 1
            elif type == "falls":
                startMin = e.oDate.minute
            else:
                print("ERROR")

        #Find guard and minute.
        maxGuard = 0
        max = 0
        minute = 60
        maxMin = 0
        for g, gv in self.guards.items():
            sum = 0
            for m in self.guards[g]:
                sum += self.guards[g][m]
            #print(str(g) + " " + str(gv) + " " + str(sum))
            if sum > max:
                maxGuard = g
                max = sum
            sum = 0
            #for t in g:
                #print(t)
        #print(maxGuard)
        for n in self.guards[maxGuard]:
            if self.guards.get(maxGuard).get(n) > maxMin:
                maxMin = self.guards.get(maxGuard).get(n)
                minute = n
        print("AOC4_1: " + str(maxGuard * minute))
        print("Time taken: " + str(time.time() - now))

    def AOC4_2(self):
        now = time.time()

        #Find guard and minute.
        maxGuard = 0
        max = 0
        minute = 60
        maxMin = 0

        for g, gv in self.guards.items():
            for m in self.guards[g]:
                if self.guards.get(g).get(m) > maxMin:
                    maxMin = self.guards.get(g).get(m)
                    minute = m
                    maxGuard = g

        print("AOC4_2: " + str(maxGuard * minute))
        print("Time taken: " + str(time.time() - now))

