from card import Card


rank=[i for i in range(2,15)]
suit=["Spades", "Hearts", "Clubs", "Diamonds"]

def make_deck(name):
    for j in suit:
        for i in rank:
            _=Card(i,j)
            name.append((_.rank, _.suit))
