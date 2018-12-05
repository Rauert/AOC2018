import time
import Functs
import sys

class AOC5:
    inFile = ""
    lines = []
    s = ""

    def __init__(self, filePath):
        self.inFile = filePath
        self.lines = Functs.importFile(self.inFile)

    def extractStr(self, inStr, x):
        if x == 0:
            return inStr[2:len(inStr)]
        elif x + 1 == len(inStr) - 1:
            return inStr[0:len(inStr) - 2]
        else:
            return inStr[0:x] + inStr[x + 2:len(inStr)]

    def extractStr1(self, inStr, x):
        if x == 0:
            return inStr[1:len(inStr)]
        elif x == len(inStr) - 1:
            return inStr[0:len(inStr) - 1]
        else:
            return inStr[0:x] + inStr[x + 1:len(inStr)]

    #didnt work
    def recursePolymer(self, inStr):
        for i in range(len(inStr)):
            if i == len(inStr) - 1: #End of string
                return inStr
                break
            else:
                if str.isupper(inStr[i]) == True and str.islower(inStr[i+1]) == True:
                    if ord(inStr[i])+32 == ord(inStr[i+1]):
                        self.recursePolymer(self.extractStr(inStr, i))
                        break
                if str.islower(inStr[i]) == True and str.isupper(inStr[i+1]) == True:
                    if ord(inStr[i])-32 == ord(inStr[i+1]):
                        self.recursePolymer(self.extractStr(inStr, i))
                        break

    def reducePol(self):
        found = False
        i = 0
        while found == False:
            #print(len(self.s))
            if i == len(self.s) - 1: #End of string
                found = True
            else:
                if str.isupper(self.s[i]) == True and str.islower(self.s[i+1]) == True:
                    if ord(self.s[i])+32 == ord(self.s[i+1]):
                        self.s = self.extractStr(self.s, i)
                        if i != 0:
                            i -= 1
                    else:
                        i += 1
                elif str.islower(self.s[i]) == True and str.isupper(self.s[i+1]) == True:
                    if ord(self.s[i])-32 == ord(self.s[i+1]):
                        self.s = self.extractStr(self.s, i)
                        if i != 0:
                            i -= 1
                    else:
                        i += 1
                else:
                    i += 1

    def reducePolLetter(self, a, A):
        found = False
        i = 0
        while found == False:
            #print(len(self.s))
            if i == len(self.s) - 1: #End of string
                found = True
            else:
                if self.s[i] == a or self.s[i] == A:
                    self.s = self.extractStr1(self.s, i)
                else:
                    i += 1

    def AOC5_1(self):
        now = time.time()

        #Create object of each entry and sort the entries chronologically.
        #lower = "abcdefghijklmnopqrstuvwyxz"
        #upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        #for c in lower:
        #    print(c + " " + str(ord(c)))
        #for c in upper:
        #    print(c + " " + str(ord(c)))
        #sys.setrecursionlimit(3000)
        self.s = self.lines[0][0:len(self.lines[0])-1]
        #print(len(self.s))
        #print(self.s)
        self.reducePol()
 
        print("AOC5_1: Result: " + str(len(self.s)))
        print(self.s)
        print("Time taken: " + str(time.time() - now))

    def AOC5_2(self):
        now = time.time()
        lower = "abcdefghijklmnopqrstuvwxyz"
        upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        ans = len(self.lines[0][0:len(self.lines[0])-1])
        for a in range(26):
            self.s = self.lines[0][0:len(self.lines[0])-1]
            self.reducePolLetter(lower[a], upper[a])
            #self.s = self.s.replace(lower[a], '')
            #self.s = self.s.replace(upper[a], '')
            self.reducePol()
            if len(self.s) < ans:
                ans = len(self.s)

        print("AOC5_2: " + str(ans))
        print("Time taken: " + str(time.time() - now))

