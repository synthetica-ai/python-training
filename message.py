def message(ev_1,ev_2,hc_1,hc_2,msg_1,msg_2):
    if ev_1<ev_2:
        print(f"\nPlayer 1 wins with {msg_1}")
    elif ev_2<ev_1:
        print(f"\nPlayer 2 wins with {msg_2}")
    elif ev_1==ev_2 and ev_1!=10:
        if hc_1>hc_2:
            print("\nPlayers have the same hand but player 1 wins with highest card")
        else:
            print("\nPlayer have the same hand but player 2 wins with highest card")
    else:
        if hc_1>hc_2:
            print("\nPlayer 1 wins with highest card")
        else:
            print("\nPlayer 2 wins with highest card")
