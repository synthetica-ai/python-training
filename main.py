from itertools import chain, product
from random import shuffle, sample

suits = ['diamonds', 'hearts', 'spades', 'clubs']

rank = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14']

def createCard(combination):
    card = {}
    card['rank'], card['suit'] = combination

    return card

def createDeck():
    return list(map(createCard, chain(product(rank, suits))))

def shuffleDeck(deck):
    shuffle(deck)

    return deck

def getHand(deck):
    hand = sample(deck, 5)

    map(deck.remove, hand)
    
    return  hand, deck

deck = createDeck()

shuffleDeck(deck)

player1, deck = getHand(deck)
player2, deck = getHand(deck)

