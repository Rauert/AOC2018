import time
import Functs
import Node

class AOC8:
    inFile = ""
    line = []
    metaTot = 0
    i = 0
    head = None
    nodes = []

    def __init__(self, filePath):
        self.inFile = filePath
        lines = Functs.importFile(self.inFile)
        lines = lines[0]
        lines = lines.split()
        self.line = [int(x) for x in lines]

    def procNode(self, p):
        n = Node.Node(p)
        c = self.line[self.i]
        self.i += 1
        m = self.line[self.i]
        self.i += 1
        n.c = []
        for ci in range(c):
            n.c.append(self.procNode(n))
        n.m = []
        for mi in range(m):
            self.metaTot += self.line[self.i]
            n.m.append(self.line[self.i])
            self.i += 1
        self.nodes.append(n)
        #print(n.m)
        return n

    def calcVal(self, p):
        sum = 0
        if len(p.c) == 0:
            for i in p.m:
                sum += i
        else:
            print(p.m)
            for i in p.m:
                if i - 1 < len(p.c):
                    sum += self.calcVal(p.c[i - 1])
        return sum

    def AOC8_1(self):
        now = time.time()
        self.head = self.procNode(None)
        print("AOC8_1: Result: " + str(self.metaTot))
        print("Time taken: " + str(time.time() - now))

    def AOC8_2(self):
        now = time.time()
        #for n in self.nodes:
            #print(n.c)
            #for c in n.c:
            #    print(c.c)
            #    print(c.m)
            #print(n.m)
            #print(n.p)
        print("AOC8_2: " + str(self.calcVal(self.head)))
        print("Time taken: " + str(time.time() - now))

