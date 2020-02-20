from typing import List

def high(my_list:List, hand):
    if hand in [3, 4, 7, 8, 9]:
        for i in range(5):
            try:
                if my_list[i]==my_list[i+1]:
                    hc=my_list[i]
                    break
            except:
                pass
    else:
        hc=my_list[0]
    return hc
