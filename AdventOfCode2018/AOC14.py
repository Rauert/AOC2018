import time
import Functs

class AOC14:
    c1 = 0
    c2 = 1
    s = [3, 7]
    m = 0
    ms = ""
    ss = "37"

    def __init__(self, inSR):
        self.ms = inSR
        self.m = int(inSR)

    def AOC14_1(self):
        now = time.time()

        c1 = self.c1
        c2 = self.c2
        s = self.s
        m = self.m
        
        while len(s) < m + 10:
            r = s[c1] + s[c2]
            if r > 9:
                s.append(1)
                s.append(r - 10)
            else:
                s.append(r)
            c1 = (c1 + s[c1] + 1) % len(s)
            c2 = (c2 + s[c2] + 1) % len(s)

        ans = ""
        for i in range (m,m+10):
            ans += str(s[i])
        print("AOC14_1: Result: " + ans)
        print("Time taken: " + str(time.time() - now))

    #Slow
    def AOC14_2A(self):
        now = time.time()

        self.c1 = 0
        self.c2 = 1

        c1 = self.c1
        c2 = self.c2
        s = self.ss
        m = self.ms

        found = False
        ans = 0
        ii = 0
        c = 0
        while found == False:
            c += 1
            if c % 100000 == 0: print(c)
            s += str(int(s[c1]) + int(s[c2]))
            c1 = (c1 + int(s[c1]) + 1) % len(s)
            c2 = (c2 + int(s[c2]) + 1) % len(s)
            ii = s.find(m)
            if ii != -1:
                found = True
        print("AOC14_2: " + str(len(s[0:ii])))
        print("Time taken: " + str(time.time() - now))

    def AOC14_2(self):
        now = time.time()
        self.s = [3, 7]
        self.c1 = 0
        self.c2 = 1

        c1 = self.c1
        c2 = self.c2
        s = self.s
        m = self.ms

        for i in range(20000000):
            r = s[c1] + s[c2]
            if r > 9:
                s.append(1)
                s.append(r - 10)
            else:
                s.append(r)
            c1 = (c1 + s[c1] + 1) % len(s)
            c2 = (c2 + s[c2] + 1) % len(s)

        print("AOC14_2: " + str(''.join(map(str,s)).index('077201')))
        print("Time taken: " + str(time.time() - now))

    def run(self):
        for i in range(1000000):
            r = self.s[self.c1] + self.s[self.c2]
            if r > 9:
                self.s.append(1)
                self.s.append(r - 10)
            else:
                self.s.append(r)
            self.c1 = (self.c1 + self.s[self.c1] + 1) % len(self.s)
            self.c2 = (self.c2 + self.s[self.c2] + 1) % len(self.s)

    def AOC14_2AA(self):
        now = time.time()
        self.s = [3, 7]
        self.c1 = 0
        self.c2 = 1

        while self.ms not in ''.join(map(str,self.s)):
            self.run()

        print("AOC14_2: " + str(''.join(map(str,self.s)).index(self.ms)))
        print("Time taken: " + str(time.time() - now))