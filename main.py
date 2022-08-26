############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

############# Blackjack Project #############

### Imported Libraries ###
from art import logo  # Import logo from art.py
import random # Import random library. (To choose randomly from deck of cards)
from os import system, name # Create clear function. (To clear the screen)


### Functions ###
def clear():
  """ Clears the screen."""
  if name == 'nt':    # For windows.
    _ = system('cls')
  else:               # For Unix and Linux
    _ = system('clear')


def deal_card():
  """ Deals a random card from the list of cards in the deck.

  Returns:
      random_Card (int): Returns a random integer from the deck of cards.
  """
  deck_of_Cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] # Create the deck of cards. Represent Ace with 11, 10/Jack/Queen/King with 10.
  random_Card = random.choice(deck_of_Cards)  # Choose a random card from the deck of cards.
  return random_Card


def calculate_Hand(list_of_Cards):
  """ Takes a list of cards as the input and returns the sum of the Hand.

      Checks for a blackjack (a hand with only 2 cards: ace + 10) and returns 0 instead of the actual score.
      0 will represent a blackjack in the game.

      Checks for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1.

  Returns:
    hand_Sum (int) : Returns the sum of the list of cards.
  """
  hand_Sum = 0 # Create a variable to hold the sum of the Hand.
  hand_Sum = sum(list_of_Cards) # Sum the list of cards.

  # Check the hand_Sum for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score.
  if hand_Sum == 21 and len(list_of_Cards) == 2:
    return 0

  # Check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1.
  if 11 in list_of_Cards and hand_Sum > 21:
    list_of_Cards.remove(11)
    list_of_Cards.append(1)
  return hand_Sum


def compare(player_Score, dealer_Score):
  """ Compares the player's Score and the dealer's Score and returns the winner.
      Returns a string with the result of the comparison.
  """
  if player_Score == dealer_Score:
    return "\nIt's a tie!\n"
  elif player_Score == 0:
    return "\nBlackjack! \nYou win!\n"
  elif dealer_Score == 0:
    return "\nBlackjack! \nThe dealer wins!\n"
  elif player_Score > 21:
    return "\nYou busted! \nThe dealer wins!\n"
  elif dealer_Score > 21:
    return "\nThe dealer busted! \nYou win!\n"
  elif player_Score > dealer_Score:
    return "\nYou win!"
  else:
    return "\nSorry you lose, the dealer wins!\n"

def playGame():
  print(logo) # Display logo


  ### Variables ###
  player_cards = []  # Create a list to hold the player's cards.
  dealer_cards = []  # Create a list to hold the dealer's cards.
  is_game_over = False  # Create a variable to hold the game status.

  # For loop to deal the player and dealer 2 cards each.
  for i in range(2):
    player_cards.append(deal_card()) # Add the random card to the player's cards list.
    dealer_cards.append(deal_card()) # Add the random card to the dealer's cards list.

  # User Move
  while not is_game_over:
    # Call the calculate_Hand function to calculate the sum of the player's and dealer's cards.
    player_Score = calculate_Hand(player_cards)
    dealer_Score = calculate_Hand(dealer_cards)

    # Print the player's and dealer's cards and their scores.
    print(f"Your cards: {player_cards} , Your current score: {player_Score}")
    print(f"Dealer's first card: {dealer_cards[0]} \n")

    # If the player or dealer has a blackjack (0) or the player has 21, the game is over.
    if player_Score == 0 or dealer_Score == 0 or player_Score > 21:
      is_game_over = True
    else:  # If the game is not over, ask the player if they want to hit or stay.
      player_Input = input(
          "Type 'hit' to draw another card, type 'stay' to pass: ")
      if player_Input == "hit":
        # Add the random card to the player's cards list.
        player_cards.append(deal_card())
      else:
        is_game_over = True

  # Dealer Move -- Dealer will draw a card until their score is less than 17.
  while dealer_Score != 0 and dealer_Score < 17:
    dealer_cards.append(deal_card()) # Add the random card to the dealer's cards list.
    dealer_Score = calculate_Hand(dealer_cards) # Calculate the sum of the dealer's cards.

  print (f"\nYour final hand: {player_cards} , Your final score: {player_Score}")
  print (f"Dealer's final hand: {dealer_cards} , Dealer's final score: {dealer_Score}")

  # Call the compare function to compare the player's and dealer's scores and print the result.
  print(compare(player_Score, dealer_Score))


# Play again?
while input ("Do you want to play BlackJack? Type 'y' or 'n': ") == "y":
  clear()
  playGame()
