import random

class Card:
    def __init__(self,name,suite):
        self.name = name
        self.suite = suite
    def __str__(self):
        return f"{self.name} of {self.suite}"
    def __repr__(self):
        return f"{self.name} of {self.suite}"

class Deck: 
    def __init__(self):
        self.cards = self.builddeck()    
        
        
    def builddeck(self):    
        temp = []
        for i in ["Spades", "Hearts", "Clubs", "Diamonds"]:
            for j in range(1,14):
                temp.append(Card(j,i))
        return temp

    def shuffle(self):
        Decko = []
        for _ in range(0,52):
            j = random.randint(0,len(self.cards)-1)
            Decko.append(self.cards[j])
            del self.cards[j]
        self.cards = Decko

class Player: 
    def __init__(self,name):
        self.name = name
        self.hand = []

    def takecards(self, deck):
        for i in deck.cards[0:5]:
            self.hand.append(i)
        deck.cards = deck.cards[5:]

    def handpowder(self):
        Num = []
        Suit = []
        a = []
        k = 0
        for i in range(0,5):
            Num.append(self.hand[i].name)
            Suit.append(self.hand[i].suite)
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
  

    def printHand(self):
        print(f"To fyllo toy {self.name} einai: {self.hand}")

deck = Deck()
deck.shuffle()

player1 = Player(input("Give 1 > "))
player2 = Player(input("Give 2 > "))

player1.takecards(deck)
player2.takecards(deck)

player1.printHand()
player2.printHand()

if player1.handpowder() > player2.handpowder():
    print("O paixths A nikaei")
elif player2.handpowder() > player1.handpowder():
    print("O paixths B nikaei")
else:
    print("exoume split")















        


            
        
                     





    
