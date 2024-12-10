import random as rd 

def setBoite():
    N = rd.randint(1,10)
    B = rd.randint(1,10)
    print("Nombre de grains noirs : ",N)
    print("Nombre de grains blancs :",B)
    boiteCafe = []
    for i in range(N):
        boiteCafe.append("N")
    for i in range(B):
        boiteCafe.append("B")
    return boiteCafe

def AlgoDavidGries(boite: list):
    print("Boite =",boite)
    print("")
    while(len(boite)!=1): #Taille de la boite diminue à chaque passage dans la boucle 
        ramdom1 = rd.choice(boite)
        boite.remove(ramdom1)
        ramdom2 = rd.choice(boite)
        boite.remove(ramdom2)
        print("Grain 1 tiré :",ramdom1)
        print("Gain 2 tiré :",ramdom2)
        if(ramdom1 == ramdom2):
            boite.append("N")
        else:
            if(ramdom1 == "B"):
                boite.append(ramdom1)
            else:
                boite.append(ramdom2)
        print(boite)
        print("Taille Boite = ",len(boite))
        print("")
    return boite

print(AlgoDavidGries(setBoite()))

