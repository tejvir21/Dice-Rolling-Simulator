from random import *
from colorama import Fore

while True:

  dice=['''
         ____________________
        |                    |
        |   ⚪    ⚪    ⚪   |
        |                    | 
        |                    |
        |   ⚪    ⚪    ⚪   |
        |                    |
        |                    |
        |   ⚪    ⚪    ⚪   |
        |____________________|
        ''',
       '''
         ____________________
        |                    |
        |   ⚪         ⚪    |
        |                    | 
        |                    |
        |         ⚪         |
        |                    |
        |                    |
        |   ⚪         ⚪    |
        |____________________|
        ''',
       '''
         ____________________
        |                    |
        |   ⚪         ⚪    |
        |                    | 
        |                    |
        |                    |
        |                    |
        |                    |
        |   ⚪         ⚪    |
        |____________________|
        ''',
       '''
         ____________________
        |                    |
        |   ⚪               |
        |                    | 
        |                    |
        |         ⚪         |
        |                    |
        |                    |
        |               ⚪   |
        |____________________|
        ''',
       '''
         ____________________
        |                    |
        |   ⚪               |
        |                    | 
        |                    |
        |                    |
        |                    |
        |                    |
        |               ⚪   |
        |____________________|
        ''',
       '''
         ____________________
        |                    |
        |                    |
        |                    | 
        |                    |
        |         ⚪         |
        |                    |
        |                    |
        |                    |
        |____________________|
        ''']
  
  roll_the_dice=input("You want to roll the dice[y/n]: ")
  
  if roll_the_dice=='y' or roll_the_dice=='Y':
    number_on_dice=randint(0,5)
    print()
    print()
    print(dice[number_on_dice])
    print()
    print()
    continue
  else:
    break

print()
print()
print(Fore.BLACK + "*******",
      Fore.BLUE + "Thanks for playing the game 'DiceRolling'",
      Fore.BLACK + "*******")
print()
print(Fore.BLACK + "**********",
      Fore.LIGHTBLUE_EX + "Game Developer Tejvir Singh Chauhan",
      Fore.BLACK + "**********")
