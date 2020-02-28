from itertools import chain, product
from random import shuffle, sample
from collections import Counter

suits = ['diamonds', 'hearts', 'spades', 'clubs']

rank = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

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

def checkFlush(hand):
    flush = dict(Counter([c['suit'] for c in hand]))

    hasflush = any([v == 5 for v in flush.values()])

    return [max([c['rank'] for c in hand])] if hasflush else False

def checkStraight(hand):
    ranks = [c['rank'] for c in hand]

    hasStraight = sorted(ranks) == list(range(min(ranks), max(ranks)+1))
    return [max([c['rank'] for c in hand])] if hasStraight else False

def getRanking(hand):
    return dict(Counter([c['rank'] for c in hand]))

def checkPairType(ranks, num):
    pairList = [k if ranks[k] == num else False for k in ranks.keys()]
    hasPairType = list(filter(lambda k: k, pairList))

    return hasPairType or False

def check2Pairs(ranks):
    pairList = list(filter(lambda r: ranks[r] == 2, ranks.keys()))

    return pairList if len(pairList) > 1 else False

def checkHandRanking(hand):

    flush = checkFlush(hand)
    straight = checkStraight(hand)
    ranks = getRanking(hand)
    hasAHigh = max([c['rank'] for c in hand]) == 14
    hasFourOfAKind = checkPairType(ranks, 4)
    hasFullHouse = checkPairType(ranks, 3) if checkPairType(ranks, 3) and checkPairType(ranks, 2) else False
    hasthreeOfAKind = checkPairType(ranks, 3)
    hasTwoPair = check2Pairs(ranks)
    hasPair = checkPairType(ranks, 2) 
    high = max([c['rank'] for c in hand])

    cases = [
        straight and flush and hasAHigh,
        straight and flush,
        hasFourOfAKind,
        hasFullHouse,
        flush,
        straight,
        hasthreeOfAKind,
        hasTwoPair,
        hasPair,
        high
    ]

    caseIndex = [bool(value) for value in cases].index(True)

    return caseIndex, cases[caseIndex]

deck = createDeck()

shuffleDeck(deck)

player1, deck = getHand(deck)
player2, deck = getHand(deck)

print(player1)
print(player2)

player1Ranking, highPlayer1 = checkHandRanking(player1)
player2Ranking, highPlayer2 = checkHandRanking(player2)

if player1Ranking < player2Ranking:
    wins = 1
elif player1Ranking > player2Ranking:
    wins = 2
else:
    highs = [highPlayer1, highPlayer2]
    wins = 'none' if highPlayer1 == highPlayer2 else highs.index(max(highs)) + 1

print('The player who wins is ' + str(wins))

