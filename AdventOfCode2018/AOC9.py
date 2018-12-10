import time

class AOC9:
    players = 0
    turns = 0
    c = [] #Circle
    p = [] #Players Scores

    def __init__(self, inPlayers, inTurns):
        self.players = inPlayers
        self.turns = inTurns
        for i in range(inPlayers):
            self.p.append(0)
        self.c.append(0)

    def AOC9_1(self):
        now = time.time()
        for i in range(1,self.turns+1):

        print("AOC9_1: ")
        print("Time taken: " + str(time.time() - now))

    def AOC9_2(self):
        now = time.time()

        print("AOC9_2: ")
        print("Time taken: " + str(time.time() - now))

