from collections import Counter
from functools import reduce
from itertools import chain, product
from random import sample, shuffle

from card import Card

class Deck:
    rank=[i for i in range(2,15)]
    suit=["Spades", "Hearts", "Clubs", "Diamonds"]

    def __init__(self):
        self.cards=list(map(Deck.create, chain(product(Deck.rank, Deck.suit))))

    def create(args):
        c=Card(*args)
        return c.__str__()

    def deck_shuffle(self):
        shuffle(self.cards)

    def take_hand(self):
        h=list(sample(self.cards,5))
        for k in h:
            self.cards.remove(k)
        return h

def suits(k):
    new_l=list(map(lambda x: x['suit'], k))
    flag=reduce(lambda x,y: x if x==y else 0 ,new_l)
    return bool(flag)

def sort_hand(k):
    new_l=list(map(lambda x:x['rank'], k))
    return new_l

def evaluate(s,r):
    c=Counter(r)
    max_times=max(c.values())
    high=[k for k,l in c.items() if l==max_times]
    high.sort(reverse=True)
    flush=reduce(lambda a,b: b if (a-b==1) else 0, r)
    four=True if max_times==4 else False
    full=True if (max_times==3 and len(c)==2)  else False
    straight=s
    three=True if max_times==3 else False
    two_pairs=True if max_times==2 and len(c)==3 else False
    pair=True if max_times==2 else False
    eval=[straight and flush,
        four,
        full,
        flush,
        straight,
        three,
        two_pairs,
        pair,
        high]

    evalindex = [bool(value) for value in eval].index(True)
    return evalindex, high
