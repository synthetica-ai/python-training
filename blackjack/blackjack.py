import random

from utils import cut_deck, count, check, make_deck

answer=(input("Do you want to cut the deck? Y/n \n")).lower()

if answer=="y":
    deck=[]
    make_deck(deck)
    random.shuffle(deck)

    cut=random.randint(0,52)
    deck=cut_deck(deck, 25)
    
    Flag1=False
    Flag2=False
    i=0
    hand1=0
    hand2=0

    for j in range(4):
        if j%2==0:
            hand1,i,Flag1=count(deck,hand1,i,Flag1)
        else:
            hand2,i,Flag2=count(deck,hand2,i,Flag2)

    print("Dealer has ",hand1," you have ",hand2)
    check(hand1,"Dealer")
    check(hand2,"You")


    while hand1<21 and (21-hand1)>7:
        hand1,i,Flag=count(deck,hand1,i,Flag1)
        check(hand1,"Dealer")



    answer=(input("Do you want another card? Y/n \n")).lower()
    while answer=="y":
        print(deck[i][0])
        hand2,i,Flag2=count(deck,hand2,i,Flag2)
        print("Your sum: ",hand2)
        check(hand2,"You")
        answer=(input("Do you want another card? Y/n \n")).lower()

    if hand1>=hand2 :
        print("You lost, dealer has: ", hand1," your hand: ",hand2)
    else:
        print("You won! dealer has: ", hand1," your hand: ",hand2)


else:
    exit()
