import random
from make_deck import make_deck



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

    print(f'Player 1 has in his hands : {player_1_hand}')
    print(f'Player 2 has in his hands : {player_2_hand}')

else:
    exit()
