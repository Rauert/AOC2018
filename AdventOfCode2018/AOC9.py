import time

class AOC9:
    players = 0
    turns = 0
    c = [] #Circle
    p = [] #Players Scores
    curr = 0
    currP = 0

    def __init__(self, inPlayers, inTurns):
        self.players = inPlayers
        self.turns = inTurns
        for i in range(inPlayers):
            self.p.append(0)
        self.c.append(0)

    def AOC9_1(self):
        now = time.time()
        for i in range(1,self.turns+1):
            if (i % 100000) == 0:
                print(i)
            if i % 23 == 0:
                posi = (self.curr - 7) % len(self.c)
                self.p[self.currP] += i + self.c[posi]
                del self.c[posi]
                self.curr = posi
            else:
                posi = self.curr + 2
                if posi == len(self.c):
                    posi = 0
                elif posi > len(self.c) and len(self.c) > 1:
                    posi = 1
                elif posi > len(self.c) and len(self.c) == 1:
                    posi = 0
                #print(str(posi) + " " + str(self.curr) + " " + str(len(self.c)))
                if posi == 0:
                    self.c.append(i)
                else:
                    self.c.insert(posi,i)
                if posi == 0:
                    self.curr = len(self.c) - 1
                else:
                    self.curr = posi
            #print(str(i),end=" ")
            #print(self.c)
            #print(posi)
            #Change current player
            self.currP = (self.currP + 1) % self.players
        max = 0
        for i in self.p:
            if i > max:
                max = i
        #print(self.p)
        print("AOC9_1: " + str(max))
        print("Time taken: " + str(time.time() - now))

    def AOC9_2(self):
        now = time.time()

        print("AOC9_2: ")
        print("Time taken: " + str(time.time() - now))

