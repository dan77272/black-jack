import random
import time
import os
from art import logo
############### Blackjack Project #####################

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

print(logo)
def game():
  player_hand = [random.choice(cards), random.choice(cards)]
  dealer_hand = [random.choice(cards), random.choice(cards)]
  print(f"Your cards are: {player_hand}")
  print(f"Dealer's shown card is: {dealer_hand[0]}")
  a = True
  z = 2
  while(a):
    count = 0
    
    for card in range(len(player_hand)):
        count += int(player_hand[card])
    hit_or_stand = input("Type 's' to stand or 'h' to hit: ")
    if hit_or_stand == 'h':
      player_hand.append(random.choice(cards))
      print(f"Your cards are: {player_hand}")
      count += int(player_hand[z])
      z += 1
      if count > 21 and 11 in player_hand:
        player_hand.remove(11)
        player_hand.append(1)
        count -= 10
      if count > 21:
        print("Bust!")
        a = False
        break
      continue
    elif hit_or_stand == 's':
      break
  y = True
  while(y):
    if a == False:
      break
    dealer_count = 0
    for card in range(len(dealer_hand)):
      dealer_count += int(dealer_hand[card])
    print(f"Dealer's cards are: {dealer_hand}")
    if dealer_count < 16:
      dealer_hand.append(random.choice(cards))
      time.sleep(1)
      continue
    elif dealer_count > 21 and 11 in dealer_hand:
      dealer_hand.remove(11)
      dealer_hand.append(1)
    else:
      y = False
      break
  if count > 21:
    print("Dealer wins!")
  elif dealer_count > 21:
    print("You win!")
  elif dealer_count > count:
    print("Dealer wins!")
  elif count > dealer_count:
    print("You win!")
  else:
    print("It's a draw")
  

x = True
while(x):
  choice = input("Care to play a game of Blackjack? Type 'y' for yes or 'n' for no: ")
  os.system('clear')
  if choice == 'y':
    game()
  elif choice == 'n':
    x = False
    print("Bye!")
