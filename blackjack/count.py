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
