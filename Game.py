import Fool 
import Gambler 
import random

player = None

def choose_role(role):
    run = True

    global player

    if role.lower() == "fool":
        player = Fool.Player()
        run = False
    elif role.lower() == "gambler":
        player = Gambler.Player()
        run = False

    return run
