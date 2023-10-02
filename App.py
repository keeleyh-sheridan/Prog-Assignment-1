import Game

#Print welcome message
print("\nWelcome to my game! \nYou play the part of a character deeply in debt, \nputting their life into one more game in order to pay off a loan shark")

#Allow user to choose between 2 roles
selectionText = "\nChoose your role! \nThe gambler is determined to not quit before his big win, while the fool blindly stumbles into good luck. \n(gambler, fool): "
while Game.choose_role(input(selectionText)):
    print()

def print_stats():
    print("\nYour stats are:\nWill: " + str(Game.get_will()) + "\nLuck: " + str(Game.get_luck()) + "\nBluff: " + str(Game.get_bluff()))

def challenge(difficulty, statName, stat):
    input("\nPress -Enter- to roll 2 dice and add your " + statName + " stat (" + str(stat) + "): ")
    roll = Game.roll_dice(stat, difficulty)
    print("You rolled a", roll, "you need at least a", difficulty)

    if roll >= difficulty:
        print("Succeed")
    else:
        print("Fail")

print_stats()
print("Your \"Will\" decreases when you fail challenges and increases when you succeed!")

print("\nchallenge 1")
challenge(7, "bluff", Game.get_bluff())
print_stats()

print("\nchallenge 2")
for i in range(5,11,2):
    challenge(i, "luck", Game.get_luck())
print_stats()

print("\nchallenge 3")
challenge(8, "will", Game.get_will())