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

def get_will():
    return player.will

def get_luck():
    return player.luck

def get_bluff():
    return player.bluff

def roll_dice(stat, difficulty):
    roll = random.randint(2,12) + stat

    if roll < difficulty:
        player.will -= 1
    else:
        player.will += 1

    return roll