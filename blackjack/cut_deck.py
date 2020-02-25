def cut_deck(deck, cut_point):
    for i in range(52):
        deck[i-cut_point], deck[i]=deck[i], deck[i-cut_point]

    return deck
