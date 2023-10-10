# Module for managing the games math and the characers stats

import Fool 
import Gambler 
import random

# Set empty variable to use as object
player = None

# Set 'player' as an instance of either 'Fool' or 'Gambler' depending on user input
# Return a boolean so App knows to call the function again if the object was not created (due to invalid input)
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

# Return the value of 'will' to App
def get_will():
    return player.will

# Return the value of 'luck' to App
def get_luck():
    return player.luck

# Return the value of 'bluff' to App
def get_bluff():
    return player.bluff

# Generate a num from 2 to 12 and add 'stat'
# Increase 'will' by 1 if random num is above the set difficulty, decrease it if it's below
def roll_dice(stat, difficulty):
    roll = random.randint(2,12) + stat

    if roll < difficulty:
        player.will -= 1
    else:
        player.will += 1

    return roll