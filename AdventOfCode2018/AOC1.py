import time
import Functs

class AOC1:
    inFile = ""

    def __init__(self, filePath):
        self.inFile = filePath

    def exists(self, history, x):
        found = False
        for y in history:
            if y == x:
                found = True
        return found

    def AOC1_1(self):
        lines = Functs.importFile(self.inFile)
        x = 0

        for line in lines:
            x = x + int(line)
        print("AOC1_1: " + str(x))

    def AOC1_2(self):
        now = time.time()
        lines = Functs.importFile(self.inFile)
        length = len(lines)
        curr = 0
        x = 0
        history = [x]
        found = False

        while found == False:
            if curr == length:
                curr = 0
            line = lines[curr]
            y = int(line)
            x = x + y
            if exists(history, x) == True:
                found = True
            else:
                curr = curr + 1
            history.append(x)
        print("AOC1_2: " + str(x))
        print("Time taken: " + str(time.time() - now))

    def AOC1_2_Opt(self):
        now = time.time()
        lines = Functs.importFile(self.inFile)
        length = len(lines)
        curr = 0
        x = 0
        history = {x: x}
        found = False

        while found == False:
            if curr == length:
                curr = 0
            line = lines[curr]
            y = int(line)
            x = x + y
            if x in history:
                found = True
            else:
                curr = curr + 1
            history[x] = x
        print("AOC1_2: " + str(x))
        print("Time taken: " + str(time.time() - now))
