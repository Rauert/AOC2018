import time
import Functs

class AOC7:
    inFile = ""
    lines = []
    inst = {}
    instTm = {}

    def __init__(self, filePath):
        self.inFile = filePath
        self.lines = Functs.importFile(self.inFile)

    def AOC7_1(self):
        now = time.time()
        keys = []
        for l in self.lines:
            ll = l.split()
            if ll[1] not in keys:
                keys.append(ll[1])
            if ll[7] not in keys:
                keys.append(ll[7])
        keys.sort()
        for k in keys:
            self.inst[k] = []
        for l in self.lines:
            ll = l.split()
            self.inst[ll[7]].append(ll[1])
        for i in self.inst.values():
            #print(i)
            i.sort()
        #for i in self.inst.items():
            #print(i)
        order = ""
        while len(self.inst) > 0:
            for k,i in self.inst.items():
                if len(i) == 0:
                    order = order + k
                    del self.inst[k]
                    for kk,ii in self.inst.items():
                        if k in ii:
                            ii.remove(k)
                    break

        #print(self.inst)
        print("AOC7_1: Result: " + order)
        print("Time taken: " + str(time.time() - now))

    def AOC7_2(self):
        now = time.time()
        keys = []
        for l in self.lines:
            ll = l.split()
            if ll[1] not in keys:
                keys.append(ll[1])
            if ll[7] not in keys:
                keys.append(ll[7])
        keys.sort()
        for k in keys:
            self.inst[k] = []
            self.instTm[k] = ord(k) - 4 # - 64 for testing
        for l in self.lines:
            ll = l.split()
            self.inst[ll[7]].append(ll[1])
        for i in self.inst.values():
            #print(i)
            i.sort()
        #for i in self.inst.items():
            #print(i)
        totTime = 0
        timeLeft = True
        workers = ['0','0','0','0','0']
        #workers = ['0','0'] #For testing
        while len(self.inst) > 0 or timeLeft == True:
            print(workers)
            print(totTime)
            #find available tasks
            for k,i in self.inst.items():
                if len(i) == 0: 
                    #Assign task
                    for w in range(len(workers)):
                        if workers[w] == '0':
                            workers[w] = k
                            #del self.inst[k]
                            break
            print(workers)
            #Iterate time by 1 sec
            totTime += 1
            for w in range(len(workers)):
                if workers[w] != '0':
                    if workers[w] in self.inst:
                        del self.inst[workers[w]]
                    self.instTm[workers[w]] = self.instTm.get(workers[w]) - 1
                    #Check for completed tasks
                    if self.instTm.get(workers[w]) == 0:
                        for k,i in self.inst.items():
                            if workers[w] in i:
                                i.remove(workers[w])
                        workers[w] = '0'
            timeSum = 0
            for k,i in self.instTm.items():
                timeSum += i
            if timeSum == 0:
                timeLeft = False

            #print(workers)
            #print(totTime)
               #if self.instTm.get(k) == 0:
               #     
               #     for kk,ii in self.inst.items():
               #         if k in ii:
               #             ii.remove(k)
               #     break

        print("AOC7_2: " + str(totTime))
        print("Time taken: " + str(time.time() - now))

