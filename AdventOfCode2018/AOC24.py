import time

class AOC24:
    a = [] #Armies

    def proceed(self,count):
        rtn = True
        a = 0
        b = 0
        for i in self.a:
            if i[0] == 0:
                a += i[1]
            else:
                b += i[1]
        if a <= 0 or b <= 0:
           rtn = False
        if count == True:
            if a > b:
                rtn = a
            else:
                rtn = b
        print("proceed",a,b,rtn)
        return rtn

    def print(self):
        for i in self.a:
            print(i)

    def __init__(self, test):
        if test == True:
            #Immune System:
                           #Allegiance, # of units, hit points, weaknesses, immunities,attack damage, attack type, initiative, effective power, attacked?
            self.a.append([0,17,5390,"rb","",4507,"f",2,17*4507,False,"im-1"]) #17 units each with 5390 hit points (weak to radiation, bludgeoning) with an attack that does 4507 fire damage at initiative 2
            self.a.append([0,989,1274,"bs","f",25,"s",3,989*25,False,"im-2"]) #989 units each with 1274 hit points (immune to fire; weak to bludgeoning, slashing) with an attack that does 25 slashing damage at initiative 3
            #Infection:
            self.a.append([1,801,4706,"r","",116,"b",1,801*116,False,"in-1"]) #801 units each with 4706 hit points (weak to radiation) with an attack that does 116 bludgeoning damage at initiative 1
            self.a.append([1,4485,2961,"fc","r",12,"s",4,4485*12,False,"in-2"]) #4485 units each with 2961 hit points (immune to radiation; weak to fire, cold) with an attack that does 12 slashing damage at initiative 4
            
        else:
            #Immune System:
            self.a.append([0,889,3275,"br","c",36,"b",12,889*36,False]) #889 units each with 3275 hit points (weak to bludgeoning, radiation; immune to cold) with an attack that does 36 bludgeoning damage at initiative 12
            self.a.append([0,94,1336,"rc","",127,"b",7,94*127,False]) #94 units each with 1336 hit points (weak to radiation, cold) with an attack that does 127 bludgeoning damage at initiative 7
            self.a.append([0,1990,5438,"","",25,"s",20,1990*25,False]) #1990 units each with 5438 hit points with an attack that does 25 slashing damage at initiative 20
            self.a.append([0,1211,6640,"","",54,"f",19,1211*54,False]) #1211 units each with 6640 hit points with an attack that does 54 fire damage at initiative 19
            self.a.append([0,3026,7938,"b","c",26,"b",16,3026*26,False]) #3026 units each with 7938 hit points (weak to bludgeoning; immune to cold) with an attack that does 26 bludgeoning damage at initiative 16
            self.a.append([0,6440,9654,"","",14,"f",4,6440*14,False]) #6440 units each with 9654 hit points with an attack that does 14 fire damage at initiative 4
            self.a.append([0,2609,8218,"b","",28,"c",3,2609*28,False]) #2609 units each with 8218 hit points (weak to bludgeoning) with an attack that does 28 cold damage at initiative 3
            self.a.append([0,3232,11865,"r","",30,"s",14,3232*30,False]) #3232 units each with 11865 hit points (weak to radiation) with an attack that does 30 slashing damage at initiative 14
            self.a.append([0,2835,7220,"","fr",18,"b",2,2835*18,False]) #2835 units each with 7220 hit points (immune to fire, radiation) with an attack that does 18 bludgeoning damage at initiative 2
            self.a.append([0,2570,4797,"c","",15,"r",17,2570*15,False]) #2570 units each with 4797 hit points (weak to cold) with an attack that does 15 radiation damage at initiative 17
            #Infection:
            self.a.append([1,333,44943,"b","",223,"s",13,333*223,False]) #333 units each with 44943 hit points (weak to bludgeoning) with an attack that does 223 slashing damage at initiative 13
            self.a.append([1,1038,10867,"","bsf",16,"c",8,1038*16,False]) #1038 units each with 10867 hit points (immune to bludgeoning, slashing, fire) with an attack that does 16 cold damage at initiative 8
            self.a.append([1,57,50892,"","",1732,"c",5,57*1732,False]) #57 units each with 50892 hit points with an attack that does 1732 cold damage at initiative 5
            self.a.append([1,196,36139,"c","",334,"f",6,196*334,False]) #196 units each with 36139 hit points (weak to cold) with an attack that does 334 fire damage at initiative 6
            self.a.append([1,2886,45736,"s","c",25,"c",1,2886*25,False]) #2886 units each with 45736 hit points (immune to cold; weak to slashing) with an attack that does 25 cold damage at initiative 1
            self.a.append([1,4484,37913,"b","frs",16,"f",18,4484*16,False]) #4484 units each with 37913 hit points (weak to bludgeoning; immune to fire, radiation, slashing) with an attack that does 16 fire damage at initiative 18
            self.a.append([1,1852,49409,"r","b",52,"r",9,1852*52,False]) #1852 units each with 49409 hit points (immune to bludgeoning; weak to radiation) with an attack that does 52 radiation damage at initiative 9
            self.a.append([1,3049,18862,"r","",12,"f",10,3049*12,False]) #3049 units each with 18862 hit points (weak to radiation) with an attack that does 12 fire damage at initiative 10
            self.a.append([1,1186,23898,"","f",34,"b",15,1186*34,False]) #1186 units each with 23898 hit points (immune to fire) with an attack that does 34 bludgeoning damage at initiative 15
            self.a.append([1,6003,12593,"","",2,"c",11,6003*2,False]) #6003 units each with 12593 hit points with an attack that does 2 cold damage at initiative 11

    def AOC24_1(self):
        now = time.time()
        
        #Select targets
        while self.proceed(False) == True:
            self.a = sorted(self.a, key=lambda k: [k[8], k[7]], reverse=True)
            self.print()
            attacks = []
            for a in range(len(self.a)):
                self.a[a][9] = False
            for a in range(len(self.a)):
                max = -1
                target = -1
                enemy = 1
                if self.a[a][0] == 1: enemy = 0
                for d in range(len(self.a)):
                    if self.a[d][0] == enemy and self.a[d][9] == False and self.a[d][1] > 0:
                        attack = self.a[a][8]
                        if self.a[a][6] in self.a[d][4]: #If immune to attack
                            attack *= 0
                        print("HERE:",self.a[a][6],self.a[d][3],self.a[a][6] in self.a[d][3])
                        if self.a[a][6] in self.a[d][3]: #If weak to attack
                            attack *= 2
                        if attack > max:
                            max = attack
                            target = d
                        #Dont need since data already ordered.
                        #elif attack == max: #Tie breaker if deal same damage to 2 armies
                        #    if self.a[target][8] > self.a[d][8]:
                        #        max = attack
                        #        target = d
                        #    elif self.a[target][8] == self.a[d][8]:
                        #        if self.a[target][7] > self.a[d][7]:
                        #            max = attack
                        #            target = d
                if max > -1:
                    attacks.append([a,target,self.a[a][7]])
                    self.a[target][9] = True
                    #print(self.a[a][10],"chooses to attack",self.a[target][10],max)
            attacks = sorted(attacks, key=lambda k: [k[2]], reverse=True)
            print(attacks)
            for m in attacks:
                if self.a[m[0]][1] > 0 and self.a[m[1]][1] > 0: #Check if units still alive
                    #Recalc damage, as may have changed if units killed.
                    attack = self.a[m[0]][8]
                    if self.a[m[0]][6] in self.a[m[1]][4]: #If immune to attack
                        attack *= 0
                    if self.a[m[0]][6] in self.a[m[1]][3]: #If weak to attack
                        attack *= 2
                    #print(self.a[m[0]][10],"attacks",self.a[m[1]][10],attack)
                    print(self.a[m[1]][1],self.a[m[1]][2],attack,int(attack / self.a[m[1]][2])) ###SOMETHING WRONG WTH MAX
                    self.a[m[1]][1] -= int(attack / self.a[m[1]][2])
                    self.a[m[1]][8] = self.a[m[1]][1] * self.a[m[1]][5] #Recalc effective power
                    print(self.a[m[1]][1])

        print("AOC24_1: Result:", self.proceed(True))
        print("Time taken: " + str(time.time() - now))

    def AOC24_2(self):
        now = time.time()
        

        print("AOC24_2: Result:", self.proceed(True))
        print("Time taken: " + str(time.time() - now))