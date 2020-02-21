from itertools import chain, product
from random import shuffle, sample

suits = ['diamonds', 'hearts', 'spades', 'clubs']

rank = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

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

    updatedDeck = list(map(deck.remove, hand))
    return  hand, updatedDeck

deck = createDeck()

shuffleDeck(deck)

player1, deck = getHand(deck)
player2, deck = getHand(deck)

