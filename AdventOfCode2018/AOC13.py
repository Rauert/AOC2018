import time
import Functs

class AOC13:
    inFile = ""
    lines = []
    x = [] #Cart x coord
    y = [] #Cart x coord
    d = [] #Cart direction
    t = [] #Turn option
    s = []

    def __init__(self, filePath):
        self.inFile = filePath
        self.lines = Functs.importFile(self.inFile)

    def print(self):
        for y in range(len(self.lines)):
            for x in range(len(self.lines[y])):
                var = self.lines[y][x]
                for i in range(len(self.x)):
                    if x == self.x[i] and y == self.y[i]:
                        var = self.d[i]
                print(var, end="")
            print()

    def AOC13_1(self):
        now = time.time()
        #Find carts
        for y in range(len(self.lines)):
            for x in range(len(self.lines[y])):
                if self.lines[y][x] == "^":
                    #self.lines[y][x] = "|"
                    self.lines[y] = self.lines[y][0:x] + "|" + self.lines[y][x+1:len(self.lines[y])+1]
                    self.x.append(x)
                    self.y.append(y)
                    self.d.append("u")
                    self.t.append("l")
                elif self.lines[y][x] == "v":
                    #self.lines[y][x] = "|"
                    self.lines[y] = self.lines[y][0:x] + "|" + self.lines[y][x+1:len(self.lines[y])+1]
                    self.x.append(x)
                    self.y.append(y)
                    self.d.append("d")
                    self.t.append("l")
                elif self.lines[y][x] == ">":
                    #self.lines[y][x] = "-"
                    self.lines[y] = self.lines[y][0:x] + "-" + self.lines[y][x+1:len(self.lines[y])+1]
                    self.x.append(x)
                    self.y.append(y)
                    self.d.append("r")
                    self.t.append("l")
                elif self.lines[y][x] == "<":
                    #self.lines[y][x] = "-"
                    self.lines[y] = self.lines[y][0:x] + "-" + self.lines[y][x+1:len(self.lines[y])+1]
                    self.x.append(x)
                    self.y.append(y)
                    self.d.append("l")
                    self.t.append("l")

        #self.print()
        crash = False
        while crash == False:
            for i in range(len(self.x)):
                ntx = 0 #Next piece of track
                nty = 0
                if self.d[i] == "u":
                    ntx = self.x[i]
                    nty = self.y[i] - 1
                elif self.d[i] == "d":
                    ntx = self.x[i]
                    nty = self.y[i] + 1
                elif self.d[i] == "r":
                    ntx = self.x[i] + 1
                    nty = self.y[i]
                elif self.d[i] == "l":
                    ntx = self.x[i] - 1
                    nty = self.y[i]
                nt = self.lines[nty][ntx]
                #if nt == "|" or nt == "-":
                if nt == "+":
                    if self.t[i] == "s":
                        self.t[i] = "r"
                    elif self.t[i] == "l":
                        if self.d[i] == "u":
                            self.d[i] = "l"
                        elif self.d[i] == "d":
                            self.d[i] = "r"
                        elif self.d[i] == "r":
                            self.d[i] = "u"
                        elif self.d[i] == "l":
                            self.d[i] = "d"
                        self.t[i] = "s"
                    elif self.t[i] == "r":
                        if self.d[i] == "u":
                            self.d[i] = "r"
                        elif self.d[i] == "d":
                            self.d[i] = "l"
                        elif self.d[i] == "r":
                            self.d[i] = "d"
                        elif self.d[i] == "l":
                            self.d[i] = "u"
                        self.t[i] = "l"
                elif nt == "/":
                    if self.d[i] == "u":
                        self.d[i] = "r"
                    elif self.d[i] == "d":
                        self.d[i] = "l"
                    elif self.d[i] == "r":
                        self.d[i] = "u"
                    elif self.d[i] == "l":
                        self.d[i] = "d"
                elif nt == "\\":
                    if self.d[i] == "u":
                        self.d[i] = "l"
                    elif self.d[i] == "d":
                        self.d[i] = "r"
                    elif self.d[i] == "r":
                        self.d[i] = "d"
                    elif self.d[i] == "l":
                        self.d[i] = "u"
                #Check for crash
                for j in range(len(self.x)):
                    if i != j:
                        if ntx == self.x[j] and nty == self.y[j]:
                            crash = True
                            print("AOC13_1: Result: " + str(ntx) + "," + str(nty))
                self.x[i] = ntx
                self.y[i] = nty
            #self.print()

        print("Time taken: " + str(time.time() - now))

    def AOC13_2(self):
        now = time.time()
        #Find carts
        for y in range(len(self.lines)):
            for x in range(len(self.lines[y])):
                if self.lines[y][x] == "^":
                    #self.lines[y][x] = "|"
                    self.lines[y] = self.lines[y][0:x] + "|" + self.lines[y][x+1:len(self.lines[y])+1]
                    self.x.append(x)
                    self.y.append(y)
                    self.s.append(x + y)
                    self.d.append("u")
                    self.t.append("l")
                elif self.lines[y][x] == "v":
                    #self.lines[y][x] = "|"
                    self.lines[y] = self.lines[y][0:x] + "|" + self.lines[y][x+1:len(self.lines[y])+1]
                    self.x.append(x)
                    self.y.append(y)
                    self.s.append(x + y)
                    self.d.append("d")
                    self.t.append("l")
                elif self.lines[y][x] == ">":
                    #self.lines[y][x] = "-"
                    self.lines[y] = self.lines[y][0:x] + "-" + self.lines[y][x+1:len(self.lines[y])+1]
                    self.x.append(x)
                    self.y.append(y)
                    self.s.append(x + y)
                    self.d.append("r")
                    self.t.append("l")
                elif self.lines[y][x] == "<":
                    #self.lines[y][x] = "-"
                    self.lines[y] = self.lines[y][0:x] + "-" + self.lines[y][x+1:len(self.lines[y])+1]
                    self.x.append(x)
                    self.y.append(y)
                    self.s.append(x + y)
                    self.d.append("l")
                    self.t.append("l")

        #self.print()
        crash = False
        while crash == False:
            order = sorted(range(len(self.s)), key=lambda k: self.s[k]) #Ensure carts are moved in order from top to bottom, uses x+y to sort. Poor logic 2+3 and 3+2 are the same, doesnt ensure correct order
                                                                        #Could use: my_list = [[1,2],[0,2],[2,1],[1,1],[2,2],[2,0],[0,1],[1,0],[0,0]]
                                                                        #           sorted(my_list , key=lambda k: [k[1], k[0]]) #Sorts on y, then x.
                                                                        #           b[[0, 0], [1, 0], [2, 0], [0, 1], [1, 1], [2, 1], [0, 2], [1, 2], [2, 2]]
            for i in order:
                if self.d[i] != "x":
                    ntx = 0 #Next piece of track
                    nty = 0
                    if self.d[i] == "u":
                        ntx = self.x[i]
                        nty = self.y[i] - 1
                    elif self.d[i] == "d":
                        ntx = self.x[i]
                        nty = self.y[i] + 1
                    elif self.d[i] == "r":
                        ntx = self.x[i] + 1
                        nty = self.y[i]
                    elif self.d[i] == "l":
                        ntx = self.x[i] - 1
                        nty = self.y[i]
                    nt = self.lines[nty][ntx]
                    #if nt == "|" or nt == "-":
                    if nt == "+":
                        if self.t[i] == "s":
                            self.t[i] = "r"
                        elif self.t[i] == "l":
                            if self.d[i] == "u":
                                self.d[i] = "l"
                            elif self.d[i] == "d":
                                self.d[i] = "r"
                            elif self.d[i] == "r":
                                self.d[i] = "u"
                            elif self.d[i] == "l":
                                self.d[i] = "d"
                            self.t[i] = "s"
                        elif self.t[i] == "r":
                            if self.d[i] == "u":
                                self.d[i] = "r"
                            elif self.d[i] == "d":
                                self.d[i] = "l"
                            elif self.d[i] == "r":
                                self.d[i] = "d"
                            elif self.d[i] == "l":
                                self.d[i] = "u"
                            self.t[i] = "l"
                    elif nt == "/":
                        if self.d[i] == "u":
                            self.d[i] = "r"
                        elif self.d[i] == "d":
                            self.d[i] = "l"
                        elif self.d[i] == "r":
                            self.d[i] = "u"
                        elif self.d[i] == "l":
                            self.d[i] = "d"
                    elif nt == "\\":
                        if self.d[i] == "u":
                            self.d[i] = "l"
                        elif self.d[i] == "d":
                            self.d[i] = "r"
                        elif self.d[i] == "r":
                            self.d[i] = "d"
                        elif self.d[i] == "l":
                            self.d[i] = "u"
                    #Check for crash
                    for j in range(len(self.x)):
                        if i != j and self.d[j] != "x":
                            if ntx == self.x[j] and nty == self.y[j]:
                                #crash = True
                                self.d[i] = "x"
                                self.d[j] = "x"
                    self.x[i] = ntx
                    self.y[i] = nty
                    self.s[i] = ntx + nty
            #self.print()
            sum = 0
            for i in range(len(self.d)):
                if self.d[i] != "x":
                    sum += 1
            if sum == 1:
                crash = True
                for i in range(len(self.d)):
                    if self.d[i] != "x":
                        print("AOC13_2: Result: " + str(self.x[i]) + "," + str(self.y[i]))
        print("Time taken: " + str(time.time() - now))

