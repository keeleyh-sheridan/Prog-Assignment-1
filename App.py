import Game

#Print welcome message
print("\nWelcome to my game! \nYou play the part of a character deeply in debt, \nputting their life into one more game in order to pay off a loan shark")

#Allow user to choose between 2 roles
selectionText = "\nChoose your role! \nThe gambler is determined to not quit before his big win, while the fool blindly stumbles into good luck. \n(gambler, fool): "
while Game.choose_role(input(selectionText)):
    print()
print(Game.player)