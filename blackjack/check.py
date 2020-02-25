from slower import slower
@slower
def check(hand,who):
    if hand>21:
        print(who," lost! sum over 21...")
        exit()
