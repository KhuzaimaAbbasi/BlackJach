


from art import logo

flag=False
chance=False

  
def blackjack():

  state=False
  if total_comp==21:
    print(f"Comp Cards: {comp}")
    print(f"User Cards: {user}")
    print("Blackjack~ Comp wins")
    state=True
  elif total_user==21 and total_comp != 21:
    print(f"Comp Cards: {comp}")
    print(f"User Cards: {user}")
    print("Blackjack~ User wins")
    state=True

    return state
    

def compare(total_comp,total_user):
    if total_comp>21:
        print("Comp busted ~ Game Over")
        
    elif total_comp>total_user:
        print("Computer wins")
        
    elif total_comp<total_user:
        print("User wins")
        
    elif total_comp==total_user:
        print("Draw")
        
  

def calculate(deck):

  value=0
  for x in deck:
    if x==11 and value+x>21:
      value=value+1
    else:
      value=value+x
  return value

import random

def add():
  num=random.randint(0,12)

  card=cards[num]

  return card 

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

user=[]
comp=[]




while chance==False:
  

  while flag==False:

    print(logo)
    user.append(add())
    user.append(add())
    comp.append(add())
    comp.append(add())

    total_user=calculate(user)
    total_comp=calculate(comp)


    print(f"User Cards: {user}")
    print(f"User Score: {total_user}")
    print(f"Comp first card: {comp[0]}")
    state=blackjack()
  
    if state==True:
      break
    choice=input("Do you want to hit or stay\n")
  
    if choice=="hit":
      user.append(add())
      total_user=calculate(user)
      print(f"User Cards: {user}")
      print(f"User Score: {total_user}")
      print(f"Comp first card {comp[0]}")
      if total_user>21:
        print("You busted ~ Game Over")
        break
    if choice=="stay":
      while total_comp<16:
        comp.append(add())
        total_comp=calculate(comp)
      print(f"Comp Cards: {comp}")
      print(f"Computer Score: {total_comp}")
      print(f"User Cards: {user}")
      print(f"User Score: {total_user}")
      state=blackjack()

      if state==True:
        break

      compare(total_comp,total_user)
      flag=True
  client=input("Do you wish to play again? y/n\n")

  if client=='n':
    chance=True
    break
  elif client=='y':
    user=[]
    comp=[]
 
    
   
    
      
    



  






















#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.


#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

