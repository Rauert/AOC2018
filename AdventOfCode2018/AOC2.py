import time
import Functs

class AOC2:
    inFile = ""
    srchString = "abcdefghijklmnopqrstuvwxyz"

    def __init__(self, filePath):
        self.inFile = filePath

    def AOC2_1(self):
        now = time.time()
        lines = Functs.importFile(self.inFile)
        dbl = 0
        tpl = 0
        dblFnd = False
        tplFnd = False

        for line in lines:
            sortedLine = ''.join(sorted(line))
            for c in self.srchString:
                cnt = sortedLine.count(c)
                if cnt == 2:
                    dblFnd = True
                elif cnt == 3:
                    tplFnd = True
            if dblFnd == True:
                dbl = dbl + 1
            if tplFnd == True:
                tpl = tpl + 1
            dblFnd = False
            tplFnd = False
        print("AOC2_1: " + str(dbl * tpl))
        print("Time taken: " + str(time.time() - now))

    #Brute force method takes every possible answer and tests against every other string. Inefficient.
    def AOC2_2(self):
        now = time.time()
        lines = Functs.importFile(self.inFile)
        length = len(lines)
        lineLength = len(lines[0]) - 1 #-1 to remove newline char
        found = False
        Ans = ""

        for currline in lines:
            for line in lines:
                if currline != line and found == False:
                    for x in range(lineLength):
                        if x == 0:
                            #print(str(x) + " " + currline[1:lineLength])
                            #print(len(currline[1:lineLength]))
                            if currline[1:lineLength] == line[1:lineLength]:
                                #print(currline[1:lineLength])
                                found = True
                                Ans = currline[1:lineLength]
                        elif x == lineLength - 1:
                            #print(str(x) + " " + currline[0:lineLength-1])
                            #print(len(currline[0:lineLength-1]))
                            if currline[0:lineLength-1] == line[0:lineLength-1]:
                                #print(currline[0:lineLength-1])
                                found = True
                                Ans = currline[0:lineLength-1]
                        else:
                            print(str(x) + " " + currline[0:x] + " " + currline[x + 1:lineLength])
                            if currline[0:x] + currline[x + 1:lineLength] == line[0:x] + line[x + 1:lineLength]:
                                found = True
                                Ans = currline[0:x] + currline[x + 1:lineLength]
        print("AOC2_2: " + str(Ans))
        print("Time taken: " + str(time.time() - now))

    #Optimised Day 2 part 2
    def AOC2_2O(self):
        now = time.time()
        lines = Functs.importFile(self.inFile)
        length = len(lines)
        lineLength = len(lines[0]) - 1 #-1 to remove newline char
        found = False
        Ans = ""

        i = -1
        for cl in lines:
            i += 1
            for l in range(i,len(lines)):
                dif = 0
                index = 0
                for j in range(lineLength):
                    if cl[j] != lines[l][j]:
                        dif += 1
                        index = j
                    if dif > 1:
                        break
                if dif == 1:
                    #print(cl)
                    #print(lines[l])
                    print("AOC2_2: " + str(cl[0:index] + cl[index + 1:lineLength]))
                    print("Time taken: " + str(time.time() - now))
                    return