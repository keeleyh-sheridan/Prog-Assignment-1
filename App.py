import Game

#Print welcome message
print("\nWelcome to my game! \nYou play the part of a character deeply in debt, \nputting their life into one more game in order to pay off a loan shark")

#Allow user to choose between 2 roles
selectionText = "\nChoose your role! \nThe gambler is determined to not quit before his big win, while the fool blindly stumbles into good luck. \n(gambler, fool): "
while Game.choose_role(input(selectionText)):
    print()
print()

#Print all of the user's stats in a string
def print_stats():
    print("Your stats are:\nWill: " + str(Game.get_will()) + "\nLuck: " + str(Game.get_luck()) + "\nBluff: " + str(Game.get_bluff()))

def challenge(difficulty, statName, stat):
    input("Press -Enter- to roll 2 dice and add your " + statName + " stat(" + str(stat) + "), you need at least a " + str(difficulty))
    roll = Game.roll_dice(stat, difficulty)
    print("You rolled a", roll)

    if roll >= difficulty:
        print("Succeed")
        win = True
    else:
        print("Fail")
        win = False

    return win

print_stats()
print("Your \"Will\" decreases when you fail challenges and increases when you succeed!")

print('''
      This is it. The last night to pay of your debt, you hold your life savings worth of chips in your hands.
      You've already won a little tonight but to get what you need, you need to play at the high rollers table.
      Blocking your path is the bouncer, you can see the high roller table right behind him but first you need to convince him to let you pass.
      ''')
if challenge(7, "bluff", Game.get_bluff()):
    print('''
          He falls for your bluff, stepping aside to let you through.
          You didn't think you'd even make it this far. Confidence surges through you as you stride over to the table.
          ''')
else:
    print('''
          The bouncer is unconvinced and stares you down. Before he makes you leave, a man from behind him calls out to let you in.
          The bouncer begrudgingly steps aside to reveal a smiling man at the high rollers table waving you over, you can see in his 
          eyes that he sees you as free cash for him to win. 
          You've gotten past your first roadblock but your failed plan has shaken your will.
          ''')
    
print_stats()

print('''
      You sit down at the table, ready to try your luck at poker.
      ''')
pokerWins = 0
for i in range(5,11,2):
    if challenge(i, "luck", Game.get_luck()):
        pokerWins += 1
if pokerWins < 1:
    print('''
          You have yet to win a single hand. You're at your lowest point and your will is shattered.
          ''')
elif pokerWins < 2:
    print('''
          You've lost more than you've gained. You're starting to get desperate, your goal slowly escaping your reach.
          ''')
elif pokerWins < 3:
    print('''
          You've been playing it safe and it's slowly paying off. Your confidence is high but you're running out of time.
          ''')
else:
    print('''
          You're on the best streak of your life, you've already doubled your money and the excitement is taking over you.
          All it would take is one more big win to pull yourself out of debt.
          ''')

print_stats()

print('''
      You lock eyes with the man across from you. You recognise them from a sign you saw on your way in, the owner of the casino.
      He silently pushes his entire stack of chips into the middle of the table. The entire table folds and the man looks at you,
      waiting for your decision. Your hand is ok but not great but winning this game would surely be enough to pay of your debt.
      That said, losing will push you even further into debt. You check the time to see that the casino is about to close, this is the last hand.
      ''')
if challenge(8, "will", Game.get_will()):
    print('''
          You gather all your courage and call. He laughs and flips over his cards, he was bluffing.
          You're in shock as the dealer passes you the chips, you're free from your debt. This is the luckiest you've ever felt in your life.
          Maybe just one more hand.
          ------------------------------------------YOU WIN------------------------------------------
          ''')
else:
    print('''
          You fold and stand from the table, leaving with what you have. As you stumble into the street you try to
          come to terms with your debt plaguing you for the rest of your life. You lose.
          ------------------------------------------GAME OVER------------------------------------------
          ''')