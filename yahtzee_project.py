## Please follow the instructions and complete the YAHTZEE Game
import random

def roll_a_die():
  return randint(1,6)
  
  # Instead of returning zero, this function should return
  # a random number between 1 and 6

def roll_yahtzee_dice():
  dice = []
  # Rolls 5 dice and adds them all to a list
  

  # Returns the dice list
  return dice

def display_dice(dice_list):
  dice_list=[]
  print('Your Dice are:')
  for dice in dice_list:
    print(dice)
  # Instead of printing nothing, this function should print
  # "Your dice are:" followed by all of the dice in dice_list,
  # each on its own line 

def count_score(dice_list):
  # Instead of returning zero, this function should add up
  # all the values in dice_list and return the total sum
  dice_list=[]
  result=0
  for dice in dice_list:
    result+=dice
    
  return result
  
def play_a_round():
  # Rolls dice for the user
  rolled_dice = roll_yahtzee_dice()

  # Prints out the dice
  display_dice(rolled_dice)
  
  # Checks if the user wants to reroll any dice
  reroll = input("Do you want to reroll any dice? ")

  if reroll == "yes":
    # For each die, asks the user if they want to reroll it
    for i in range(len(rolled_dice)):
      reroll_it = input("Do you want to reroll die #" + str(i + 1) + "? ")
      if reroll_it == "yes":
        # Rolls a new die and store it in the list
        # at the old die's place
        rolled_dice[i] = roll_a_die()
  
  # Prints out the dice
  display_dice(rolled_dice)

  # Gets and prints out the user's final score
  final_score = count_score(rolled_dice)
  print("Your final score is: " + str(final_score))
  
def play_yahtzee():
  # Instead of playing rounds of Yahtzee forever, this function
  # should ask the user if they want to stop after every round,
  # and break out of the loop if the user types 'stop'
  
  
  while (True):
    print("Let's play Yahtzee!")
    
    
    
    play_a_round()
    
play_yahtzee()