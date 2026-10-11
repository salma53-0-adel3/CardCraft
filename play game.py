import random 
import os 
import time 
Black_jack = (r"""
                         ♠ ♥ ♣ ♦  WELCOME  ♠ ♥ ♣ ♦
                        ===========================
    .------..------..------..------..------..------..------..------..------.
    |B.--. ||L.--. ||A.--. ||C.--. ||K.--. ||J.--. ||A.--. ||C.--. ||K.--. |
    | :(): || :/\: || (\/) || :/\: || :/\: || :(): || (\/) || :/\: || :/\: |
    | ()() || (__) || :\/: || :\/: || :\/: || ()() || :\/: || :\/: || :\/: |
    | '--'B|| '--'L|| '--'A|| '--'C|| '--'K|| '--'J|| '--'A|| '--'C|| '--'K|
    `------'`------'`------'`------'`------'`------'`------'`------'`------'
                                                                                  """)
def clear_screen() :
    os.system("cls" if os.name =="nt" else "clear")
def hello() :
    print("\nLoading...") ; time.sleep(4) ; clear_screen()
def play_twenty_one() :
  def deal_card() :
    cards = [11,2,3,4,5,6,7,8,9,10,10,10]
    card = random.choice(cards)
    return card
  user = [ deal_card() for _ in range(2) ]
  comp = [ deal_card() for _ in range(2) ]
  def check_ace(card) :
     if card == 11 :
         while True :
            try :
                choice = int(input("You got an Ace card. Do you want to count it as 1 or 11? "))
                if choice == 11 or choice == 1 :
                    return choice
                else : print("Type (1/11) only !")
            except ValueError :
                print("Type (1/11) only !")
     return card
  user[0] = check_ace(user[0])
  user[1] = check_ace(user[1])
  def calculator(hand) :
    if sum(hand) > 21 and 11 in hand :
        hand[hand.index(11)] = 1
    return sum(hand)
  user_final_n = calculator(user)
  comp_final_n = calculator(comp)
  print(f"Computer's first card is {comp[0]}")
  while True :
       user_final_n = calculator(user)
       print(f"Your cards are {user}, current score is {user_final_n}")
       if user_final_n >= 21 : break
       another = input("Get another card? Y/N: ").upper().strip()
       if another == "Y" :
          user.append(deal_card()) 
       elif another == "N" : break
       else :
          print("Enter (y/n) Only !")
  while comp_final_n < 17 :
     comp.append(deal_card())
     comp_final_n = calculator(comp)
  print(f"Computer's final hand: {comp} With score {comp_final_n}")
  def results(user_total,comp_total) :
    if user_total > 21 :
        return "\ncomputer Win ! \nBetter luck next time! 🃏"
    elif comp_total > 21 :
        return "\nCongratulations you win 👏"
    elif comp_total == user_total :
        return "\nDraw ★"
    elif user_total > comp_total :
        return "\nCongratulations you win 👏"
    else :
        return "\ncomputer Win ! \nBetter luck next time! 🃏"
  print(results(user_final_n,comp_final_n))
while True :
   print("Choose a game to start...\n\n1-🐸 Froggy\n2-🎲 Twenty one\n3-🐍 Snake")
   print('_'*10)
   choice = input("Enter game name or number: ").lower().strip()
   if choice == "twenty one" or choice == "2" :
     hello()
     print(Black_jack)
     play_twenty_one()
   while True :
      restart = input("\n****Restart game?**** (y/n) ").lower().strip() 
      if restart == "y" :
        print("\nLoading..."); time.sleep(4); clear_screen() ; break
      else : break
   if restart != "y" : break