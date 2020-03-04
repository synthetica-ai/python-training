
def HandPowder(Hand):
    Num = []
    Suit = []
    a = []
    
    for i in range(0,5):
        Num.append(Hand[i][0])
        Suit.append(Hand[i][1])
    Num.sort(reverse = True)
    Suit.sort(reverse = True)
    
    if len(set(Num)) == 5:
        
        if len(set(Suit)) == 1:
            if (Num[0] - Num[4] == 4) or ((Num[1]-Num[4] == 3) and (Num[0] ==14)):
                if (Num[1] - Num[4] == 3) and (Num[0] == 14):                    
                    Num[0] = 1
                    Num.sort(reverse = True)
                a.append(9)
                a.append(Num[0])
            else:
                a.append(6)
                a.extend(Num)
        elif (Num[0] - Num[4] == 4) or ((Num[1] - Num[4] == 3) and (Num[0] == 14)):
            if ((Num[1] - Num[4]) == 3) and (Num[0] ==14):                    
                    Num[0] = 1
                    Num.sort(reverse = True)
            a.append(5)
            a.append(Num[4])
        else:
            a.append(1)
            a.extend(Num)
    
    elif len(set(Num)) == 2:
        if Num[2] != Num[3]:
            a.append(7)
            a.append(Num[2])
        else:
            a.append(8)
            a.append(Num[1])

    elif len(set(Num)) == 3:
        if (Num[0] == Num[2]) or (Num[1] == Num[3]) or (Num[2] == Num[4]):
            a.append(4)
            a.append(Num[2])
                 
        else: 
            a.append(3)
            a.append(Num[1])
            a.append(Num[3])
            a.sort(reverse = True)
            set(Num)
            for i in range(0,2):
                if Num[i] not in a: 
                    a.append(Num[i])

    else:
        for i in range(0,4):
            if Num[i] == Num[i+1]:
                a.append(2)
                a.append(Num[i])
                k = i  
        del(Num[k])
        del(Num[k])
        a.extend(Num)
 
        
                

            

    return a            


testa = [(5, 3), (11, 1), (5, 4), (10, 1), (6, 3)]
testb = [(2, 4), (12, 4), (12, 3), (13, 4), (4, 4)]
ha = HandPowder(testa)
hb = HandPowder(testb)
print(ha)
print(hb)

if ha[0] > hb[0]:
    print("O paixths A nikaei")
elif hb[0] > ha[0]:
    print("O paixths B nikaei")
else:
    if ha == hb:
        print("exoume split")
    else:
        for i in range(1,len(ha)):
            if ha[i] != hb[i]:
                break
        if ha[i] > hb[i]:
            print("o paixths A nikaei")
        else:
            print("o paixths B nikaei")
            
        
                     





    
