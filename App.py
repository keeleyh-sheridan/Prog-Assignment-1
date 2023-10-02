import Game

#Print welcome message
print("\nWelcome to my game! \nYou play the part of a character deeply in debt, \nputting their life into one more game in order to pay off a loan shark")

#Allow user to choose between 2 roles
selectionText = "\nChoose your role! \nThe gambler is determined to not quit before his big win, while the fool blindly stumbles into good luck. \n(gambler, fool): "
while Game.choose_role(input(selectionText)):
    print()

print("\nYour stats are:\nWill: " + str(Game.get_will()) + "\nLuck: " + str(Game.get_luck()) + "\nBluff: " + str(Game.get_bluff()))

print("Challenge 1")
input("\nPress -Enter- to roll 2 dice and add your bluff stat (" + str(Game.get_bluff()) + "): ")
difficulty = 7
roll = Game.roll_dice(Game.get_bluff(), difficulty)
print("You rolled a", roll, "you need at least a", difficulty)

if roll >= difficulty:
    print("Succeed")
else:
    print("Fail")