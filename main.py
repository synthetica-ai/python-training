def HandPowder(Hand):
    Num = []
    Suit = []
    a = []
    k = 0
    for i in range(0,5):
        Num.append(Hand[i][0])
        Suit.append(Hand[i][1])
    Num.sort(reverse = True)
    Suit.sort(reverse = True)
    
    if len(set(Num)) == 5:
        
        if len(set(Suit)) == 1:
            if (Num[0] - Num[4] == 4) or ((Num[1]-Num[4] == 3) and (Num[0] ==14) and Num[1] == 5):
                if (Num[1] - Num[4] == 3) and (Num[0] == 14) and Num[1] == 5 :                    
                    Num[0] = 1
                    Num.sort(reverse = True)
                a.append(9)
                a.append(Num[0])
            else:
                a.append(6)
                a.extend(Num)
        elif (Num[0] - Num[4] == 4) or ((Num[1] - Num[4] == 3) and (Num[0] == 14) and Num[1] == 5):  
            if ((Num[1] - Num[4]) == 3) and (Num[0] ==14) and Num[1] == 5:                    
                    Num[0] = 1
                    Num.sort(reverse = True)
            a.append(5)
            a.append(Num[4])
        else:
            a.append(1)
            a.extend(Num)
    
    elif len(set(Num)) == 2:
        if Num[2] != Num[3]:
            a.append(7)
            a.append(Num[2])
        else:
            a.append(8)
            a.append(Num[1])

    elif len(set(Num)) == 3:
        if (Num[0] == Num[2]) or (Num[1] == Num[3]) or (Num[2] == Num[4]):
            a.append(4)
            a.append(Num[2])
                 
        else: 
            a.append(3)
            a.append(Num[1])
            a.append(Num[3])
            a.sort(reverse = True)
            set(Num)
            for i in range(0,2):
                if Num[i] not in a: 
                    a.append(Num[i])

    else:
        for i in range(0,4):
            if Num[i] == Num[i+1]:
                a.append(2)
                a.append(Num[i])
                k = i  
        del(Num[k])
        del(Num[k])
        a.extend(Num)

    return a

def ph(fyllo):
    printoung = []
    RankA = 0
    SuitesA = 0
    Ranks = {14: 'A', 13: 'K', 12: 'Q', 11: 'J'}
    Suites = {1: 'Spades', 2: 'Diamonds', 3: 'Hearts', 4: 'Clubs'}
    for i in range(0,5):
        if fyllo[i][0] in Ranks:
            RankA = Ranks[fyllo[i][0]]
        else:
            RankA = str(fyllo[i][0])
        SuitesA = Suites[fyllo[i][1]]
        printoung.append(RankA + ' ' + SuitesA)
    return(', '.join(printoung))

            
import random

while True:
    Answer = input("Do you want to play?(y/n)")
    if Answer == "y":
        pass
    elif Answer == "n":
        print("see ya later nerd")
        break
    else:
        print("Eisai pousths gamhmenos mpines")
        continue

    Deck = []
    Decko = []
    HandA = []
    HandB = []
    PowerA = []
    PowerB = []
    for i in range(2,15):
        for j in range(1,5):
            Deck.append((i,j))
                
    for i in range(0,52):
        j = random.randint(0,len(Deck)-1)
        Decko.append(Deck[j])
        del Deck[j]

    for i in range(0,5):
        HandA.append(Decko[i])
        HandB.append(Decko[i+5])

    print(ph(HandA))
    print(ph(HandB))      

    PowerA = HandPowder(HandA)
    PowerB = HandPowder(HandB)

    if PowerA[0] > PowerB[0]:
        print("O paixths A nikaei")
    elif PowerB[0] > PowerA[0]:
        print("O paixths B nikaei")
    else:
        if PowerA == PowerB:
            print("exoume split")
        else:
            for i in range(1,len(PowerA)):
                if PowerA[i] != PowerB[i]:
                    break
            if PowerA[i] > PowerB[i]:
                print("o paixths A nikaei")
            else:
                print("o paixths B nikaei")
                        


            



        
        
                
    
        