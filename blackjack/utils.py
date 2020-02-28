from slower import slower
from card import Card

def cut_deck(deck, cut_point):
    for i in range(52):
        deck[i-cut_point], deck[i]=deck[i], deck[i-cut_point]

    return deck

def count(deck,hand,i,Flag):
    if deck[i][0]==14 and (hand+11)<21:
        hand+=11
        i+=1
        Flag==True
    elif deck[i][0]==14 and Flag==True :
        hand+=11
        i+=1
    elif deck[i][0]==14:
        hand+=1
        i+=1
    else:
        hand+=deck[i][0]
        i+=1
 
    return hand,i,Flag

@slower
def check(hand,who):
    if hand>21:
        print(who," lost! sum over 21...")
        exit()

rank=[i for i in range(2,15)]
suit=["Spades", "Hearts", "Clubs", "Diamonds"]

def make_deck(name):
    for j in suit:
        for i in rank:
            _=Card(i,j)
            name.append((_.rank, _.suit))