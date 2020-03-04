from slower import slower
from card import Card
import config

def cut_deck(deck, cut_point):
    cut_deck=[]
    cut_deck.extend(deck[cut_point:])
    cut_deck.extend(deck[:cut_point])
    return cut_deck


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
    elif deck[i][0]>=10:
        hand+=10
        i+=i
    else:
        hand+=deck[i][0]
        i+=1

    true_counter(deck, i-1)
    return hand,i,Flag

@slower
def check(hand,who):
    if hand>21:
        print(f"{who} lost! sum over 21...")
        exit()

rank=[i for i in range(2,15)]
suit=["Spades", "Hearts", "Clubs", "Diamonds"]

def make_deck(name):
    for j in suit:
        for i in rank:
            _=Card(i,j)
            name.append((_.rank, _.suit))

def true_counter(deck,i):
    if deck[i][0]<7 :
        config.true_count+=1
        config.cards +=1
    elif deck[i][0]>9:
        config.true_count-=1
        config.cards +=1
