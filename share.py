import random
from make_deck import make_deck
from evaluation import evaluation
from message import message

answer=(input("Do you want to play? Y/n  ")).lower()
if answer=="y":
    deck1=[]
    make_deck(deck1)
    random.shuffle(deck1)

    player_1_hand=[]
    player_2_hand=[]

    for i in range(10):
        if i%2==0:
            player_1_hand.append(deck1[i])
        else:
            player_2_hand.append(deck1[i])

    player_1_hand.sort(reverse=True)
    player_2_hand.sort(reverse=True)

    ev_1,hc_1,msg_1=evaluation(player_1_hand)
    ev_2,hc_2,msg_2=evaluation(player_2_hand)

    print(f'\nPlayer 1 has in his hands : {player_1_hand}')
    print(f'\nPlayer 2 has in his hands : {player_2_hand}')

    message(ev_1,ev_2,hc_1,hc_2,msg_1,msg_2)
else:
    exit()
