import random as rd
class Box():
    def __init__(self,m):
        self.nut = [ x for x in range(m)] #Liste d'écrous
        rd.shuffle(self.nut)
        self.bolt = [ x for x in range(m)] #Liste de vis
        rd.shuffle(self.bolt)
    
    def screw(self, n, b):
        if self.nut[n] < self.bolt[b]:
            return -1 # Ecrou trop étroit
        if self.nut[n] == self.bolt[b]:
            return 0 # Ecrou et vis s'ajustent
        if self.nut[n] > self.bolt[b]:
            return 1 # Ecrou trop lâche
    
    def assemble(self):
        dico = {}
        for i in range(len(self.bolt)):
            j=0
            while(j<len(self.nut)):
                if(self.screw(i,j) == 0):
                    dico[self.nut[i]] = self.bolt[j]
                    break
                else:
                    j+=1
        return dico
    
    def fusion(self,l1,l2):
        if(not l1):return l2
        if (not l2):return l1
        if(l1[0]<l2[0]):return [l1[0]] + self.fusion(l1[1:],l2)
        return [l2[0]] + self.fusion(l1,l2[1:])

    def AlgotriFusion(self,l):
        if(len(l)==1):return l
        else:
            N = len(l)//2
            leftlist = self.AlgotriFusion(l[0:N])
            rightlist = self.AlgotriFusion(l[N:])
            a = self.fusion(leftlist,rightlist)
        return a
    
    def probabilistic_assemble(self):
        dico = {}
        newbolt = self.AlgotriFusion(self.bolt)
        for i in range(len(self.bolt)):
            pivot = rd.choice(newbolt)
            print("Nut = ",self.nut[i])
            print("Pivot random = ",pivot)
            if(self.screw(i,pivot) == 0):
                pass
            else:
                list_pivot  =[]
                list_pivot.append(pivot)
                while(self.screw(i,pivot) != 0):
                    pivot_filtres = [x for x in newbolt if x not in list_pivot]
                    pivot = rd.choice(pivot_filtres)
                    print("New pivot",pivot)
                    list_pivot.append(pivot)
            print("Bon Pivot = ",pivot)
            dico[self.nut[i]] = self.bolt[pivot]
        return dico
        


box1 = Box(5)
print("Nut :",box1.nut)
print("Bolt :",box1.bolt)
print(box1.assemble())
print(box1.probabilistic_assemble())