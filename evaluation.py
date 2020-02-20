from typing import List
from high import high

def evaluation(my_list:List):
    num= [i[0] for i in my_list]
    suit= [i[1] for i in my_list]

    if suit[0]==suit[1]==suit[2]==suit[3]==suit[4] and num[0]!= num[1]: #flush
        hand=5
        msg="flush"
    elif num[0]-num[1]==1 and num[1]-num[2]==1 and num[2]-num[3]==1 and  num[3]-num[4]==1: #straight
            if suit[0]==suit[1]==suit[2]==suit[3]==suit[4]: #straight flush
                hand=1
                msg="straight flush"
            else:
                hand=6
                msg="straight"
    elif num[0]==num[1] or num[1]==num[2] or num[2]==num[3] or num[3]==num[4]: #pair
            if num[0]==num[2] and num[3]==num[4] or num[2]==num[4] and num[0]==num[1]: #full house
                hand=4
                msg="full house"
            elif num[0]==num[2] or num[1]==num[3] or num[2]==num[4]: #three of a kind
                hand=7
                msg="three of a kind"
                if num[0]==num[3] or num[1]==num[4]: #four of a kind
                    hand=3
                    msg="four of a kind"
            elif num[0]==num[1] and num[2]==num[4] or num[1]==num[2] and num[3]==num[4]:#two pairs
                hand=8
                msg="two pairs"
            else:
                hand=9
                msg="one pair"
    else:
        hand=10
        msg="highest card"

    highest_card=high(num, hand)
    return hand,highest_card,msg
