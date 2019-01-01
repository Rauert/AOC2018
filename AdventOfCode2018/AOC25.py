import time
import Functs

class AOC25:
    d = [] #Data
    c = [] #Connections
    a = [] #Added to constellation?
    co = [] #Constellations

    def __init__(self, filePath):
        lines = Functs.importFile(filePath)
        for l in lines:
            self.d.append(list(map(int,l.rstrip().split(","))))
            self.c.append([])
            self.a.append(False)

    def buildCO(self, coID, i):
        for j in self.c[i]:
            if self.a[j] == False:
                self.co[coID].append(self.d[j])
                self.a[j] = True
                if len(self.c[j]) > 0:
                    self.buildCO(coID,j)

    def AOC25_1(self):
        now = time.time()
        #Find each nodes connections
        for i in range(len(self.d)):
            for j in range(len(self.d)):
                if i != j:
                    if abs(self.d[i][0] - self.d[j][0]) + abs(self.d[i][1] - self.d[j][1]) + abs(self.d[i][2] - self.d[j][2]) + abs(self.d[i][3] - self.d[j][3]) <= 3:
                        self.c[i].append(j)

        #Create constellations
        for i in range(len(self.d)):
            if self.a[i] == False:
                self.co.append([self.d[i]])
                self.a[i] = True
                if len(self.c[i]) > 0:
                    #Recursively build constellation
                    self.buildCO(len(self.co)-1,i)

        #for i in self.co:
        #    print(i)
        #for i in self.c:
        #    print(i)
        print("AOC25_1: Result:", len(self.co))
        print("Time taken: " + str(time.time() - now))

    def AOC25_2(self):
        now = time.time()
        

        print("AOC25_2: Result:", self.proceed(True))
        print("Time taken: " + str(time.time() - now))
