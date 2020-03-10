from operator import itemgetter

from Deck import *

deck1=Deck()

deck1.deck_shuffle()

hand1=deck1.take_hand()
hand2=deck1.take_hand()

print(sorted(hand1, key=itemgetter('rank'), reverse=True))
print(sorted(hand2, key=itemgetter('rank'), reverse=True))

suit_h1=suits(hand1)
suit_h2=suits(hand2)

s_h1=sort_hand(hand1)
s_h2=sort_hand(hand2)

ev1,high1=evaluate(suit_h1, s_h1)
ev2,high2=evaluate(suit_h2, s_h2)

if ev1<ev2:
    winner=1
elif ev2<ev1:
    winner= 2
elif high1>high2:
    winner=1
elif high2>high1:
    winner= 2
else:
    print("draw")
    exit()
print(f"Player {winner} wins")
